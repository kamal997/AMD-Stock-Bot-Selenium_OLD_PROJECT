import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="Desktop\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
myPageTitle = driver.title

driver.get("https://discord.com/login")
time.sleep(2)
driver.find_element_by_name("email").send_keys("your_email@example.com")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_css_selector('[type="submit"]').click()
time.sleep(8)
driver.find_element_by_css_selector('[aria-label="Schließen"]').click()
driver.find_element_by_css_selector('[aria-label="Stummschalten"]').click()
#driver.switch_to_alert().accept()

driver.get("https://www.amd.com/de/direct-buy/5530312900/de")
time.sleep(2)
driver.find_element_by_id("onetrust-accept-btn-handler").click()
time.sleep(2)



 
while True:
    driver.get("https://www.amd.com/de/direct-buy/5530312900/de")
    time.sleep(2)
    driver.get("https://www.amd.com/de/direct-buy/5530312900/de")
    time.sleep(2)
    
        
    if driver.find_elements_by_class_name("btn-shopping-cart"):
        print ("IN STOCK")
        driver.get("https://discord.com/channels/@me/848328151016538163")
        time.sleep(4)
        driver.find_element_by_css_selector('[aria-label="Sprachanruf starten"]').click()
        time.sleep(20)
        driver.find_element_by_css_selector('[aria-label="Verbindung trennen"]').click()
        


    else:
        driver.find_element_by_class_name("product-out-of-stock")
        print ("OUT OF STOCK")
        driver.get("https://kamalidris.de/")
        time.sleep(2)
