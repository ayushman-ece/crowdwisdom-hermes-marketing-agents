import json
import os

from skills.pain_analysis import PainAnalysisSkill
from services.logger import logger


class MarketingAnalyzerAgent:

    def __init__(self):
        self.skill = PainAnalysisSkill()

    def run(self, ads):

        logger.info("Marketing Analysis Started")

        analyses = []

        for ad in ads:

            analysis = self.skill.execute(str(ad))

            analyses.append(analysis)

        os.makedirs("outputs/analysis", exist_ok=True)

        with open(
            "outputs/analysis/analysis.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                analyses,
                f,
                indent=4,
                ensure_ascii=False
            )

        logger.info("Analysis Saved")

        return analyses