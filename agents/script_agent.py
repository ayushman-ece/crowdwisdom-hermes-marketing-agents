import json
import os

from skills.script_generation import ScriptGenerationSkill
from services.logger import logger


class ScriptAgent:

    def __init__(self):

        self.skill = ScriptGenerationSkill()

    def run(self, analyses):

        logger.info("Generating Scripts")

        scripts = []

        for item in analyses:

            script = self.skill.execute(item)

            scripts.append(script)

        os.makedirs("outputs/scripts", exist_ok=True)

        with open(
            "outputs/scripts/scripts.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                scripts,
                f,
                indent=4,
                ensure_ascii=False
            )

        logger.info("Scripts Saved")

        return scripts