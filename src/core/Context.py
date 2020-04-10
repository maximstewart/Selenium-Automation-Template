# Python imports


# Lib imports

# Application imports
from .utils import Logger, Browser
from .mixins import ControlerMixin


class Context(ControlerMixin):
    """
        The Context class consumes mixins to add functionality as needed.
    """
    def __init__(self, args):
        """
            Construct a new 'Context' object which pulls in mixins.
            :param args: The terminal passed arguments

            :return: returns nothing
        """
        self.logger = Logger().get_logger("MAIN")
        browser     = Browser()
        self.driver = browser.get_browser(args.browser, args.headless) # The browser driver
        self.url    = ""      # The url we are pointing to
