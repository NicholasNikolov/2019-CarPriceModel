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


# This method builds the actual dataframe which will be filled with data
def DataFrameBuilder():
    # This assumes that all cars have the same variables
    link = 'https://www.carspecs.us/cars/2019/acura/mdx'
    NewResponse = requests.get(link)
    variables = []
    for i in range(72):
        variables.append(BeautifulSoup(NewResponse.text,
                                       'html.parser')
                                        .findAll(True,{'class':'pure-u-1 pure-u-md-1-2'})[i]
                                        .get_text().strip()
                                        .split('\r\n')[0])
    CarData = pd.DataFrame(columns = variables)
    print('success')
    return(CarData)
    
    
    
    
def MakeList():
    link = 'https://carspecs.us'
    response = requests.get(link)
    makes = []
    
    



# This method will extract URL's for the designated makes and years.
def UrlSeeker(make,year):
    # Create reference to main webpage that will be used to seek out various car makes and models
    url = 'https://www.carspecs.us/'
    response = requests.get(url)
    
    # The beautiful soup result of parsing the main page. Will search for links to pursue
    bsMain = BeautifulSoup(response.text,"html.parser")
    make = make
    year = str(year)
    
    ModelPageUrl = url + "cars/" + year + "/" + make

    NewResponse = requests.get(ModelPageUrl)
    bsModels = BeautifulSoup(NewResponse.text,'html.parser')
    LinkList = bsModels.findAll('a')
    
    ModelLowIndex = [x for x, y in enumerate(bsModels.findAll('a')) if 'Cars' in y][0]
    ModelHighIndex = [x for x, y in enumerate(bsModels.findAll('a')) if 'Privacy Policy' in y][0]

    model = LinkList[ModelLowIndex+2]['href']
    SpecSheetUrl = url + model[1:]
    print('success')

    



    
    
    






