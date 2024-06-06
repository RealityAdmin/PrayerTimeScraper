from scraper import PrayerTimeScraper
import sys
import pause
import datetime

datetime.t

if __name__ == '__main__':
    scraper = PrayerTimeScraper(sys.argv[1])
    while True:
        times = {}
        while not times:
            times = scraper.scrape_times()
            print(times)
        pause.seconds(5)