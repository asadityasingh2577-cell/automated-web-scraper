from init_db import init_db
from scraper import scrape_and_store
from export_csv import export_to_csv

if __name__ == "__main__":
    init_db()
    scrape_and_store()
    export_to_csv("sample_data.csv")
