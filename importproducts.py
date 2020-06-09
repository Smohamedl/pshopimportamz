from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import json


def open_url( url, webdriver):
    # Navigate to a whatever url recommended for setting cookies
    webdriver.get('http://188.213.25.132/404')
    webdriver.add_cookie({'name' : 'PHPSESSID', 'value' : 'b6n2991vc08j0utdh2ljepqk6t', 'http://188.213.25.132' : url})
    webdriver.add_cookie({'name': 'PrestaShop-cbac049c40e842298a95cd1e70b00bde',
                          'value': 'def5020093fcdf5c69e8a92c588e963889b3da73242e83bd4be359393c8bf9487de356168b89124d5f19d6e13141854dea7782424535f8dbab60d544c803d642372e56a380b38c24a45f53ce27f143b2322ec80ac30d04bcbfbd8e851653e54fa1e0fdf523cc31bf9c92ec3a62e1097dbb99b8551319d029b07f00444ba8510c1fb2e31e61950ec1c5a8a4fb1699e887ab8096bf6e48776617a067ec2bf282aa1316a846ec52460cb48b3c09c1fee47a49f9cba7c485eca54b119dcec5df4bba8c19c91c40ccaa043ca7546d1812c4b2bcd408b5608742add46f50e8a4f1716e1256bd57ada0114edce830fc335736cdf489d66dff511dcab5881770256d173d8337292a246872e818dc068e00a22f7ef11cbcb1905e972421a11e14536220b96974e21ce9209024df473084c71fb07da5a2a58d0d846ff5044e64494f0706c6b5a1b9da6eec6d615a2b35622d63fc324910fabaf491becd70186b2a25f70d264640f279ba48eb0f55733b10aa695646b3f8c2ab02d5e11603d2dab711172d13369330bfae1c5324d15297c710125236911bbd8d05848f92fc3f9a4e3a3802d47b104dc1117ac0d940a416794abc89c23ba5b33f564d879ad70d1efbfc7a5474fe10b460d589f0ad7954b51d891a0ea3c94adbeb434d6acb1c2562d5a6f1d0ead4e7ed65af28ad71d500df72dbc4', 'http://188.213.25.132': url})
    webdriver.get(url)

def importproduct(url, driver):
    # mohamed-oumarou@live.com nuages1200$
    #email passwd submit_login
    #connectAsAdmin(driver)
    prestaShopImportUrl = 'http://188.213.25.132/admin048j6acmk/index.php/sell/catalog/products?_token=3e2CQ5eUJcEaH9TBOQrBR3a4xfjMGXvk3wlRksAdmSg'
    driver.get(prestaShopImportUrl)
    #open_url(prestaShopImportUrl, driver)

    # Click import button
    btnImportProducts = driver.find_element_by_id('ats-copy_product')
    btnImportProducts.click()

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

    inputImportProduct.send_keys(Keys.RETURN)

def connectAsAdmin(driver) :
    adminPageUrl = 'http://188.213.25.132/admin048j6acmk'
    open_url(adminPageUrl, driver)
    try:
        email = driver.find_element_by_id('email')
        password = driver.find_element_by_id('passwd')
        submit = driver.find_element_by_id('submit_login')

        email.send_keys('mohamed-oumarou@live.com')
        password.send_keys('nuages1200$')
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
    print("Bienvenu au crawler Linkdin")
    keyword = "finance"
    SCROLL_PAUSE_TIME = 0.9

    connectAsAdmin(driver)
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data:
            print('url: ' + p['url'])
            importproduct(p['url'], driver)
            time.sleep(SCROLL_PAUSE_TIME)


if __name__ == '__main__':
    main()



