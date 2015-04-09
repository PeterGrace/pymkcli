pymkcli
=======

This project creates a skeleton python project with some basic mix-ins that facilitate producing well-behaved command line apps in python.

Dependencies used
-----------------
- Click
- Blessings
- GitPython


What it does
------------
- Creates a new folder for your project
- Puts a README file and setup.py file in that folder
- creates a module folder under your project folder, with a blank __init__.py file.
- creates the main.py template in the module folder where your app can be written


How to use
----------
- Clone this repo.
- (Optional) enter into the virtualenv of your choice
- Execute `pip install .` in the directory to install the `pymkcli` command in your path.
- Use the `pymkcli` command to create a new project, e.g. `pymkcli mynewproject`
