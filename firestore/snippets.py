from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
# windows powershell : $env:GCLOUD_PROJECT="project-name"

# create firestore client
db = firestore.Client()

#Add data 1
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

#Add data 2
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})

#read data from collection
# but data exist local.
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))