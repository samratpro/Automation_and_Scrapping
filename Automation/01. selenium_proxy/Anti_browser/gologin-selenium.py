import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from gologin import GoLogin
from gologin import getRandomPort


gl = GoLogin({
	"token": "yU0token",
	"profile_id": "yU0Pr0f1leiD"
	})

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"
	
service = Service(executable_path=chrome_driver_path)

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
time.sleep(3)
driver.quit()
time.sleep(3)
gl.stop()
