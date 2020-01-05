from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
# create firestore client
db = firestore.Client()

# this pgm run by python 3
# if python 2 uses then u'name':u'city name'
data = {
    'name': 'Los Angeles',
    'state': 'CA',
    'country': 'USA'
}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection('cities').document('LA').set(data)


data = {
    'name': 'san francisco',
    'state': 'SF',
    'country': 'USA'
}

# Add a new doc in collection 'cities' with ID 'SF'
db.collection('cities').document('SF').set(data)

# Add a new doc in collection 'cities' with auto ID
# nest data
const city_add = db.collection('cities').doc()
await city_add.set({
    data:{
        name : 'oregon',
        state : 'OR',
        country : 'USA'
    }
    data_seq : 1,
    create: firebase.firestore.FieldValue.serverTimestamp(),
    update: firebase.firestore.FieldValue.serverTimestamp(),
})

# merge=True then, overwritten and add field when document exist.
#  merge=True : SF => {'state': 'SF', 'capital': False, 'name': 'san francisco', 'country': 'USA'}
#  merge=False: SF => {'capital': False}
city_ref = db.collection('cities').document('SF')
city_ref.set({
    'capital': False
}, merge=True)



#read data from collection
# but data exist local.
users_ref = db.collection('cities')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))