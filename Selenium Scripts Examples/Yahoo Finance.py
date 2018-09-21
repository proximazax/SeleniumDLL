
import DriverClass
import FindElement
import Inputs
import time

page_load_timeOut = 30

Driver = DriverClass.Driver('Chrome', loadTimeInSeconds=page_load_timeOut)
URL = "https://finance.yahoo.com/"
Driver.openWebsite(url=URL)

driver = Driver.getDriver()

elm_searchBar = FindElement.findElementByName(driver, 'p')
keyboard = Inputs.Keyboard(driver)
mouse = Inputs.Mouse(driver)
keyboard.writeTextToElement(element=elm_searchBar, inputAsString='EBAY')
elm_searchBtn = FindElement.findElementByID(driver, "search-button")
time.sleep(1)
mouse.clickOnAnElement(element=elm_searchBtn)

time.sleep(5)
driver.quit()















