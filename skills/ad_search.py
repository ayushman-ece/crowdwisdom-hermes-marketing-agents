from services.apify_service import ApifyService
from services.logger import logger


class AdSearchSkill:

    def __init__(self):
        self.apify = ApifyService()

    def execute(self, keyword: str):

        logger.info("Running Ad Search Skill")

        ads = self.apify.search_ads(keyword)

        return ads