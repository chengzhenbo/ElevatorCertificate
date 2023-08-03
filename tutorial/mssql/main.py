import urllib
from sqlalchemy import create_engine

driver = 'ODBC Driver 17 for SQL Server'
server = 'localhost'
username = 'sa'
password = 'yourStrong(!)Password'

odbc_connect = urllib.parse.quote_plus(
    'DRIVER={%s};SERVER=%s;UID=%s;PWD=%s' % (driver, server, username, password))
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % odbc_connect)

query1 = "Select [销售组织ID],[合同子号] from [Integration].[dbo].[hetonginfo] where [生效日] between '2020-01-01' and '2020-01-31'"
query2 = "Select * from [10.10.161.121].[APS].[dbo].[合格证参数中间表] where [合同子号] ='XZ22160745' and [参数名]='项目名称'"

with engine.connect() as conn:
    rs = conn.execute(query1)
    for row in rs:
        print(row['销售组织ID'])

