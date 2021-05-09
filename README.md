# BIS-csv-dataset
Create an ETL pipeline for csv datasets from BIS (Bank for International Settlements) using Python and SQLite.

## Background
BIS provides their financial and international banking datasets (mostly time series) via the [BIS Statistics Explorer](https://stats.bis.org/statx/toc/LBS.html) and [BIS Statistics Warehouse](https://stats.bis.org/#ppq=CBS_C_AND_OTH_EXP_UR;pv=11~10,5,6~0,0,0~name) as well as their
[SDMX web servies API](https://www.bis.org/statistics/sdmx_techspec.htm). If you are interested in working with their flat files, they are available here 
https://www.bis.org/statistics/full_data_sets.htm, which are updated by BIS on a regular basis. However, one major issue with their flat files is that the data is already pivoted (aka. not tidy). This ETL pipeline project contains Python scripts that process BIS CSV files and insert the unpivoted data into an SQLite database file. You can then access the SQLite file to transform the data the way you want it for your own purposes (e.g. connecting to a datalake, performing data analysis using Pandas, R, and etc.). 

As of today, this project contains ETL pipelines available for the following datasets:
* **Effective exchange rate indices (monthly)** => Nominal and real FX indices (broad, narrow) of more than 30 countries going back to 1960
* **Policy rates (monthly)** => Central bank benchmark policy rates of more than 30 central banks going back to 1960
*  More coming up...    

## What's in this repository
* Python scripts for parsing and loading BIS into SQLite (required)
* Raw data files downloaded and unzipped (required)
* SQL script that creates 'country' mapping table (optional)
* SQL scripts that creates Views (optional)

## Instructions
