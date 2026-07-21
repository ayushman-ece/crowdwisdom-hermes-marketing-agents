from skills.video_generation import VideoGenerationSkill
from services.logger import logger


class VideoAgent:

    def __init__(self):

        self.skill = VideoGenerationSkill()

    def run(self, scripts):

        logger.info("Generating Videos")

        videos = []

        for script in scripts:

            video = self.skill.execute(script)

            videos.append(video)

        logger.info("Videos Generated")

        return videos