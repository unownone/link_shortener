import re
from flask import request,Flask, render_template,redirect,url_for,jsonify
from flask_pymongo import PyMongo
import string
import random
import secrets
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)


links = mongo.db.redirect

def get_random_url():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
    
@app.route('/', methods=['GET','POST'])
@app.route('/<url>',methods=['GET'])
def main(url=''):
    if request.method == 'GET' and url=='':
        return render_template('index.html',hide='hidden',url='')
    elif request.method == 'POST':
        data = request.form.get('link')
        ra = get_random_url()
        search = links.find_one({'link':data})
        if search is not None:
            return render_template('index.html',hide='',url=request.base_url+'/'+ra)
        else:
            search = links.find_one({'short':ra})
        while search is not None:
            ra = get_random_url()
            search = links.find_one({'short':ra})
        links.insert_one({'short':ra,'link':data})
        return render_template('index.html',hide='',url=request.base_url+''+ra)
    elif request.method == 'GET' and url!='':
        search = links.find_one({'short':url})
        if search is not None:
            if search['link'].startswith('http://') or search['link'].startswith('https://'):
                liink = search['link']
            elif search['link'].startswith('www'):
                liink = 'http://'+search['link']
            else:
                liink = 'http://www.'+search['link']
            return redirect(liink)
        else:
            return 'INVALID LINK'


if __name__ == '__main__':
    app.run(debug=True)