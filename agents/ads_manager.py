import json
import os

from skills.ad_search import AdSearchSkill
from services.logger import logger


class AdsManagerAgent:

    def __init__(self):
        self.skill = AdSearchSkill()

    def run(self, keyword: str):

        logger.info("Ads Manager Started")

        ads = self.skill.execute(keyword)

        os.makedirs("outputs/ads", exist_ok=True)

        with open(
            "outputs/ads/ads.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                ads,
                f,
                indent=4,
                ensure_ascii=False
            )

        logger.info("Ads Saved")

        return ads