import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    # Create webdriver and connect to chromedriver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('/root/chromedriver', chrome_options=options)
    driver.set_window_size(1024, 960)

    try:
        # Visit https://tw.yahoo.com/
        driver.get("https://tw.yahoo.com")

        # Find input box and put "hello world" in.
        inputs = driver.find_element_by_xpath('//*[@id="UHSearchBox"]')
        inputs.send_keys("hello world")

        # Find search button and click it.
        driver.find_element_by_xpath('//*[@id="UHSearchWeb"]').click()

        # Save current page to 'yahoo.png'
        driver.save_screenshot('yahoo.png')

        # Print page html source
        print(driver.page_source.encode('utf-8'))
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
