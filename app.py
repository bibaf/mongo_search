#!/usr/bin/env python3

from flask import Flask, request, render_template, send_file,json
from pymongo import MongoClient
import requests
from bson.objectid import ObjectId

def newEncoder(o):
    if type(o) == ObjectId:
        return str(o)
    return o.__str__

app=Flask(__name__,template_folder='templates')

# Connect to MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['GHSA']
collection = db['advisories']  # Replace 'mycollection' with your collection name







@app.route('/', methods=['GET'])
def do_list():
    # Define a list of options for the drop-down list
    options = ['GitHub Actions', 'Go', 'Hex', 'Maven','NuGet', 'Packagist','Pub','PyPI', 'RubyGems', 'crates.io', 'npm']
    limit=100;
    query={};
    if request.args.get("summary"):
        query["summary"]={"$regex": request.args.get("summary"), "$options" :'gi'}
        summary=request.args.get("summary")

    if request.args.get("limit",type=int) and request.args.get("limit",type=int)>0:
        limit=request.args.get("limit",type=int)
    if request.args.get("ecosystem") and request.args.get("ecosystem") in options:
        selected_option = request.args.get('ecosystem')
        query["affected.package.ecosystem"]=selected_option

    results = collection.find(query, {'id':1,'affected':1, 'aliases': 1, 'published': 1, 'details': 1, 'summary': 1,'todo':1,'done':1}).sort("published",-1).limit(limit)
    return render_template('index.html', results=results,options=options)

@app.route('/', methods=['POST'])
def do_toggle():
    toggle=request.args.get("toggle")
    response = app.response_class()
    id=request.args.get("id")
    current = collection.find_one(ObjectId(id))
    if toggle == 'todo':
        curval=current.get('todo')
        newval=not curval
        newvalues = {"$set":{'todo': newval }}
    else:
        curval=current.get('done')
        newval=not curval
        newvalues = {"$set":{'done':newval}}


    data=collection.update_one({'_id': ObjectId(id)}, newvalues)
    response = app.response_class(
        response=json.dumps({"status": "success",'data': data.matched_count}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)