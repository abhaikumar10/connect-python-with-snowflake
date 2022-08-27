import snowflake.connector
import sys
import pandas as pd

#setting up snowflake connection
con = snowflake.connector.connect(
    user="usernae ex. email", #You can get it by executing in UI: desc user <username>;
    account="ex. am464376.ap-southeast-2", #Add all of the account-name between https:// and snowflakecomputing.com   ex. am62976.ap-southeast-2
    authenticator="externalbrowser", 
    )
cur = con.cursor()

#executing sql query
f = open("py\code.sql",'r')                       #reading Sql from file, alternativelly use below inline code.     
sql=f.read()                                      #sql= "select current_date"
cur.execute(sql)
names = [ x[0] for x in cur.description]          #pulling column names from discription of Snowflake output.
data=cur.fetchall()                               # .fetchone(), .fetchmany(5)

#writing data to external file as csv via pandas.
dataout=pd.DataFrame(data,columns=names)         #converting output to pd df adding column names as well.
dataout.to_csv('py\data.csv',index=0)