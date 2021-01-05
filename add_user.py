import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import argparse
from typing import Optional
from firebase_admin import auth
from firebase_admin.auth import UserRecord
from initialise_firebase_admin import app
import requests
import os

print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))



# initializations 
# cred = credentials.Certificate('myprojectwithfirebase-8a1e4-firebase-adminsdk-bcezw-742d66b7bc.json')
# firebase_admin.initialize_app(cred)


db = firestore.client()
#adding second data
a = []
n = int(input("enter number of name : "))
for i in range(n):
	a.append(str(input("enter name : ")))
	print("list of name")
	for name in a:
		data = {
			'description':name
		}

	def save(collection_id, document_id, data):
		db.collection('collection_id').document('document_id').set(data)

	save(
		collection_id = "1",
		document_id = "1",
		data = data
	)

# doc_ref = db.collection('employee').document('data')
# doc_ref.set({

#     'name':'John',
#     'lname':'Doe',
#     'email':'john@gmail.com',
#     'age':24
# })

# # Udpdate:
# col_ref = db.collection('employee') # col_ref is CollectionReference
# results = col_ref.where('name', '==', 'john').get() # one way to query
# results = col_ref.order_by('name',direction='DESCENDING').limit(5).get() # another way - get the last document by date
# for item in results:
#     print(item.to_dict())
#     print(item.id)
# doc = col_ref.document(item.id) # doc is DocumentReference
# field_updates = {"name": "Updated description"}
# doc.update(field_updates)



#Reading the data
# emp_ref = db.collection('employee')
# docs = emp_ref.stream()

# for doc in docs:
#     print('{} => {} '.format(doc.id, doc.to_dict()))
