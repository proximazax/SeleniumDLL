from selenium import webdriver
from selenium.webdriver.common.by import By

# driver.find_element_by_id("something")
def findElementByID(driver, idAsString):
    element = driver.find_element_by_id(idAsString)
    return element


# driver.find_element_by_name('n')
def findElementByName(driver, nameAsString):
    element = driver.find_element_by_name(nameAsString)
    return element


# driver.find_element_by_xpath('//*[@title="somthing"]')
def findElementByTitle(driver, titleAsString):
    title = '//*[@title="%s"]' % (titleAsString,)
    element = driver.find_element_by_xpath(title)
    return element


# driver.find_element_by_xpath('//*[@aria-label="somthing"]')
def findElementByAriaLabel(driver, aria_labelAsString):
    aria_label = '//*[@aria-label="%s"]' % (aria_labelAsString,)
    element = driver.find_element_by_xpath(aria_label)
    return element


# driver.find_element_by_link_text("CSV")
def findElementByLinkText(driver, linkTextAsString):
    element = driver.find_element_by_link_text(linkTextAsString)
    return element




