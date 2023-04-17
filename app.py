from flask import Flask, request, render_template, send_file
from pymongo import MongoClient
import json
from markupsafe import Markup


app=Flask(__name__,template_folder='template')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['GHSA']  # Replace 'mydatabase' with your database name
collection = db['advisories']  # Replace 'mycollection' with your collection name



@app.route('/', methods=['GET', 'POST'])
def drop_list():
    # Define a list of options for the drop-down list
    options = ['GitHub Actions', 'Go', 'Hex', 'Maven','NuGet', 'Packagist','Pub','PyPI', 'RubyGems', 'crates.io', 'npm']

    if request.method == 'POST':
        # Get the selected option from the form submission
        selected_option = request.form.get('option')
        results = collection.find({"affected.package.ecosystem": selected_option}, {'aliases': 1, 'published': 1, 'details': 1, 'summary': 1})
        results_list = list(results)
        results_str = str(results_list)
        replace = results_str.replace('\n', '<br>').replace("_id", "\n_id").replace("\\n", "\n").replace("]", "").replace("-", "").replace("[", "").replace(",", "\n").replace("{", "").replace("}", "").replace("'", "")
        with open("/app/results.txt") as file:
            file_content = file.read()
            file_content = file_content.replace('\n', '<br>')
        return render_template('results.html', file_content=file_content)
        #html_markup = Markup(replace)
        #with open("results.txt" ,"w") as file:
        #    file.write(replace)
        #    file.close()
        
        #return render_template_string(replace)
        #return render_template('results.html', file_content=replace)






        #return render_template('results.html', html=replace)


    # Render the template with the drop-down list
    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)

    




# db.advisories.find({"affected.package.ecosystem": "Go"}, {'published': 1, 'aliases': 1, 'summary': 1, 'details:': 1})


#array = list(collection.find({"affected.package.ecosystem": "Go"}, {'published': 1, 'aliases': 1, 'summary': 1, 'details:': 1}))

#print(array)