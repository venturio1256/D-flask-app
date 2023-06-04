import os
from pyairtable import Base, Table
import json
api_key = 'patNDOiJNRiFMwDAL.e0de4d749d28e381f266e45fbd9def6f3f4df0e0f52e13e138db60935a785397'
base_id = 'appSaOc4eWkXFfsY1'
base = Base(api_key, base_id)
print('--------------------------------------------------------------------------------------')
baseAll = base.all('Users')
print (baseAll)
for json_data in baseAll:
    print (json_data['id'])

print('--------------------------------------------------------------------------------------')
    
for page in base.iterate('Users'):
    print('Base.iterate', page)
    for record in page:
        print('Record ', record)    
    
print('--------------------------------------------------------------------------------------')

tableUsers = Table(api_key, base_id, 'Users')

print('---------------------Table Users-----------------------------------')

for page in tableUsers.iterate():
    print('Page ' , page)
    for record in page:
        print('Record ', record)
        
tableChores = Table(api_key, base_id, 'Chores')

print('-----------------Table Chores--------------------------------------')

for page in tableChores.iterate():
    print('Page ' , page)
    for record in page:
        print('Record ', record)
        
        
print('-----------------Table History -------------------------------')

tableHistory = Table(api_key, base_id, 'History')

print('--------------Send Chores to Airtable ----------------------------------')
        
#Insert / Create a new history record
tableHistory.create({'name': ['recfzC9hsuLqbHlj0'], 'username': ['rec5gaI0ovQ3Z4ssd']})


for page in tableHistory.iterate():
    print('Page ' , page)
    for record in page:
        print('Record ', record)