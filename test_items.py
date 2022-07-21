import unittest
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options


def test_button_cart(browser):
    link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    browser.get(link)
    button = browser.find_element(By.XPATH,"//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

