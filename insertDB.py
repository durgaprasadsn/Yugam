from firebase_admin import db
from firebase_admin import credentials
import firebase_admin
import csv

def insert_to_firebase(user, hash_map, index):
    if (index == 0):
        databaseURL = 'https://rotasia-tech-default-rtdb.firebaseio.com/'
        cred_obj = credentials.Certificate('./rotasia-tech-firebase-adminsdk-6kzjs-e8b851a764.json')
        default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': databaseURL})
        ref_users_date = db.reference("/date")
        date = {'18-05-2024': 'Day1', '19-05-2024': 'Day2'}
        ref_users_date.update(date)

        ref_users_food = db.reference("/food")
        ref_users_food.update({"food_type": "Breakfast"})
    print(user)
    ref_users = db.reference("/delegates")
    ref_users.update(user)
    ref_users_map = db.reference("/map")
    ref_users_map.update(hash_map)
    

i = 0

with open('Tech Sync.csv', mode ='r') as file:    
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        # print(lines)
        create_val = {lines['Booking Id']: {'tshirt': lines['T Shirt Size'], 'name': lines['Name'], 'logistics': {'IDCard': 'No', 'GenericKit': 'No', 'T-Shirt (' + lines['T Shirt Size'] + ')': 'No'}, 'Day1': {'Checkedin': 'No', 'Breakfast': 'No', 'Lunch': 'No', 'HighTea': 'No', 'Dinner': 'No'}, 'Day2': {'Checkedin': 'No', 'Breakfast': 'No', 'Lunch': 'No', 'HighTea': 'No', 'Dinner': 'No'}}}
        hash_map = {lines['Registeration ID']: lines['Booking Id']}
        print(create_val)
        insert_to_firebase(create_val, hash_map, i)
        # map_hash_id(hash_map, i)
        i += 1