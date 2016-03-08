#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def initDriver():
	driver = webdriver.Firefox() #open FF
	return driver

def getPrice(driver, country):
	driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")#open page
	whatcountry = driver.find_element_by_id("countryName")#find the user input box
	whatcountry.send_keys(country)#add country
	whatcountry.send_keys(Keys.RETURN)#click enter
	driver.find_element_by_id("paymonthly").click()#click the "monthly payment" button
	price = driver.find_element_by_xpath("//div[@id='standardRates']/table[1]/tbody/tr/td[2]").text
	return price

if __name__ == "__main__":
	countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']
	driver = initDriver()
	for country in countries:
		price = getPrice(driver, country)
		print "The price of calling a landline in " + country + " is " + price + " per minute\n"
	driver.close()

