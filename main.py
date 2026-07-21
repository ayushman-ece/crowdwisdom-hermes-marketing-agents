from workflows.marketing_pipeline import MarketingPipeline
from services.logger import logger
from config import APIFY_API_TOKEN



def banner():

    print("=" * 70)
    print(" CrowdWisdom Hermes AI Marketing Agents ")
    print("=" * 70)


def main():

    banner()

    logger.info("Project Started")

    keyword = input(
        "\nEnter Product / Niche to search ads for : "
    ).strip()

    if not keyword:

        print("Keyword cannot be empty.")
        return

    pipeline = MarketingPipeline()

    videos = pipeline.run(keyword)

    print("\n")
    print("=" * 70)
    print("Pipeline Completed Successfully")
    print("=" * 70)

    print(f"\nVideos Generated : {len(videos)}")

    print("\nOutputs Saved In:")

    print("outputs/ads/")
    print("outputs/analysis/")
    print("outputs/scripts/")
    print("outputs/videos/")
    print("outputs/reports/")

    logger.info("Project Finished")


if __name__ == "__main__":
    main()