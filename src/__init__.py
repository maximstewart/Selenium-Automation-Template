#!/usr/bin/python3

# Python imports
import sys, os, json


# Application imports
from core import Context


class Main(Context):
    def __init__(self, args):
        super().__init__(args)

        try:

            with open(args.file) as f:
                self.logger.debug("Opened command file...")
                # Fill out your logic for parsing a command file...
                # Then call the "call_method" methid to run a command against that logic.
                pass

            if "true" in args.persist.lower():
                input("Press 'Enter' key to close the browser...")

        except Exception as e:
            self.logger.debug(e, exec_info=True)

        self.driver.quit()
        sys.exit(0)


    def call_method(self, method_name, data = None):
        mName  = str(method_name)
        method = getattr(self, mName, lambda data: "No valid key passed...\nkey= " + mName + "\nargs= " + data)
        return method(data) if data else method()
