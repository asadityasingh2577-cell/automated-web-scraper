import csv
from db import get_all_quotes

def export_to_csv(path="sample_data.csv", limit=None):
    rows = get_all_quotes(limit=limit)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "text", "author", "tags", "scraped_at"])
        for row in rows:
            writer.writerow(row)
    print("Exported", len(rows), "rows to", path)

if __name__ == "__main__":
    export_to_csv()
