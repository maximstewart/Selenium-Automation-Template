# Python imports
import os

# Lib imports
from selenium.webdriver.common.keys import Keys

# Application imports


class ControlerMixin:
    """
        The ControlerMixin has methods to manage interaction with the browser.
        These get called from the _init__.Main class and ran.
    """

    def getImage(self):
        """
            Get image of page we are on.

            :return: no return data
        """
        folder = self.domain
        if not os.path.exists(folder):
            os.mkdir(folder)

        i = 0
        name    = folder + "_" + str(i) + ".png"
        toFile  = folder + "/" + fName
        while os.path.exists(file):
            i += 1
            name   = folder + "__" + i + ".png"
            toFile = folder + "/" + fName

        self.logger.debug("Screenshot File Path/Name:  " + toFile)
        self.driver.save_screenshot(toFile)


    def createXPath(self, data):
        """
            Don't call directly.

            :return: created xpath string
        """

        keys       = data.keys()
        attribList = []
        xpathStr   = ""
        queryCount = 0

        if "elm" in keys:
            xpathStr = "//" + data["elm"] + "["
            queryCount += 1
        else:
            xpathStr = "//" + data["elm"] + "["

        if "id" in keys:
            attribList.append("@id='" + data["id"] + "'")
            queryCount += 1
        if "class" in keys:
            attribList.append("@class='" + data["class"] + "'")
            queryCount += 1
        if "type" in keys:
            attribList.append("@type='" + data["type"] + "'")
            queryCount += 1
        if "value" in keys:
            attribList.append("@value='" + data["value"] + "'")
            queryCount += 1

        if len(attribList) > 1:
            xpathStr += " and ".join(attribList)
        else:
            xpathStr += attribList[0]

        xpathStr += "]"
        self.logger.debug("Generated XPath:  " + xpathStr)
        return xpathStr
