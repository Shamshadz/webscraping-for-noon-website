from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
import time

if __name__ == '__main__':
    
    driver = uc.Chrome()

    driver.get('https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club')

    driver.maximize_window()
    time.sleep(5)
    driver.refresh()

    domain_name = []
    price = []
    # # //div[@data-cy="single-line-display"]
    # # //div[@class="d-inline-flex spins-domain-info pt-2 pb-2 pl-4 pr-1"]

    products = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,"//div[@class='d-inline-flex spins-domain-info pt-2 pb-2 pl-4 pr-1']"))
                )

    print("Scraping page Started")

#     for product in products:
#         domain_name.append(product.text)

    print(products)

# # To fake the browser
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# print(opener.open(url).read())

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# page_url = "https://in.godaddy.com"
# # waited to url
# driver.get(page_url)

# driver.maximize_window()

# time.sleep(5)
# search = driver.find_element(By.XPATH,"(//input[@class='searchInput form-control    '])[1]")
# search.send_keys("bjmtuc.club")
# time.sleep(4)  
# search.send_keys(Keys.RETURN)   
# driver.refresh()
# links = []
# EANs = []
# # //div[@data-cy="single-line-display"]
# # //div[@class="d-inline-flex spins-domain-info pt-2 pb-2 pl-4 pr-1"]
# # time.sleep()
# time.sleep(5)
# driver.refresh()
# time.sleep(5)
# products = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH,"//div[@class='d-inline-flex spins-domain-info pt-2 pb-2 pl-4 pr-1']"))
#             )

# print("Scraping page Started")

# for product in products:
#     # links.append(link.get_attribute('href'))
#     print(product.text)

#     # EAN = link.get_attribute('id').split('-')
#     # EANs.append(EAN[1])

# # count = 0
# # for link in links:
# #     driver.get(link)

#     data = []
    
#     # Locators

#     today = date.today()

#     try:
#         position = driver.find_element(By.XPATH,"//div[@class='sc-e4a456cc-5 hsjerl']").text
#     except:
#         position = ""

#     try:
#         name = driver.find_element(By.XPATH,"//h1[@class='sc-c44e3e2d-12 kODUYj']").text
#     except:
#         name = ""




#     try:
#         storeRating = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH,"//div[@class='sc-33d82e78-1 ekJjKz']"))
#         )
#         storeRating = storeRating.text
#     except:
#         storeRating = ""

#     try:
#         storeRatingCount = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH,"(//div[@class='sc-33d82e78-0 hbyggc']/div)[3]"))
#         )
#         storeRatingCount = storeRatingCount.text
#     except:
#         storeRatingCount = ""
        
#     ## making list to append data in excel (should be proper format according to headers)
#     data.append(today)
#     data.append(EANs[count])
#     data.append(position)

        

# df_bike = pd.DataFrame(columns=['Date','EAN/SKU','Position','Product Name','Currency','Product Price','Old Price','Product Rating','Product Rating Count',
#                                 'Brand','Store Name','Store Rating','Store Rating count','FBN','link'])

# df_bike.to_excel('Extraction.xlsx',index=False)
    


# driver.quit()   