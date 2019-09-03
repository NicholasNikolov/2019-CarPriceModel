# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:26:05 2019

@author: asus
"""

from urllib.request import Request, urlopen
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
import winsound


# This method creates a 2000x72 dataframe that will be filled with data
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
    variables.insert(0,'Price')
    variables.insert(1,'Make')
    variables.insert(2,'Model')
    variables.insert(3,'Year')
    CarData = pd.DataFrame(columns = variables,index=range(2000))

    return(CarData)
    
# This method uses pre-determined indices to extract all makes from the homepage.
def MakeList():
    link = 'https://www.carspecs.us/'
    response = requests.get(link)
    makes = []
    # Current list index is 24 to 91 as of Aug 29, 2019
    for i in range(24,91):
        make = BeautifulSoup(response.text,'html.parser').findAll('a')[i].get_text()
        makes.append(make)
    return(makes)
    
# Method to get all of the models in the particular make. Works similar to URLSeeker
def ModelList(make,year):
    url = 'https://www.carspecs.us/'
    #response = requests.get(url)
    
    # The beautiful soup result of parsing the main page. Will search for links to pursue
    #bsMain = BeautifulSoup(response.text,"html.parser")
    make = make
    make = make.replace(" ","-")
    year = str(year)
    
    ModelPageUrl = url + "cars/" + year + "/" + make.lower()
    NewResponse = requests.get(ModelPageUrl)
    bsModels = BeautifulSoup(NewResponse.text,'html.parser')
    LinkList = bsModels.findAll('a')

    # Indices are determined from my observation that 'Cars' precedes the make name which precedes all model links
    # This is followed by Privacy policy for all observed makes
    ModelLowIndex = [x for x, y in enumerate(LinkList) if 'Cars' in y][0]
    ModelHighIndex = [x for x, y in enumerate(bsModels.findAll('a')) if 'Privacy Policy' in y][0]
    
    # Appends the models to the list within the prescribed indices
    ModelList = []
    for i in range(ModelLowIndex,ModelHighIndex-2):
        ModelList.append(LinkList[i+2].get_text())
    
    # Confirming that there are models. May be problematic if no model release for some years
    if len(ModelList)>0:
        return(ModelList)
        
# This method returns a list with all URL's for the models on the make page
def UrlSeeker(make,year):
    # Create reference to main webpage that will be used to seek out various car makes and models
    url = 'https://www.carspecs.us/'
    #response = requests.get(url)
    
    # The beautiful soup result of parsing the main page. Will search for links to pursue
    # bsMain = BeautifulSoup(response.text,"html.parser")
    make = make
    year = str(year)
    
    make = make.replace(" ","-")
    
    ModelPageUrl = url + "cars/" + year + "/" + make.lower()

    NewResponse = requests.get(ModelPageUrl)
    bsModels = BeautifulSoup(NewResponse.text,'html.parser')
    LinkList = bsModels.findAll('a')
    
    print("PAGE URL: ",ModelPageUrl)
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
    
    
    

    
df = DataFrameBuilder()
dfColumns = df.columns
makes = MakeList()

year = 2019
row = 0
for make in makes:
    urls = UrlSeeker(make,year)
    models = ModelList(make,year)
    time.sleep(10)
    
    # Using numerical indexing because urls and models should be the same length
    if(models):
        for i in range(len(models)):
            url = urls[i]
            model = models[i]
            time.sleep(10)
            NewResponse = requests.get(url)
            
            # Yes, I'm sorry. It's hideous code. But it works
            price = BeautifulSoup(NewResponse.text,'html.parser').findAll(True,{'class':'main-car-details'})[0].get_text().strip().split('from ')[1].split('\r\n')[0]
            
            df.loc[df.index[row],'Price'] = price
            df.loc[df.index[row],'Make'] = make
            df.loc[df.index[row],'Model'] = model
            df.loc[df.index[row],'Year'] = year
            
            dataLength = len(BeautifulSoup(NewResponse.text,'html.parser').findAll(True,{'class':'pure-u-1 pure-u-md-1-2'}))
            
            #for j in range(dataLength-1):
            for j in range(dataLength-1):
                #print("Third Entry Item: ",df.loc[df.index[j-1],variable])
                try:
                    entry = BeautifulSoup(NewResponse.text,'html.parser').findAll(True,{'class':'pure-u-1 pure-u-md-1-2'})[j].get_text().strip().split('\r\n')[1]
                    variable = BeautifulSoup(NewResponse.text,'html.parser').findAll(True,{'class':'pure-u-1 pure-u-md-1-2'})[j].get_text().strip().split('\r\n')[0]

                except IndexError:
                    #"Index Error for mismatch count of pure-u-1 pure-u-md-1-2"
                    pass
                #print("Fourth Entry Item: ",df.loc[df.index[j-1],variable])

                print(j)
                print("Variable: ",variable," Entry: ", entry)
                print("Entry Type: ",type(entry))
                print("Make: ",make)
                print("Model: ",model)

                if variable in df.columns:
                    try:
                        # CarData.loc[CarData.index[5], 'Make'] = "TESTTEST"
                        df.loc[df.index[row],variable] = entry
                        #print("First Entry Item: ",df.loc[df.index[j],variable])
                        # print("!!!!!!!!!!!!!Entry!!!!!!!!!!!!!!!: ",df.loc[df.index[j],variable])
                        # df[variable].loc[j] = entry
                    
                    except TypeError:
                        print("Type Error Appeared")
                        #df[variable][j] = "Null"
                        pass
                #print("Second Entry Item: ",df.loc[df.index[j],variable])
                #print("Fourth Entry: ",df.loc[df.index[0],'Passenger Capacity'])
            row += 1
# =============================================================================
#                 else:
#                     print("ENTERED ELSE STATEMENT")
#                     df[variable][j] = "Null"
# =============================================================================
                        
                    

                        
df.to_csv("2019Data.csv")

duration = 10000  # milliseconds
freq = 550  # Hz
winsound.Beep(freq, duration)


