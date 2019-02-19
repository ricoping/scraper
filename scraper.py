import requests, time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class Scraper():
		def __init__(self, url):
			self.url = url

		def staticUrlParser(self): #Get html text
			response = requests.get(self.url)
			response.raise_for_status()
			source = response.text
			return source

		def dynamicUrlParser(self):
			options = Options()
			options.add_argument('-headless')
			exe_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static", "geckodriver.exe"))
			browser = webdriver.Firefox(executable_path = exe_path, firefox_options=options)
			browser.get(self.url)
			source = browser.page_source
			browser.close()
			return source

		def dynamicUrlParserByTarget(self, target):
			options = Options()
			options.add_argument('-headless')
			exe_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static", "geckodriver.exe"))
			browser = webdriver.Firefox(executable_path = exe_path, firefox_options=options)
			browser.get(self.url)
			element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "js-stream-item")))
			source = browser.page_source
			browser.close()
			return source

def cleaner(sentence):
	cleaned = ""
	for s in sentence:
		try:
			tmp = open('tmp.txt','w')
			tmp.write(s)
			cleaned += s
		except:
			continue
	return cleaned