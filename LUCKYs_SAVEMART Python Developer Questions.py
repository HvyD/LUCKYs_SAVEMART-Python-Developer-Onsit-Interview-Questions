#!/usr/bin/env python
# coding: utf-8

# # LUCKY's/SAVEMART Python Developer Questions
# 
# 
# 
# 
# 

# In[ ]:


#initial table
DataBase:
+---------------+          
|    A  |   B   |      
+---------------+
| Foo1  | Bar1  | 
| Foo2  | Bar2  |  
| Foo3  | Bar3  | 
| Foo4  | Bar4  |  
+---------------+

#After clearification
Customers:
+------------+------------+
| first_name | last_name  | 
+------------+------------+
| John       | Smith      | 
| Ava        | Muffinson  |  
| Cailin     | Ninson     | 
| Mike       | Peterson   |   
+------------+------------+


# #### 1. Take a SQL database and pull the data into JSON format

# In[ ]:


import json
import sqlites

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
query = "SELECT * FROM Customers"
result = cursor.execute(query)

sqlData = []

for row in result:
    for key in cursor.description:
        sqlData.append({key[0]: value for value in row})
print(json.dumps({'sqlData': sqlData}))

#OUTPUT should look like:
[{"firstname":"John","lastname":"Smith"}, {"firstname":"Ava","lastname":"Muffinson"}, {"firstname":"Cailin","lastname":"Ninson"}, {"firstname":"Mike","lastname":"Peterson"}]


# #### 2. Parse form APi to JSON

# In[ ]:


import requests

results  = requests.get(url='https://<WebsiteURLhere>?print=pretty')
print(results.json())


# #### 3. Transfer a .CSV to JSON

# In[ ]:


import csv
import json

csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("FirstName","LastName")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)


# OutPut Should look like:
[{"firstname":"John","lastname":"Smith"}, {"firstname":"Ava","lastname":"Muffinson"}, {"firstname":"Cailin","lastname":"Ninson"}, {"firstname":"Mike","lastname":"Peterson"}]

