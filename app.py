"""
This file contains the main application logic for the tiny URL service.
This flask application provides endpoints to create a short URL, retrieve the original URL,
The application uses redis to store the mapping between the short hashes and the orginla urls

"""

from flask import Flask,request, jsonify , redirect , url_for
from flask_cors import cross_origin  # Not CORS app-wide
from redis_helper_kit import Helper_fun
from hash_utils import generate_unique_hash




#SET REDIS CONFIGURATION   
REDIS_HOST = 'localhost'
PRIMARY_SET = 'frest_hash_set'
SECONDRY_SET = 'used_hash_set'
HASH_NAME = 'tiny_url_hash'



#make the submission route 
app = Flask(__name__)


@app.route('/')
def index():
    """
    Endpoint to check if the service is running.
    """
    return "<h1>Welcome to the TinyURL Service! Use /tu/submit to create a short URL.</h1>", 200




@app.route('/tu/<hash_val>', methods=['GET'])  

def get_original_url(hash_val):
    """
    Endpoint to retrieve the original URL using the short hash.
    """
    #make the instance for the redis helper
    redis_helper = Helper_fun(host_name = REDIS_HOST)

    #get the url from the hash
    url = redis_helper.get_hash_value(hash_val, HASH_NAME)

    if not url:
        return jsonify({"error": "URL not found"}), 404
    
    #redirect to the original URL
    return redirect(url, code=302)





@app.route('/tu/submit', methods=['POST'])
@cross_origin()  # Allow CORS on this route only
def submit_url():
    """
    Endpoint to submit a URL and get a short hash.
    I have to pass the htps://url.com in the frontend
    """
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    # Generate a unique hash
    generate_unique_hash(PRIMARY_SET, SECONDRY_SET, REDIS_HOST, 5, 10, 100)

    #make the instance for the redis helper
    redis_helper = Helper_fun(host_name = REDIS_HOST)

    #pop the hash from the redis set
    hash_val = redis_helper.pop_set_val(PRIMARY_SET)
    
    # Store the URL in the hash
    redis_helper.add_value_to_hash(hash_val, url, HASH_NAME)

    #add the hash to the secondary set
    redis_helper.add_value_to_set(hash_val, SECONDRY_SET)
    
    return jsonify({"tinyurl" : "https://meabhi.me/tu/" + hash_val}), 201


# Gunicorn will use this
app_wsgi = app

if __name__ == '__main__':
    """
    Starts the Flask application server for local development.

    This is only used when running the app directly and is not required in a production environment.
    The server listens on all available interfaces (0.0.0.0) and uses port 5050.
    """
    app.run(debug=True, host='0.0.0.0', port=5050)
