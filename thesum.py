# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import pandas as pd
import os
import sys

# Hidden mode
options = Options()
options.headless = True

# Drive Settings
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Global Variables
WEBSITE = 'https://www.thesun.co.uk/sport/football/'
PATH = os.path.dirname(sys.executable)

titles = list()
subtitles = list()
links = list()
my_dict = {'title': titles, 'subtitles': subtitles, 'link': links}


def day_mouth_year():
    """ Return the date on format DD-MM-YYYY"""
    now = datetime.now()
    return now.strftime('%d%m%Y')


def access_website():
    """Go to access website"""
    driver.get(WEBSITE)


def extract_information():
    """Extracts the information of titles, subtitles and links of every pages"""
    containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

    for container in containers:
        title = container.find_element(by='xpath', value='./a/h2').text
        subtitle = container.find_element(by='xpath', value='./a/p').text
        link = container.find_element(by='xpath', value='./a').get_attribute('href')
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)


def filename():
    """Returns the final name of the file"""
    return os.path.join(PATH, f'headlines-{day_mouth_year()}.csv')


def export_to_csv():
    """Convert the dataframe file to format csv"""
    df_headlines = pd.DataFrame(my_dict)
    df_headlines.to_csv(filename())


if __name__ == '__main__':
    access_website()
    extract_information()
    export_to_csv()
    driver.quit()
