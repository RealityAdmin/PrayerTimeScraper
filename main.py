from scraper import PrayerTimeScraper
import sys
import pause
import datetime
import os
from dotenv import load_dotenv, dotenv_values 
from mailer import Mailer

if __name__ == '__main__':

    load_dotenv()

    scraper = PrayerTimeScraper('ICCM')
    mailer = Mailer(os.getenv('BOT_EMAIL'), os.getenv('MY_EMAIL'))
    mailer.send_email('Test', os.getenv('APP_PASS'))
    while True:
        times = {}
        while not times:
            times = scraper.scrape_times()
            print(times)
        pause.seconds(5)