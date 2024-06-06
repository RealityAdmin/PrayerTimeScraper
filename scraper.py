from bs4 import BeautifulSoup
import requests

class PrayerTimeScraper:
    _website_url = ''
    _website = ''

    def __init__(self, website):
        self._website = website
        if website == 'ICCM':
            self._website_url = 'https://icnamilton.com/'

    def scrape_times(self):

        res = requests.get(self._website_url)

        if res.status_code != 200:
            return {}
        
        soup = BeautifulSoup(res.content, 'html.parser')

        ptime_container = soup.find('div', class_='prayertime')
        times = ptime_container.find_all('td', class_='subtext')
        adhan_times = {}
        adhan_categories = ['Fajr', 'Sunrise', 'Zuhr', 'Asr', 'Maghrib', 'Isha']
        for i in range(0, 6):
            adhan_times[adhan_categories[i]] = times[i].text
        return adhan_times