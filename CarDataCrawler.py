# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:59:43 2019

@author: Nicholas V. Nikolov
"""

# Imports
from urllib.request import Request, urlopen
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np



def LinkCreator():
    # Create reference to main webpage that will be used to seek out various car makes and models
    url = 'https://www.carspecs.us/'
    response = requests.get(url)
    
    # The beautiful soup result of parsing the main page. Will search for links to pursue
    bsMain = BeautifulSoup(response.text,"html.parser")
    
    for i in range(24,92):
        MainLinkList = bsMain.findAll('a')
        make = MainLinkList[i]['href']
        NewUrl = url + make[1:]
        
        NewResponse = requests.get(NewUrl)
        
        bsYears = BeautifulSoup(NewResponse.text,'html.parser')
        
        # The considered years for data. Only cars of the following years will be used
        yr2019 = [x for x, y in enumerate(bsYears.findAll('a')) if '2019' in y]
        
        if yr2019:
            yr2019 = yr2019[0]
            
            # Get the year part of link to append to make like
            year = bsYears.findAll('a')[yr2019]['href']

            # New url with years
            NewUrl = url + year[1:]
            
            # Selecting the model
            NewResponse = requests.get(NewUrl)

            bsModels = BeautifulSoup(NewResponse.text,'html.parser')

            MainLinkList = bsModels.findAll('a')
            
            
            # This separates the list of links from the rest of the page. It seems this always appears between
            # Cars and privacy policy. Note, if this changes, this code might become deprecated.
            ModelLowIndex = [x for x, y in enumerate(bsYears.findAll('a')) if 'Cars' in y][0]
            ModelHighIndex = [x for x, y in enumerate(bsYears.findAll('a')) if 'Privacy Policy' in y][0]
            
            # Create the loop here to go through the models and eventually
            # and save to array or run another function to populate the dataframe
            
        yr2018 = [x for x, y in enumerate(bsYears.findAll('a')) if '2018' in y]
        
        if yr2018:
            yr2018 = yr2018[0]
       # year19 = bsYears.findAll('a')[yr2019]['href']
       # year18 = bsYears.findAll('a')[yr2018]['href']
        
       # NewUrl19 = url + year19[1:]
      #  NewUrl18 = url + year18[1:]
        
       # print(NewUrl19)
        
LinkCreator()