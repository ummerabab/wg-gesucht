## WG-Gesucht

SoSe21 Computational Social Science Lab Project - WG-Gesucht

This project creates a Dataset of advertisements from the most common shared housing website WG-Gesucht and analyses the differences in their sentiments and age and gender preferences, which influence an individual's search for a shared accomadation.


## Project setup

We recommend creating a Python virtual environment before setting up the project. More details regarding virtual environments for Python can be found https://docs.python.org/3/library/venv.html or https://docs.conda.io/en/latest/.

## Installation Guide

Using "pip install" download the following libraries :

- BeautifulSoup
- Matplotlib
- Numpy
- Pandas
- Pickle
- Random
- Re
- Selenium
- Scipy

# Load selenium components

from selenium import webdriver

Download and install the correct version of chrome webdriver or firefox geckodriver and 
extract the file in your desired PATH and paste the PATH in the code.
Chrome- https://chromedriver.chromium.org/downloads
Firefox- https://github.com/mozilla/geckodriver/releases

## Code structure

Dataset collection is done in the file 'data_collection.ipynb' and 'listings.ipynb'. Once the dataset is created, Sentiment Analysis is carried out Sentiment_Analysis_Textblob.ipynb and age, gender preferences are analysed in 'age_gender_preference.ipynb'.

