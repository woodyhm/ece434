import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#might need to make document link dynamic
status_ref = db.collection(u'CoffeeMakers').document(u'FfOEJgMxR9kzuus67ydD')

try: 
    status = status_ref.get()
    print(format(status.to_dict()[u'isBrewing']))
    
except google.cloud.exception.NotFound:
    print(u'No data found')

