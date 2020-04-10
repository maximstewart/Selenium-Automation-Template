# Selenium Automation Template
A template to get you setup to pass a command file and run commands.

# Note(s)
This is designed with using Python mixins to inherit functionality from discrete classes that have discrete methods. The only "global" variable should be in the Context class.

!Important! BUILD OUT THE LOGIC FIRST AS THIS IS JUST TO GET STARTED!


# Dependencies
``` sudo apt install python3 python-pip libgirepository1.0-dev ```


# Setup

*** Change directory to the src.

``` python3 -m venv ./venv ```

``` source venv/bin/activate ```

``` pip install -r requirements.txt ```

``` python . <your command file> ```

... when done ...

``` deactivate ```
