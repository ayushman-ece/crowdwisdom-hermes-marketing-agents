import json
import subprocess
import re
from pathlib import Path
from datetime import datetime

from services.logger import logger


class VideoService:

    def __init__(self):
        # Better project root detection (Assumes this file is in a /services or similar subfolder)
        self.project_root = Path(__file__).resolve().parent.parent
        self.output_dir = self.project_root / "outputs" / "videos"
        self.composer_dir = self.project_root / "OpenMontage" / "remotion-composer"
        self.props_file = self.output_dir / "props.json"
        self.video_output = self.output_dir / "output.mp4"

        # Create outputs/videos if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def split_script(self, script: str) -> list:
        # Automatically creates one scene per sentence
        parts = re.split(r"[.!?]\s+", script)
        return [p.strip() for p in parts if p.strip()]

    def build_cuts(self, lines: list) -> list:
        cuts = []
        current_time = 0

        for i, line in enumerate(lines, start=1):
            # Calculate dynamic duration based on word count (between 3 and 6 seconds)
            word_count = len(line.split())
            duration = max(3, min(6, round(word_count / 2)))
            
            cuts.append({
                "id": f"scene{i}",
                "type": "text_card",
                "title": f"Scene {i}",
                "text": line,
                "in_seconds": current_time,
                "out_seconds": current_time + duration
            })
            current_time += duration

        return cuts

    def build_props(self, script: str) -> dict:
        lines = self.split_script(script)
        cuts = self.build_cuts(lines)
        
        # IMPORTANT: Ensure these keys perfectly match what your Explainer.tsx expects!
        return {
            "cuts": cuts,
            "overlays": [],
            "captions": [],
            "audio": {},
            "theme": "clean-professional"
        }

    def save_props(self, props: dict):
        with open(self.props_file, "w", encoding="utf-8") as f:
            json.dump(props, f, indent=4)

    def generate(self, script: str) -> dict:
        logger.info("Starting video generation...")

        # Handle empty scripts
        script = script.strip()
        if not script:
            raise ValueError("Generated script is empty.")

        # Check if npx exists and catch the FileNotFoundError if Node isn't installed
        # Updated for Windows compatibility
        try:
            subprocess.run(
                ["cmd", "/c", "npx", "--version"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        except FileNotFoundError:
            raise RuntimeError("Node.js / npx is not installed.")
        except subprocess.CalledProcessError:
            raise RuntimeError("npx is not working correctly.")

        # Check OpenMontage directory exists
        if not self.composer_dir.exists():
            raise FileNotFoundError(f"Composer not found: {self.composer_dir}")

        # Verify composer contents (entry file)
        index_file = self.composer_dir / "src" / "index.tsx"
        if not index_file.exists():
            raise FileNotFoundError(f"Missing Remotion entry file: {index_file}")

        # Build props and save them
        props = self.build_props(script)
        self.save_props(props)

        # Log props content for debugging
        logger.info("Props generated:")
        logger.info(json.dumps(props, indent=2))

        # Check props.json
        if not self.props_file.exists():
            raise FileNotFoundError("props.json not created.")

        # Render command setup with Windows cmd /c
        render_cmd = [
            "cmd",
            "/c",
            "npx",
            "remotion",
            "render",
            "src/index.tsx",
            "Explainer",
            str(self.video_output),
            "--props",
            str(self.props_file),
            "--codec",
            "h264"
        ]

        logger.info(f"Props: {self.props_file}")
        logger.info(f"Output: {self.video_output}")
        logger.info(f"Render command: {' '.join(render_cmd)}")
        logger.info("Running Remotion renderer...")
        
        # Error handling & Execution
        try:
            result = subprocess.run(
                render_cmd,
                cwd=self.composer_dir,
                check=True,
                capture_output=True,
                text=True
            )
            # Print stdout/stderr cleanly
            if result.stdout:
                logger.info(result.stdout)
            if result.stderr:
                logger.warning(result.stderr)
            
        except subprocess.CalledProcessError as e:
            # Print stderr on failure
            logger.error(f"Video rendering failed: {e}")
            if e.stderr:
                logger.error(e.stderr)
            raise

        # Check output.mp4
        if not self.video_output.exists():
            raise RuntimeError("Video was not generated.")

        # Metadata
        metadata = {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "generator": "Hermes Marketing Agent",
            "renderer": "Remotion",
            "engine": "OpenMontage",
            "video": str(self.video_output),
            "props": str(self.props_file),
            "status": "SUCCESS"
        }

        metadata_path = self.output_dir / "video_metadata.json"
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)

        logger.info("Video rendered successfully.")

        # Return final file paths
        return {
            "video": str(self.video_output),
            "props": str(self.props_file),
            "metadata": str(metadata_path)
        }