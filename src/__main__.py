
# Python imports
import argparse

# Application imports
from __init__ import Main


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        # Add long and short arguments
        parser.add_argument("--file", "-f", help="The instructions file to use.")
        parser.add_argument("--browser", "-b", default="firefox", help="ie, chrome, firefox (Optional)")
        parser.add_argument("--headless", "-hm", default=False, help="Run browser in headless mode. (Optional)")
        parser.add_argument("--persist", "-p", default=False, help="Keep browser open after run. (Optional)")


        # Read arguments (If any...)
        args = parser.parse_args()
        main = Main(args)
    except Exception as e:
        print( repr(e) )
