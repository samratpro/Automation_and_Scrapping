# Using smartproxy.com

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from extension import proxies

# smartproxy.com
username = 'user-spf1lb1tfd-session-1'
password = '4ihsvz3mMtW18d=mUE'
endpoint = 'gate.smartproxy.com'
port = '7000'
chrome_options = webdriver.ChromeOptions()
proxies_extension = proxies(username, password, endpoint, port)
chrome_options.add_extension(proxies_extension)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("link)
driver.quit()
