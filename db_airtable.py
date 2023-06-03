import os
from pyairtable import Base, Table
import json
api_key = 'patNDOiJNRiFMwDAL.e0de4d749d28e381f266e45fbd9def6f3f4df0e0f52e13e138db60935a785397'
base_id = 'appSaOc4eWkXFfsY1'
base = Base(api_key, base_id)
baseAll = base.all('Users')
print (baseAll)
for json_data in baseAll:
    print (json_data['id'])
    
for records in base.iterate('Users'):
    print('Base.iterate', records)
    
table = Table(api_key, base_id, 'Users')

#tableAll = table.all()
#print ('Table.all ', tableAll)
for page in table.iterate():
    print('Page ' , page)
    for record in page:
        print('Record ', record)