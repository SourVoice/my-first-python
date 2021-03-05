import requests
from bs4 import BeautifulSoup
import sys


class Download(object):

    def __init__(self):
        self.server = ''
        self.target = ''
        self.nums = 0
        self.names = []
        self.urls = []

    def get
