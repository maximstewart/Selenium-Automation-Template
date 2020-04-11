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
            Don't call directly from a command file.

            :return: created xpath string
        """
        xpathStr   = "//*["
        keys       = data.keys()
        attribLst  = []
        queryCount = 0

        if "elm" in keys:
            xpathStr = "//" + data["elm"] + "["

        flags = ["id", "class", "type", "value"]
        for key in keys:
            if key in flags:
                attribLst.append("@" + key + "='" + data[key] + "'")
                queryCount += 1

        xpathStr += ( " and ".join(attribLst) if len(attribLst) > 1 else attribLst[0] ) + "]"

        self.logger.debug("Generated XPath:  " + xpathStr)
        return xpathStr
