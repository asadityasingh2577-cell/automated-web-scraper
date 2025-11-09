# Automated Web Scraper with Scheduler

**Stack:** Python, Selenium, BeautifulSoup, Celery, Redis, SQLite

## Overview
Scrapes JavaScript-rendered web pages using Selenium, parses content with BeautifulSoup, stores results in SQLite, and runs scheduled tasks via Celery + Redis. Data can be exported to CSV.

## Quick Start
1. Clone repo:
2. Create virtualenv & install dependencies:
3. Start Redis (Docker recommended):
4. Copy `.env.example` to `.env` and adjust variables if needed
5. Initialize database:
6. Run a one-off scrape & export CSV:
7. Start periodic scraping:
8. ## Author
Aditya Singh
