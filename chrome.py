from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

PATH = "/home/linuxone/hus/code/chromedriver/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--user-data-dir=chrome-data")
#options.add_argument("user-data-dir=C:\environments\selenium")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#driver = webdriver.Chrome(options=options, executable_path=r"/home/linuxone/hus/env/chromedriver")

def post_ad(profile,title):
    options.add_argument("user-data-dir=C:\environments\selenium\"" + profile)
    driver = webdriver.Chrome(options=options, executable_path=r"/home/linuxone/hus/code/jiji/chromedriver/chromedriver")

    driver.get("https://www.kijiji.ca/")
    print("OPENING KIJIJI")
    time.sleep(10)
    

    element = driver.find_element_by_class_name("headerButtonPostAd-1524038143")
    highlight(element)
    element.click()
    time.sleep(10)
    print("ClICKING POST AD")

    
    element = driver.find_element_by_id("AdTitleForm")
    highlight(element)
    element.send_keys("DRAKE AND PIZZARONI")
    print("DUMMY TITLE")
    time.sleep(18)
    element = driver.find_element_by_xpath('//button[normalize-space()="Next"]')
    highlight(element)
    element.click()
    print("CONTINUE AD POSTING")
    time.sleep(10)


    file = open('ads/' + title + '/category.txt', 'r')
    categories = file.read().splitlines()
    print(categories)
    time.sleep(12)

    for category in categories:
        element = driver.find_element_by_xpath('//button[normalize-space()="' + category +'"]')
        print("CHOOSING ", category)
        highlight(element)
        element.click()
        time.sleep(5)

    time.sleep(10)

    if (len(driver.find_elements_by_id('desktopbrand_s'))>0):
        print("BRAND OPTION EXISTS")
        file = open('ads/' + title + '/brand.txt', 'r')
        f = str(file.read())
        select = Select(driver.find_element_by_id('desktopbrand_s'))
        time.sleep(1)
        print("ENTERING BRAND")
        select.select_by_value(f.strip())


    print("READING TITLE")
    file = open('ads/' + title + '/title.txt', 'r')
    f = file.readline()
    element = driver.find_element_by_id("postad-title")
    highlight(element)
    element.clear()
    element.send_keys(f)
    print("ENTERING TITLE")
    time.sleep(10)


    element = driver.find_element_by_id("pstad-descrptn")
    highlight(element)
    print("READING DESCRIPTION")
    file = open('ads/' + title + '/description.txt', 'r')
    f = file.readlines()
    element.send_keys(f)
    print("ENTERING DESCRIPTION")
    time.sleep(5)


    element = driver.find_element_by_id("PriceAmount")
    print("READING PRICE")
    file = open('ads/' + title + '/price.txt', 'r')
    f = file.readlines()
    element.send_keys(f)
    print("ENTERING PRICE")
    time.sleep(5)


    file = open('ads/' + title + '/pictures/count.txt', 'r')
    f = file.readline()
    print(f[:-1] + "IMAGES TO UPLOAD")
    element = driver.find_element_by_xpath("//div[@id=\"FileInputWrapper\"]/div/div/input")
    
    for x in range(int(f)):
        element.send_keys("/home/linuxone/hus/code/jiji/ads/"+title+"/pictures/" + str(x+1) + ".jpg")
        print("IMAGE " + str(x) + " UPLOADED")
        time.sleep(4)
    time.sleep(5)

    element = driver.find_element_by_xpath('//button[normalize-space()="Change"]')
    element.click()
    print("CHANGE LOCATION")
    time.sleep(5)

    file = open('ads/' + title + '/postal.txt', 'r')
    print("READING POSTAL CODE")
    f = file.readline()
    element = driver.find_element_by_id("location")
    print("ENTERING POSTAL CODE")
    element.send_keys(f)
    time.sleep(5)

    element = driver.find_element_by_id("LocationSelector-item-0")
    print("CHOOSING LOCATION")
    element.click()    
    time.sleep(1)

    element = driver.find_element_by_xpath('//button[normalize-space()="Post Your Ad"]')
    highlight(element)
    time.sleep(2)
    element.click()
    print("Posting AD")
    time.sleep(10)

    
    ad_id = str(driver.current_url)
    driver.close()
    time.sleep(2)
    return ad_id

def delete_ad(profile,ad_id):
    options.add_argument("user-data-dir=C:\environments\selenium\"" + profile)
    driver = webdriver.Chrome(options=options, executable_path=r"/home/linuxone/hus/code/jiji/chromedriver/chromedriver")

    driver.get("https://www.kijiji.ca/v-view-details.html?"+ ad_id)
    print("OPENING AD TO DELETE")
    time.sleep(4)


    element = driver.find_element_by_xpath('//button[normalize-space()="Delete"]')
    print("DELETE BUTTON")
    highlight(element)
    element.click()
    time.sleep(5)


    element = driver.find_element_by_xpath("//div[@id=\"modalOverlay\"]/div/div/div/div[2]/div/div/div/span[4]/button")
    print("PREFER NOT TO SAY")
    highlight(element)
    element.click()
    time.sleep(5)

    
    element = driver.find_element_by_xpath("//div[@data-testid='delete-CTA']/button")
    print("CONFIRMING DELETE")
    highlight(element)
    element.click()
    time.sleep(5)

def kijiji(profile):
    options.add_argument("user-data-dir=C:\environments\selenium\"" + profile)
    driver = webdriver.Chrome(options=options, executable_path=r"/home/linuxone/hus/code/jiji/chromedriver/chromedriver")
    
    input("Press ENTER to exit chrome.")

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(2)
    apply_style(original_style)
    