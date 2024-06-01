from scraper import PrayerTimeScraper
import sys

if __name__ == '__main__':
    scraper = PrayerTimeScraper(sys.argv[1])
    scraper.scrape_times()