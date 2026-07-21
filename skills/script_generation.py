from services.openrouter_service import OpenRouterService
from services.logger import logger


class ScriptGenerationSkill:

    def __init__(self):
        self.llm = OpenRouterService()

    def execute(self, analysis: str):

        logger.info("Generating Advertisement Script")

        prompt = f"""
Create THREE different 30-60 second advertisement scripts.

Script 1:
Pain Focused

Script 2:
Unique Data Focused

Script 3:
CrowdWisdom Solution Focused

Analysis:

{analysis}
"""

        return self.llm.ask(prompt)