
class Find:

    def __init__(self,driver):
        self.driver = driver

    # driver.find_element_by_id("something")
    def findElementByID(self, idAsString):
        element = self.driver.find_element_by_id(idAsString)
        return element

    # driver.find_element_by_name('n')
    def findElementByName(self, nameAsString):
        element = self.driver.find_element_by_name(nameAsString)
        return element

    # driver.find_element_by_xpath('//*[@title="somthing"]')
    def findElementByTitle(self, titleAsString):
        title = '//*[@title="%s"]' % (titleAsString,)
        element = self.driver.find_element_by_xpath(title)
        return element

    # driver.find_element_by_xpath('//*[@aria-label="somthing"]')
    def findElementByAriaLabel(self, aria_labelAsString):
        aria_label = '//*[@aria-label="%s"]' % (aria_labelAsString,)
        element = self.driver.find_element_by_xpath(aria_label)
        return element

    # driver.find_element_by_link_text("CSV")
    def findElementByLinkText(self, linkTextAsString):
        element = self.driver.find_element_by_link_text(linkTextAsString)
        return element




