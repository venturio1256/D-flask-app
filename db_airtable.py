import os
from pyairtable import Base, Table
import json
api_key = 'patNDOiJNRiFMwDAL.e0de4d749d28e381f266e45fbd9def6f3f4df0e0f52e13e138db60935a785397'
base_id = 'appSaOc4eWkXFfsY1'
base = Base(api_key, base_id)
baseAll = base.all('Users')
print (baseAll)
print('--------------------------------------------------------------------------------------')
for json_data in baseAll:
    print (json_data['id'])

print('--------------------------------------------------------------------------------------')
    
for page in base.iterate('Users'):
    print('Base.iterate', page)
    for record in page:
        print('Record ', record)    
    
print('--------------------------------------------------------------------------------------')

tableUsers = Table(api_key, base_id, 'Users')

#tableAll = table.all()
#print ('Table.all ', tableAll)
print('---------------------Table Users-----------------------------------')

for page in tableUsers.iterate():
    print('Page ' , page)
    for record in page:
        print('Record ', record)
        
tableChores = Table(api_key, base_id, 'Chores')

#tableAll = table.all()
#print ('Table.all ', tableAll)
print('--------------------------------------------------------------------------------------')

for page in tableChores.iterate():
    print('Page ' , page)
    for record in page:
        print('Record ', record)
        
print('--------------------------------------------------------------------------------------')

tableHistory = Table(api_key, base_id, 'History')
for page in tableHistory.iterate():
    print('Page ' , page)
    for record in page:
        print('Record ', record)
        

print('--------------Real Stuff----------------------------------')
        
# Insert / Create a new history record
#tableHistory.create({'name': ['reck00Wy0hYs39Mzu'], 'User': ['rec5gaI0ovQ3Z4ssd']})
