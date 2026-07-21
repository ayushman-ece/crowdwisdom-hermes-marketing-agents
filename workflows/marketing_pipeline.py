import os
import json
import time
from datetime import datetime

from agents.supervisor import SupervisorAgent
from workflows.kanban import KanbanBoard
from services.logger import logger


class MarketingPipeline:

    def __init__(self):

        self.supervisor = SupervisorAgent()

        self.kanban = KanbanBoard()

    def run(self, keyword):

        start = time.time()

        logger.info("=" * 60)
        logger.info("CrowdWisdom Marketing Pipeline Started")
        logger.info("=" * 60)

        self.kanban.update("Search Ads", "🔄 Running")

        ads = self.supervisor.ads.run(keyword)

        self.kanban.update("Search Ads", "✅ Done")

        self.kanban.update("Analyze Ads", "🔄 Running")

        analysis = self.supervisor.analysis.run(ads)

        self.kanban.update("Analyze Ads", "✅ Done")

        self.kanban.update("Generate Scripts", "🔄 Running")

        scripts = self.supervisor.script.run(analysis)

        self.kanban.update("Generate Scripts", "✅ Done")

        self.kanban.update("Generate Videos", "🔄 Running")

        videos = self.supervisor.video.run(scripts)

        self.kanban.update("Generate Videos", "✅ Done")

        self.kanban.update("Telegram Notification", "🔄 Running")

        self.supervisor.telegram.send(
            "✅ CrowdWisdom Marketing Pipeline Finished Successfully."
        )

        self.kanban.update("Telegram Notification", "✅ Done")

        end = time.time()

        self.create_execution_report(
            keyword,
            ads,
            analysis,
            scripts,
            videos,
            end - start,
        )

        logger.info("=" * 60)
        logger.info("Pipeline Finished")
        logger.info("=" * 60)

        return videos

    def create_execution_report(
        self,
        keyword,
        ads,
        analysis,
        scripts,
        videos,
        execution_time,
    ):

        os.makedirs("outputs/reports", exist_ok=True)

        report = {
            "keyword": keyword,
            "execution_date": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),
            "ads_found": len(ads),
            "analyses": len(analysis),
            "scripts_generated": len(scripts),
            "videos_generated": len(videos),
            "execution_time_seconds": round(execution_time, 2),
            "status": "SUCCESS",
        }

        with open(
            "outputs/reports/execution_report.json",
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(report, f, indent=4)

        with open(
            "outputs/reports/execution_report.md",
            "w",
            encoding="utf-8",
        ) as f:

            f.write("# Execution Report\n\n")

            f.write(f"**Keyword:** {keyword}\n\n")

            f.write(f"**Ads Found:** {len(ads)}\n\n")

            f.write(f"**Marketing Analysis:** {len(analysis)}\n\n")

            f.write(f"**Scripts Generated:** {len(scripts)}\n\n")

            f.write(f"**Videos Generated:** {len(videos)}\n\n")

            f.write(
                f"**Execution Time:** {round(execution_time,2)} seconds\n\n"
            )

            f.write("**Status:** SUCCESS\n")