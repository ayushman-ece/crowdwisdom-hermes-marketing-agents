from agents.ads_manager import AdsManagerAgent
from agents.marketing_analyzer import MarketingAnalyzerAgent
from agents.script_agent import ScriptAgent
from agents.video_agent import VideoAgent
from agents.telegram_agent import TelegramAgent

from services.logger import logger


class SupervisorAgent:

    def __init__(self):

        self.ads = AdsManagerAgent()

        self.analysis = MarketingAnalyzerAgent()

        self.script = ScriptAgent()

        self.video = VideoAgent()

        self.telegram = TelegramAgent()

    def start(self, keyword):

        logger.info("Supervisor Started")

        ads = self.ads.run(keyword)

        analysis = self.analysis.run(ads)

        scripts = self.script.run(analysis)

        videos = self.video.run(scripts)

        self.telegram.send(
            "✅ CrowdWisdom Marketing Pipeline Finished Successfully."
        )

        return videos