from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import json

prestaShopImportUrl = ""

WEBSITE_URL = "http://vps-59148.fhnet.fr"

SCROLL_PAUSE_TIME = 3

def open_url( url, webdriver):
    # Navigate to a whatever url recommended for setting cookies
    webdriver.get(WEBSITE_URL + '/404')
    webdriver.add_cookie({'name' : 'PHPSESSID', 'value' : 'e70ic7c2ngakrl88cgftp8t4cj', WEBSITE_URL : url})
    webdriver.add_cookie({'name': 'PrestaShop-cbac049c40e842298a95cd1e70b00bde',
                          'value': 'def5020081fc5e910fb96c9ffe631a5084654b6213c2ccb9b9e81a198d7bf25dfb66b201076cc819a4c9616d16b3625cfeb807a039b9e0f93cdbe23c4719036d6d4452e4a9a9c5f457e9141c2725f0029422481f87040017a773a26e2e1e4f7674f5bb75ef762edf54c647a22ed4596fe0d80a3108a529b65c2e34df2b79f931de50171764c24b018a1381d5d8a937914795dffc0b2450c18952c9d03d76c132a3c533fafc994845f1591b3d5656c5764d7eb15913f116d40c7d0b08b1849e38d9'
                          , 'http://188.213.25.132': url})
    webdriver.get(url)

def importproduct(url, driver):
    # mohamed-oumarou@live.com nuages1200$
    #email passwd submit_login
    #connectAsAdmin(driver)

    global prestaShopImportUrl

    if(prestaShopImportUrl != ""):
        driver.get(prestaShopImportUrl)
        time.sleep(SCROLL_PAUSE_TIME)

    prestaShopImportUrl = driver.current_url;

    #prestaShopImportUrl = 'http://188.213.25.132/admin048j6acmk/index.php/sell/catalog/products?_token=j-k-FceY1PvzdQfSIj4_Lrl4OeJAM7tTmbUDbujTd5M'
    #driver.get(prestaShopImportUrl)
    #open_url(prestaShopImportUrl, driver)
    # Click import button
    btnImportProducts = driver.find_element_by_id('ats-copy_product')
    btnImportProducts.click()

    #time.sleep(SCROLL_PAUSE_TIME)

    inputImportProduct = driver.find_element_by_id('module-copy-url')
    driver.implicitly_wait(30)
    #ActionChains(driver).move_to_element(inputImportProduct).perform()
    inputImportProduct.clear()
    # send_keys(url) does not work caused by angular issue see https://github.com/angular/angular/issues/5808
    # this is a workaround
    urls = [url[i:i+2] for i in range(0, len(url), 2)]
    for c in url:
        inputImportProduct.send_keys(c)
        driver.implicitly_wait(1)

    ElementSelectAll = driver.find_element_by_id('ats-select-unselect-all')
    ElementSelectAll.click()

    #time.sleep(SCROLL_PAUSE_TIME)

    ElementSelectAll = driver.find_element_by_name('sku')
    ElementSelectAll.click()

    #time.sleep(SCROLL_PAUSE_TIME)

    ElementSelectAll = driver.find_element_by_name('meta_title')
    ElementSelectAll.click()

    #time.sleep(SCROLL_PAUSE_TIME)

    ElementSelectAll = driver.find_element_by_name('meta_description')
    ElementSelectAll.click()

    #time.sleep(SCROLL_PAUSE_TIME)

    ElementSelectAll = driver.find_element_by_name('meta_keywords')
    ElementSelectAll.click()

    #time.sleep(SCROLL_PAUSE_TIME)

    #ElementSelectAll = driver.find_element_by_name('description')
    #ElementSelectAll.click()

    #time.sleep(SCROLL_PAUSE_TIME)

    inputImportProduct.send_keys(Keys.RETURN)

def connectAsAdmin(driver) :
    adminPageUrl = WEBSITE_URL + '/admin088yzklkw'
    open_url(adminPageUrl, driver)
    try:
        email = driver.find_element_by_id('email')
        password = driver.find_element_by_id('passwd')
        submit = driver.find_element_by_id('submit_login')

        email.send_keys('mohamed-oumarou@live.com')
        #password.send_keys('nuages1200$')
        password.send_keys('boutique1200')
        time.sleep(SCROLL_PAUSE_TIME)
        submit.click()

        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.implicitly_wait(1)
        driver.execute_script("document.body.style.zoom='75%'")

        # driver.find_element_by_id('subtab-AdminCatalog').click()
        # UrlProductsPage = driver.find_element_by_id('subtab-AdminProducts')
        # UrlProductsPage.click()


    except Exception:
        print("already connected")

def main():
    driver = webdriver.Chrome('./bin/chromedriver.exe')

    driver.implicitly_wait(30)

    connectAsAdmin(driver)

    driver.implicitly_wait(30)

    time.sleep(SCROLL_PAUSE_TIME)

    element = driver.find_element_by_id('subtab-AdminCatalog')
    element.click()

    time.sleep(SCROLL_PAUSE_TIME)

    element = driver.find_element_by_id('subtab-AdminProducts')
    element.click()

    time.sleep(SCROLL_PAUSE_TIME)

    with open('data.json') as json_file:
        data = json.load(json_file)
        time.sleep(SCROLL_PAUSE_TIME)
        for p in data:
            print('url: ' + p['url'])
            importproduct(p['url'], driver)
            time.sleep(SCROLL_PAUSE_TIME)

def test():
    driver = webdriver.Chrome('./bin/chromedriver.exe')
    driver.get('https://www.amazon.fr/Badabulle-BADABULLE-Transat-en-hauteur-compactup/dp/B07LB8KB62')


if __name__ == '__main__':
    main()
