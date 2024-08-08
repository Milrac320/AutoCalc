import sys
import re
import os
import json
import psutil
from decimal import Decimal
import time
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFrame, QHBoxLayout, QPushButton, QCheckBox, QFileDialog, QLineEdit, QMessageBox, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QScreen
import warnings
import datetime
import xlrd
import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By