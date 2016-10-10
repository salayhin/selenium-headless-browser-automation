from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pdb
import urllib.parse as urlparse
import random
from random import randint
import time


class AutometicScript():
    def __init__(self):
        self.search_engine_url = 'http://www.google.de'
        #self.keyword = 'SEO Frankfurt'
        self.keyword = ["SEO Frankfurt", "Suchmaschinenoptimierung Frankfurt", "SEO Rhein Main", "Seo & Suchmaschinenoptimierung Frankfurt"]
        self.page_number = 2
        self.url = 'http://www.suchmaschinen-optimierung-frankfurt.com/'

    def search_url(self):
        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)

        cookies = driver.get_cookies()

        driver.delete_all_cookies()

        for cookie in cookies:
            driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry')})

        driver.get(self.search_engine_url)
        driver.find_element_by_name("q").is_displayed()
        driver.find_element_by_name("q").send_keys(random.choice(self.keyword))
        driver.find_element_by_name("btnG").click()
        driver.implicitly_wait(30)

        page_number = 1

        while True:
            try:
                print("page number" + str(page_number))

                if page_number > 1:
                    link = driver.find_element_by_link_text(str(page_number))
                    link.click()

                results = driver.find_elements_by_css_selector('div.g')

                for result in results:
                    link = result.find_element_by_tag_name("a")
                    href = link.get_attribute("href")
                    url = urlparse.parse_qs(urlparse.urlparse(href).query)["q"]
                    print(url)
                    if str(url[0]) == str(self.url):
                        link.click()
                        driver.implicitly_wait(120)
                        driver.find_element_by_id("wdform_1_element10").send_keys('suchmaschinenoptimierung Frankfurt')
                        driver.find_element_by_css_selector(".button-submit").click()
                        print(url)
                        driver.quit()
                        return True

                page_number += 1

            except NoSuchElementException as e:
                driver.quit()
                print(e)
                break

        pdb.set_trace()


ac = AutometicScript()

while True:
    print("starting ....")
    time.sleep(randint(1000, 3500))
    ac.search_url()

