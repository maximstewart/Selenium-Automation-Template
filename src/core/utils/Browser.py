# Python imports

# Lib imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOptions


# Application imports


class Browser:
    """
        The Browser allows us to bring in selenium driver (a.k.a browser) related objects
    """
    def get_browser(self, browserType = None, headless = None):
        """
            Construct new selenium driver (a.k.a browser object)
            Sets the "self.driver" in Context object.
            :note: Should consider creating methods per browser type.
            :param browserType: The browser we want to use
            :param headless: If we have a gui or not

            :return: the selenium browser driver
        """
        driver    = None
        _log_path = "./core/logs/webdriver.log"

        if "firefox" in browserType:
            _options = FOptions()
            profile  = webdriver.FirefoxProfile()

            profile.accept_untrusted_certs = True
            if headless:
                _options.add_aregument("--headless")

            driver = webdriver.Firefox(options=_options, firefox_profile=profile, log_path=_log_path)


        return driver
