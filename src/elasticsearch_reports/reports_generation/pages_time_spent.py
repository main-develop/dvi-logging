import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import logging

load_dotenv()


def generate_pages_time_spent_report(logs) -> str | None:
    try:
        df = pd.DataFrame(logs)
        df_grouped = df.groupby(df["attributes"].apply(lambda x: x["page"]))["attributes"].apply(
            lambda x: sum(d["time_spent_s"] for d in x))

        plt.figure(figsize=(10, 5))
        df_grouped.plot(kind="bar", color="skyblue")
        plt.xlabel("Page")
        plt.ylabel("Time (seconds)")
        plt.title("Time spent on the pages")
        plt.xticks(rotation=45)

        report_filename = f"pages_time_spent_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        report_path = os.path.join(os.environ.get("REPORTS_DIR"), report_filename)

        plt.savefig(report_path, dpi=300, bbox_inches="tight")
        plt.close()

        return report_path
    except Exception as error:
        logging.error(f"An error ocurred while generating a report: {error}")

        return None
