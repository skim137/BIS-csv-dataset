## -----------------------------------------------------------
# Desc: Create an ETL pipeline using SQLite for BIS effective fx rate indices monthly data
# 
# Data source: 'BISWEB_EERDATAFLOW_csv_col.csv' / 'Effective exchange rate indices (monthly)'
# https://www.bis.org/statistics/full_data_sets.htm
## -----------------------------------------------------------

import csv
import os
import sqlite3

#Create a new sqlite3 db. If exists, connect to it
dbname = 'bis_stat.sqlite3'
dbpath = os.path.join(os.path.dirname(__file__), dbname)

conn = sqlite3.connect(dbpath)
c = conn.cursor()


#Custom functions
#chk_table(): Check if a table exists
def chk_table(table):
    t = (table, )
    c.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?", t)
    if c.fetchone() == t:
        return 1
    elif c.fetchone() == None:
        return 0


#SQL statements
create_bisfx_data = '''CREATE TABLE bisfx_data (date TEXT,
                    attrib TEXT,
                    value TEXT,
                    CONSTRAINT PK_bisfx PRIMARY KEY (date, attrib)
                    )
'''

insert_bisfx_data = 'INSERT OR IGNORE INTO bisfx_data VALUES (?, ?, ?)'


#Read BIS file and create a nested list (row by row)
filename = 'BISWEB_EERDATAFLOW_csv_col.csv'
filepath = os.path.join(os.path.dirname(__file__), filename)

series = []

with open(filepath) as csv_file:
    csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter=',')
    for row in csv_reader:
        series.append(row)

#Create a list with dates only
dates = series[0][9:len(series[0])]

#Create a nested list for row by row attributes
attrib = [series[i][0:9] for i in range(1, len(series))]

#Create a list with dates duplicated by the # of attribute rows
cols = dates * len(attrib)

#Create a nested list with selected values from attribute list duplicated by the # of dates
rows = []

for i in range(0, len(attrib)):
    rows = rows + [attrib[i][8]] * len(dates)

#Read values row by row and chain them all into a single list
values = []

for i in range(1, len(attrib) + 1):
    values = values + series[i][9:len(series[0])] 

#Zip three lists and remove blank values
unpivot = list(zip(cols, rows, values))

records = [(i[0], i[1], i[2]) if i[2] != '' else None for i in unpivot]

records = list(filter(lambda x: x is not None, records))


#Create TABLE bisfx_data if not exist
if chk_table('bisfx_data') == 0:

    c.execute(create_bisfx_data)

    conn.commit()

elif chk_table('bisfx_data') == 1:

    pass


#Insert records
c.executemany(insert_bisfx_data, records)

conn.commit()

conn.close()