#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main_spider.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2018/3/26

from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Firefox()

def get_first_page():
    browser.get('https://www.toutiao.com/')
    #elements = browser.find_elements_by_xpath('//a[contains(@href,"c/user")]')

    #elements = browser.find_elements_by_xpath('//div[contains(@class,"bui-left footer-bar-left")]')

    elements = browser.find_elements_by_xpath('//div[@class="bui-left footer-bar-left"]')

    for i in elements:
        #print(i.get_attribute('innerHTML'))
        html = i.get_attribute('innerHTML')
        soup = BeautifulSoup(html, "html.parser")
        name = soup.find(attrs={'ga_event':'article_name_click'})
        try:
            print(name.get_text())
            print(name["href"])
        except:
            continue

    browser.close()

if __name__=='__main__':
    get_first_page()