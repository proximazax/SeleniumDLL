import DriverClass, Inputs, FindElement

import time

Driver = DriverClass.Driver("Chrome")

URL = "https://www.tase.co.il/he/market_data/indices/updates/parameters/listed_capital?dType=0&View=1"
Driver.openWebsite(URL)
# driver = Driver.getDriver()

keyboard = Inputs.Keyboard(Driver)
mouse = Inputs.Mouse(Driver)

time.sleep(3)
# Find
elm_downloadIcon = Driver.Find.findElementByAriaLabel("הורדת נתונים")
# elm_downloadIcon = FindElement.findElementByAriaLabel(driver, "הורדת נתונים")
mouse.clickOnAnElement(elm_downloadIcon)

time.sleep(2)
elm_csvBtn = Driver.Find.findElementByLinkText("CSV")
# elm_csvBtn = FindElement.findElementByLinkText(driver, "CSV")
mouse.clickOnAnElement(elm_csvBtn)

# Time to download the file
time.sleep(30)
Driver.close()
# driver.quit()









