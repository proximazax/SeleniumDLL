import FindElement
import DriverClass
import Inputs
import time

symbol = "EBAY"

page_load_timeOut = 30


Driver = DriverClass.Driver('Chrome', loadTimeInSeconds=page_load_timeOut)
URL = "https://finance.yahoo.com/quote/%s/history?p=%s" % (symbol,symbol,)
Driver.openWebsite(url=URL)

keyboard = Inputs.Keyboard(Driver)
mouse = Inputs.Mouse(Driver)

time.sleep(2)
elm_downloadBtn = Driver.Find.findElementByClass("Fl(end) Mt(3px) Cur(p)")
mouse.clickOnAnElement(elm_downloadBtn)

time.sleep(10)
Driver.close()
# driver.quit()
























