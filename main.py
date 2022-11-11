import requests
from bs4 import BeautifulSoup
from hcapbypass import bypass
import sys

# captcha_solved = bypass('pagesjaunes.fr', sys.argv[1], True)

source = requests.get('https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/').text



soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())
