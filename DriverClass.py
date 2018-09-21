
from selenium import webdriver
import os
CHROME = 'Chrome'
FIRE_FOX = 'Firefox'
EXPLORER = 'Explorer'


class Driver:

    def __init__(self, driverTypeAsString, loadTimeInSeconds=30):
        driver = None

        if driverTypeAsString == CHROME:
            # D:\PythonProjectInD\SeleniumDLL\Drivers
            DriversFolder = 'Drivers/'
            path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), DriversFolder))
            driver = webdriver.Chrome(path + "/chromedriver.exe")
        elif driverTypeAsString == FIRE_FOX:
            print('Enter firefox driver location')
            # driver = webdriver.Firefox()
        elif driverTypeAsString == EXPLORER:
            print('Enter explorer driver location')
            # driver = webdriver.Ie("Drivers\IEDriverServer.exe")


        self.driver = driver
        self.driver.set_page_load_timeout(loadTimeInSeconds)

    def getDriver(self):
        return self.driver

    def setLoadTimeout(self, loadTimeInSeconds):
        self.driver.set_page_load_timeout(loadTimeInSeconds)

    def openWebsite(self,url):
        self.driver.get(url)



