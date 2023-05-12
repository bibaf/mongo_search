#!/usr/bin/env python3

from flask import Flask, request, render_template, send_file
from pymongo import MongoClient
import requests

app=Flask(__name__,template_folder='template')

# Connect to MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['GHSA']
collection = db['advisories']  # Replace 'mycollection' with your collection name







@app.route('/', methods=['GET', 'POST'])
def drop_list():
    # Define a list of options for the drop-down list
    options = ['GitHub Actions', 'Go', 'Hex', 'Maven','NuGet', 'Packagist','Pub','PyPI', 'RubyGems', 'crates.io', 'npm']
    limit=100;

    if request.args.get("limit",type=int) and request.args.get("limit",type=int)>0:
        limit=request.args.get("limit",type=int)
    if request.args.get("option") and request.args.get("option") in options:
        selected_option = request.args.get('option')
        results = collection.find({"affected.package.ecosystem": selected_option}, {'id':1,'aliases': 1, 'published': 1, 'details': 1, 'summary': 1}).sort("published",-1).limit(limit)
        return render_template('search.html', results=results)

    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)