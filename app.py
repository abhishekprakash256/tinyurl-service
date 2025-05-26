"""
This file contains the main application logic for the tiny URL service.
This flask application provides endpoints to create a short URL, retrieve the original URL,
The application uses redis to store the mapping between the short hashes and the orginla urls

"""

#from flask import Flask,request, jsonify, send_from_directory, abort
from redis_helper_kit import Helper_fun
from hash_utils import generate_unique_hash




#SET REDIS CONFIGURATION
REDIS_HOST = 'localhost'
PRIMARY_SET = 'frest_hash_set'
SECONDRY_SET = 'used_hash_set'
HASH_NAME = 'tiny_url_hash'





#make the redis instance
redis_helper = Helper_fun(host_name = REDIS_HOST)

# generate a unique hash to store in the redis 
generate_unique_hash(PRIMARY_SET, SECONDRY_SET, REDIS_HOST, 5, 10, 100)   #min length 5, max length 10, 100 hashes

#pop the hash from the redis set
hash_val = redis_helper.pop_set_val(PRIMARY_SET)

print("hash_val: ", hash_val)

#add the hash and the url to redis
redis_helper.add_value_to_hash(hash_val, "www.meabhi.me" , HASH_NAME)

#get the value from the hash
url = redis_helper.get_hash_value(hash_val , HASH_NAME)

print("url: ", url)

