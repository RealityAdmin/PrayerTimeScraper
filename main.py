from scraper import PrayerTimeScraper
import sys
import pause
import datetime
import os
import json
from dotenv import load_dotenv, dotenv_values 
from mailer import Mailer

if __name__ == '__main__':

    load_dotenv()

    scraper = PrayerTimeScraper('ICCM')
    mailer = Mailer(os.getenv('BOT_EMAIL'))
    settings = {}
    with open('settings.json') as f:
        settings = json.load(f)
    if len(settings) < 1:
        print("ERROR: Could not read settings.json")
        exit(1)
    all_emails = settings["emails"]
    print(all_emails)
    
    while True:
        now = datetime.datetime.now()
        today7am = now.replace(hour=7, minute=0, second=0, microsecond=0)
        if now > today7am:
            pause.until(datetime.datetime.today() + datetime.timedelta(days=1))
        else:
            pause.until(today7am)
        times = {}
        while not times:
            # pause.seconds(2)
            times = scraper.scrape_times()
            message = f'''The prayer times for {datetime.date.today()} are:
            
            Fajr: {times['Fajr']} 
            Sunrise: {times['Sunrise']}
            Zuhr: {times['Zuhr']}
            Asr: {times['Asr']}
            Maghrib: {times['Maghrib']}
            Isha: {times['Isha']}
'''
            print(message)
            for email in all_emails:
                mailer.send_email(message, email, os.getenv('APP_PASS'))