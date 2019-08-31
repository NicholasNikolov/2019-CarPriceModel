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
    variables.insert(0,'Make')
    variables.insert(1,'Model')
    variables.insert(2,'Year')
    CarData = pd.DataFrame(columns = variables)
    print('success')
    return(CarData)
    
    
    
# This method uses pre-determined indices to extract all makes from the homepage.
def MakeList():
    link = 'https://www.carspecs.us/'
    response = requests.get(link)
    makes = []
    # Current list index is 24 to 91 as of Aug 29, 2019
    for i in range(24,91):
        makes.append(BeautifulSoup(response.text).findAll('a')[i]
                                        .get_text())
    return(makes)
    
    
    


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
    
    model = []
    SpecSheetUrl = []
    for i in range(ModelLowIndex,ModelHighIndex-2):
        model.append(LinkList[i+2]['href'])

    for j in range(len(model)):
        specUrl = url + model[j][1:]
        SpecSheetUrl.append(specUrl)
    return(SpecSheetUrl)

# Method to get all of the models in the particular make. Works similar to URLSeeker
def ModelList(make,year):
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
    
    ModelList = []
    for i in range(ModelLowIndex,ModelHighIndex-2):
        ModelList.append(LinkList[i+2].get_text())
    
    return(ModelList)
    

# The datafilling method that will actually get the necessary data in
def DataFiller(make,model,year):
    make = make
    model = model
    year = str(year)
    
    data = []
    for i in range(72):
        data.append(BeautifulSoup(NewResponse.text,'html.parser')
        .findAll(True,{'class':'pure-u-1 pure-u-md-1-2'})[i]
        .get_text().strip()
        .split('\r\n')[1])
        
    data.insert(0,make)
    data.insert(1,model)
    data.insert(2,year)
    
    return(data)


def MainMethod(year):
    year = year
    makes = MakeList()
    data = DataFrameBuilder()

    for make in makes:
        UrlList = UrlSeeker(make,year)
        ModelList = ModelList(make,year)
        
        for model in len(ModelList):
            obsv = DataFiller(make,model,year)
            data.append(obsv)
            
    return(data)
    
MainMethod(2019)
            
            

            
            


