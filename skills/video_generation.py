from services.video_service import VideoService
from services.logger import logger


class VideoGenerationSkill:

    def __init__(self):
        self.video = VideoService()

    def execute(self, script: str):

        logger.info("Generating Video")

        return self.video.generate(script)