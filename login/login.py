# -*- coding:utf-8 -*-
"""
  @author:ly
  @file: login.py
  @time: 2018/7/1916:51
  @version: v1.0
  @Dec: 登录金斧子
"""

import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

conf = configparser.ConfigParser()
conf.read('..\conf.ini')
chromedriver = conf.get('config','chromedriver')

os.environ["webdriver.chrome.driver"] = chromedriver
option = webdriver.ChromeOptions()
# option.add_argument("headless")
browser = webdriver.Chrome(chromedriver,chrome_options=option)

url = "https://passport.jinfuzi.com/passport/user/login"
browser.get(url)
WebDriverWait(browser, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm_username"]')))
element = browser.find_element_by_xpath('//*[@id="loginForm_username"]')
element.send_keys('13279435349')
time.sleep(random.randrange(1,20))
WebDriverWait(browser, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm_password"]')))
element = browser.find_element_by_xpath('//*[@id="loginForm_password"]')
element.send_keys('P@ssw0rd')
time.sleep(random.randrange(1,20))
WebDriverWait(browser, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm_submit"]')))
element = browser.find_element_by_xpath('//*[@id="loginForm_submit"]')
element.click()