# BIS-csv-dataset
Create an ETL pipeline for csv datasets from BIS (Bank for International Settlements) using Python and SQLite.

## Background
BIS provides their financial and international banking datasets (mostly time series) via the [BIS Statistics Explorer](https://stats.bis.org/statx/toc/LBS.html) and [BIS Statistics Warehouse](https://stats.bis.org/#ppq=CBS_C_AND_OTH_EXP_UR;pv=11~10,5,6~0,0,0~name) as well as the [SDMX web servies API](https://www.bis.org/statistics/sdmx_techspec.htm). If you are interested in working with their flat files, they are available here 
https://www.bis.org/statistics/full_data_sets.htm, which are updated by BIS on a regular basis. However, one major issue with their flat files is that the data is already pivoted (aka. not tidy, see Exhibit 1 below). 

This ETL pipeline project contains Python scripts that process BIS CSV files and insert the unpivoted data into a persistent SQLite database file. You can then access the SQLite file to transform the data the way you want it for your own purposes (e.g. connecting to a datalake, performing data analysis using Pandas, R, and etc.). Therefore, this solution is effective and scalable. 

Using SQLiteStudio is highly recommended. This excellent open source interface program can be [downloaded here](https://sqlitestudio.pl/). 


As of today, this project contains ETL pipelines for the following datasets:
* **Effective exchange rate indices (monthly)** => Nominal and real FX indices (broad, narrow) of more than 30 countries going back to 1960
* **Policy rates (monthly)** => Central bank benchmark policy rates of more than 30 central banks going back to 1960
*  More coming up...


## What's in this repository
* Python ETL scripts that parse and load BIS data into SQLite
* BIS CSV files downloaded and unzipped
* SQL script that creates a mapping table called 'country'
* SQL script that inserts mapping data into the 'country' table
* A set of SQL scripts that create Views for further data transformation
* R script using Views for data analysis (just a template)


## Instructions
1. Save raw CSV files (e.g. "BISWEB_EERDATAFLOW_csv_col.csv") in the same folder location where the Python ETL scripts (e.g. "bixfx_etl.py") are saved.
2. Execute the Python ETL scripts 
3. Check the folder to see if an SQLite database file called "bis_stat.sqlite3" is created. 
4. In the database file, you should see tables such as "bisfx_data" (see Exhibit 2 below) 
5. Execute the following SQL scripts in your SQLiteStudio (optional):
    - "CREATE TABLE country.sql"
    - "INSERT INTO country.sql"
    - "CREATE VIEW.sql" files
6. Execute R scripts in your RGui or RStudio (optional).
7. When BIS uploads updated CSV files, repeat the process.


## Exhibit
Exhibit 1

![how BIS raw file looks](https://github.com/skim137/BIS-csv-dataset/blob/38d5fd4ccf2b7749646c93857714d318c2e0b6a9/Exhibit1.JPG)
