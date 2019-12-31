from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
# create firestore client
db = firestore.Client()

data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection(u'cities').document(u'LA').set(data)


data = {
    u'name': u'san francisco',
    u'state': u'SF',
    u'country': u'USA'
}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection(u'cities').document(u'SF').set(data)

# merge=True then, overwritten and add field when document exist.
#  merge=True : SF => {'state': 'SF', 'capital': False, 'name': 'san francisco', 'country': 'USA'}
#  merge=False: SF => {'capital': False}
city_ref = db.collection(u'cities').document(u'SF')
city_ref.set({
    u'capital': False
}, merge=True)



#read data from collection
# but data exist local.
users_ref = db.collection(u'cities')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))