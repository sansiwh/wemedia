#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main_spider.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2018/3/26

from selenium import webdriver

browser = webdriver.Firefox()

def get_first_page():
    browser.get('https://www.toutiao.com/')
    print(browser.find_elements("css selector",".bui-box single-mode"))

if __name__=='__main__':
    get_first_page()