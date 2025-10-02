#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

def read_people():
    people = []
    csv_path = os.path.join(os.path.dirname(__file__), 'people.csv')
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Clean up keys and values (strip whitespace)
            person = {k.strip(): (v.strip() if v else '') for k, v in row.items()}
            people.append(person)
    return people

@app.route('/group')
def group():
    people = read_people()
    return render_template('group.html', people=people)

# Optional: redirect root to group page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




