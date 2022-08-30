import snowflake.connector
import sys
import pandas as pd

#setting up snowflake connection via external browser login
con = snowflake.connector.connect(
    user="usernae ex. email", #You can get it by executing in UI: desc user <username>;
    account="ex. am464376.ap-southeast-2", #Add all of the account-name between https:// and snowflakecomputing.com   ex. am62976.ap-southeast-2
    authenticator="externalbrowser", 
    )
    
"""
#for ligin using id & password
conn = snowflake.connector.connect(
                user=USER,
                password=PASSWORD,
                account=ACCOUNT,
                warehouse=WAREHOUSE,
                database=DATABASE,
                schema=SCHEMA
                )
                
                """    

cur = con.cursor()
