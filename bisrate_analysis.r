#############################################################
## Desc: Analyze central bank policy rate history
#############################################################

##############################
# 0 - Load libraries
##############################
library(DBI)
library(reshape2)
library(xts)

##############################
# 1 - Custom functions
##############################

#Convert data frame to xts time series
df_xts <- function(df){

    dates <- as.Date(df[ , 1])
    data <- df[ , c(2:ncol(df))]

    xts <- xts(x=data, order.by=dates) 

    return(xts)
}

##############################
# 2 - Start my code
##############################

#Pull v_bisrate from SQLite and create a dataframe object
dbfile <- "" # <--- File directory of your bis_stat db file is saved
mydb <- dbConnect(RSQLite::SQLite(), dbfile)
sqlstr <- "SELECT * FROM v_bisrate"
data.df <- dbGetQuery(mydb, sqlstr)

#Pivot data.df based on date and country
pvt.df <- dcast(data.df, data.df[, 1]~data.df[, 2])
colnames(pvt.df)[1] <- "date"
pvt.df$date <- as.Date(pvt.df$date)

#Convert pvt.df to xts
pvt.xts <- df_xts(pvt.df)