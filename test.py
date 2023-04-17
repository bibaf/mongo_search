from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import json
from markupsafe import Markup


app=Flask(__name__,template_folder='template')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['GHSA']  # Replace 'mydatabase' with your database name
collection = db['advisories']  # Replace 'mycollection' with your collection name



selected_option = request.form.get('option')
results = collection.find({"affected.package.ecosystem": "Go"}, {'aliases': 1, 'published': 1, 'details': 1, 'summary': 1})
results_list = list(results)
results_str = str(results_list)
replace = results_str.replace("\\n", "\n").replace("_id", "\n_id").replace(",", "\n").replace("{", "").replace("}", "").replace("'", "")
html_markup = Markup(replace)





with open("results.txt" ,"w") as file:
    file.write(html_markup)
    text = file.read()

def load_text():
    # Read text file content
    file_path = os.path.join(app.static_folder, '/app/result.txt')  # Update with your text file path
    with open(file_path, 'r') as file:
        text = file.read()