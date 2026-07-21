import os
import json
from datetime import datetime

from services.logger import logger


class VideoService:

    def generate(self, script: str):

        os.makedirs("outputs/videos", exist_ok=True)

        # -----------------------------
        # Video Prompt
        # -----------------------------
        video_prompt = f"""
Create a cinematic 30-60 second advertisement.

Narration:
{script}

Style:
- Modern
- Professional
- Cinematic
- Fast paced
- Motivational

Resolution: 1920x1080
Aspect Ratio: 16:9
"""

        with open("outputs/videos/video_prompt.txt", "w", encoding="utf-8") as f:
            f.write(video_prompt)

        # -----------------------------
        # Storyboard
        # -----------------------------
        storyboard = {
            "title": "CrowdWisdom Trading Advertisement",
            "duration": "45 seconds",
            "scenes": [
                {
                    "scene": 1,
                    "duration": "5 sec",
                    "description": "Hook the viewer with losing trades."
                },
                {
                    "scene": 2,
                    "duration": "10 sec",
                    "description": "Show market confusion and frustration."
                },
                {
                    "scene": 3,
                    "duration": "20 sec",
                    "description": "Introduce CrowdWisdom Trading AI solution."
                },
                {
                    "scene": 4,
                    "duration": "10 sec",
                    "description": "Strong CTA and logo animation."
                }
            ]
        }

        with open("outputs/videos/storyboard.json", "w", encoding="utf-8") as f:
            json.dump(storyboard, f, indent=4)

        # -----------------------------
        # Montage Config
        # -----------------------------
        montage = {
            "engine": "OpenMontage",
            "resolution": "1920x1080",
            "fps": 30,
            "duration": 45,
            "voice": "English Male",
            "music": "Motivational",
            "status": "READY"
        }

        with open("outputs/videos/montage_config.json", "w", encoding="utf-8") as f:
            json.dump(montage, f, indent=4)

        # -----------------------------
        # Metadata
        # -----------------------------
        metadata = {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "generator": "Hermes Marketing Agent",
            "video_type": "Marketing Advertisement",
            "status": "READY_FOR_RENDER"
        }

        with open("outputs/videos/video_metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)

        logger.info("Video assets generated successfully.")

        return {
            "video_prompt": "outputs/videos/video_prompt.txt",
            "storyboard": "outputs/videos/storyboard.json",
            "montage": "outputs/videos/montage_config.json",
            "metadata": "outputs/videos/video_metadata.json"
        }