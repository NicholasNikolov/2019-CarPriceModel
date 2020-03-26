# CarPriceModel
 
This is a three part project which includes web-scraping, data-cleaning, and statistical modeling. The data in its raw form appears as .csv files with naming convention: 20XXData where XX is used to determine the year of the car model. The data will be combined in a full dataset for data analysis.

1. Web Scraper [Complete - 03 SEP 2019]
- Scrapes the carspecs site (carspecs.us) for car data.
- As of 03 SEP 2019, the web scraper functions as expected.
- Some improvements might be made in the future to make the code more resilient to changes on the website.
- Inputs data into one of 75 categories
- NOTE: Use CarDataCrawler_v2.py if you want to test out the web scraper.
- CarDataCrawler.py is depcrecated and the Web_Scraper.ipynb jupyter notebook was used for testing the code.

2. Data Cleaner [Complete - 29 SEP 2019]
- Missing price data was manually filled through online research. The data cleaning code, by default, removes all entries with this     
  missing variable because it is intended as the response variable.
- Cleaned up leftover HTML code and string values and converted to string where applicable.
- Most missing data filled where viable. Numerous approaches were pursued depending on the situation.
     + Where a logical collinear relation existed (and where there were not a large number of missing values) a 
       simple regression model was used to fill the missing values.
     + Where a qualitative identifier existed (e.g. Gas, electric, hybrid engine), missing values were filled by the average of their
       respective groups (e.g. missing MPG's of hybrids were filled with the mean of all hybrids in the dataset).
     + Where no logical collinear relation existed, and there was not a known qualitative identifier, the missing values were filled
       using the mean of the column.
 - There may be some additional work necessary to extract a bit more data out of the dataset. Namely, there remain some qualitative
   variables that have not been extracted (E.g., transmission and tire size). These may be useful but would require me to extract
   relevant text. In the case of transmission, the process would be more complex than simply using get_dummies because there are some
   entries where speed is capitalized and some where it is not. There is already a wide variety of values which might become useless if
   they approach N ~= 1200.
 - The electric vehicles cannot have values for some columns. For example, RPM and fuel tank capacity are not relevant.
 - Output of this step is CleanData.csv
 - Input of this step is FullData.csv

3. Statistical Modeling [Complete - 29 NOV]
- Unfortunately neither supervised nor unsupervised models really seemed fitting.
- My goal was to optimize on the basis of a few characteristics (namely MPG, 0-60mph, torque, and price). I weighted price and mpg  
  higher than other stuff. 
- The approach wasn't the most statistically sound but it still lends some insight into the data. Overall it works for comparisons 
  between cars. E.g., when comparing the Ford Fusion Hybrid and Toyota Camry Hybrid, the model accurately gave a better score to the 
  Camry which had superior performance and fuel economy.
- If I think of a superior approach I'll return to this project. Otherwise, ScoredEntries.csv now holds the sorted and scored car 
  models.
  
4. Statistical Updates/Review of Stage 3 [Not Started]
- Initiating a more specific and accurate approach to the statistical modeling process -- I was more excited about my first web  
  scraper and formatting data (originally was thinking to upload to Kaggle. I might still do that!)
- Researching a more statistically sound method of determining optimal car purchases or developing a script based on a mathematical
  model. Ultimately this project was the largest personal data-related project I've undertaken. I still need to take a more mature 
  approach with the modeling. This will require more research (I got excited and was jumping from project to project around when this  
  finally came to a close).



Project Progress: Reopened [Originally Complete 29 NOV - Scheduled to reopen when my Coronavirus script is done collecting data]

Data Source: https://www.carspecs.us
 Note: Above data source is not a formatted source like other projects. The data was taken using a web scraper.

Question/Concerns?

Email me at Nikolovnickv@gmail.com

Thank you!
