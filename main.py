import requests
from bs4 import BeautifulSoup
from hcapbypass import bypass
import sys

# captcha_solved = bypass('pagesjaunes.fr', sys.argv[1], True)

source = requests.get('https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/').text



soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

# https://www.linkedin.com/jobs/search/?currentJobId=3288885160&geoId=100811329&keywords=Airline%20Pilot&location=Karnataka%2C%20India&refresh=true
# https://www.linkedin.com/jobs/search/?currentJobId=3356060708&geoId=106164952&keywords=Airline%20Pilot&location=Mumbai%2C%20Maharashtra%2C%20India&refresh=true
# https://www.linkedin.com/jobs/search/?currentJobId=3350527633&geoId=106187582&keywords=Airline%20Pilot&location=Delhi%2C%20India&refresh=true


# https://www.linkedin.com/jobs/search/?currentJobId=3288885160&keywords=Airline%20Pilot&location=Karnataka%2C%20India&refresh=true
# https://www.linkedin.com/jobs/search/?currentJobId=3356060708&keywords=Airline%20Pilot&location=Mumbai%2C%20Maharashtra%2C%20India&refresh=true
# https://www.linkedin.com/jobs/search/?currentJobId=3350527633&keywords=Airline%20Pilot&location=Delhi%2C%20India&refresh=true