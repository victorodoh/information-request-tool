# INFORMATION REQUEST TOOL

An Information request tool built using `Tkinter`, `Python`; `Pandas`, `Numpy`, `Matplotlib`, `Requests`, `datetime`

## Key functions:
1. It analyses and visualises Covid-19 confirmed cases from a [UK government-provided source file](https://coronavirus.data.gov.uk/details/about-data#cases-by-age)
2. It analyses and visualises Stop and Search data retrieved from a publicly available API by the UK police which provides detailed crime data and information about individual police forces and neighbourhood teams. [API documentation](https://data.police.uk/docs/)
3. Provides end user with a single starting point / GUI to separately run both Python modules itemised in 1 & 2 above.


## Launching the GUI application:
Firstly, you need to install all required software tools, packages and their respective versions used for this project. This project supports **Python version 3 upwards**


## Installation GUIDE

1. ***Python*** :
    To install `python` [download a python interpreter](https://www.python.org/downloads/) compatible with your device (**Python 3** `is advisable for all users`). For ***Mac*** the in built one is not recommended update to **Python 3**.

2. ***Packages used*** :
    To install the packages used and their respective version which is located in the requirements.txt file. Open the project folder in **Command Prompt** and paste or type the following command `python -m pip install -r requirements.txt`. For **Mac Users** use `python3 -m pip install -r requirements.txt`.

If successfully installed the next step will be to run the application


## Start the application

Open the project folder in **Command Prompt** and type or paste this command `python -m tk_app_index`. For **Mac Users** use `python3 -m tk_app_index`, this will start the GUI application.


## Available Visualisations

The GUI can be used to check the following visualisations

`Covid -  `

1. Result of area type on a given day
2. Change and percentage change in daily cases
3. Covid cases count by month
4. Compare two areas covid cases by month

`Stop and Search - `

1. Stop and search result by age range that resulted in arrest
2. Result of self defined ethnicity
3. Stop and search result by legislation
4. Type of stop and search conducted

## How to run test (Unit and Functional)

The `TDD (Testing Driven Development)` paradigm was applied in this project. The unit and functional tests are contained in the **test_tk_app_index.py** file. 
*** Before attempting to run tests for the application, all the packages mentioned above must be installed ***

The steps listed below demonstrate how to run the functional tests used for this project and determine the application's test coverage:

1. Run **test_tk_app_index.py** file. Open the project folder in **Command Prompt** and type `python -m test_tk_app_index`. For **Mac** type `python3 -m test_tk_app_index`, this runs all the test for the GUI application.

2. To check for test coverage, Open the project folder in **Command Prompt** 
    1. We need to first run the tests with coverage, type or paste this command in terminal `python -m coverage run -m unittest discover`. For **Mac** use `python3 -m coverage run -m unittest discover`, this runs all the test for the GUI application and calculates the coverage.
    
    2. To report the coverage in **Command Prompt** type or paste this command `python -m coverage report -m`. For **Mac** use `python3 -m coverage report -m`, this shows the coverage of the tests.
