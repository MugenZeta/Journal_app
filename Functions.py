from flask import Flask, render_template, request, redirect, url_for
import datetime
import pyrebase

import urllib3

app = Flask(__name__)


firebaseConfig = {
  'apiKey': "AIzaSyAlcU9CKgygppQIthO3ifpIClmunXg0n6Q",
  'authDomain': "capstone-project-344519.firebaseapp.com",
  'databaseURL': "https://capstone-project-344519-default-rtdb.firebaseio.com",
  'projectId': "capstone-project-344519",
  'storageBucket': "capstone-project-344519.appspot.com",
  'messagingSenderId': "359433745060",
  'appId': "1:359433745060:web:39b8741dc1dc219a782c31",
  'measurementId': "G-3N5GEQNJND"
}

# initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
# Firebase Auth
auth = firebase.auth()

# FireBase Database
db = firebase.database()

#date of entry
entry_date = datetime.date.today()


