# Screenpy-selenium-example

Repository for the tutorial of Screenpy-Selenium with pytest


## Requirements

- Python 3.11.
- Pip.
- Pipenv 
- screenpy.
- screenpy-selenium.
- screenpy-adapter-allure.

## How to run the project

First install pip and pipenv and run the command to create the environment in the folder where the project was cloned/downloaded:

`pipenv install`

After the virtual environment was created run the following command:

`pipenv sync`

This command will install the necessary packages for the project.

To enter to the virtual env run:

`pipenv shell`

Now run the project with:

`pytest`

To generate the allure-report run the following command

`pytest --alluredir="path-where-to-create-the-allure-report-folder"`

And run with:

`allure serve <path-of-the-project>`