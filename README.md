# CarPriceModel
 
This is a three part project which includes web-scraping, data-cleaning, and statistical modeling.

1. Web Scraper [Complete]
- Scrapes the carspecs site (carspecs.us) for car data.
- As of 03 SEP 2019, the web scraper functions as expected.
- Some improvements might be made in the future to make the code more resilient to changes on the website.
- Inputs data into one of 75 categories
- NOTE: Use CarDataCrawler_v2.py if you want to test out the web scraper.

2. Data Cleaner [Not Started]
- Some data from the web-scraper is necessary but missing. I need to determine a method to pull price data for missing values. This might be easiest done manually
- There are entries that have a lot of spaces, unnecessarily
- ALL entries are strings including horspower and torque. This will need to be adjusted.
- A lot of missing data that needs to be cleaned.

3. Statistical Modeling [Not Started]
- An optimal model will be determined to fit the data. 
- There are two modeling approaches that will be considered/followed. One will attempt to fit to all data while the other will fit to more average car models (I.e., do not fit to $1M Ferraris).




Project Progress: In-Progress

Data Source: https://www.carspecs.us
 Note: Above data source is not a formatted source like other projects. The data was taken using a web scraper.
