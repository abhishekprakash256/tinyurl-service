"""
This file contains the main application logic for the tiny URL service.
This flask application provides endpoints to create a short URL, retrieve the original URL,
The application uses redis to store the mapping between the short hashes and the orginla urls

"""

from flask import Flask, request, jsonify
from redis_helper_kit import Helper_fun
from unique_hash_generator import generate_unique_hash




#SET REDIS CONFIGURATION
REDIS_HOST = 'localhost'
HASH_NAME = 'TEST_HASH'
SET_NAME = 'TEST_SET'




#make the redis instance
redis_helper = Helper_fun(REDIS_HOST, HASH_NAME, SET_NAME)

# generate a unique hash to store in the redis 
generate_unique_hash(HASH_NAME, SET_NAME, REDIS_HOST, 5, 10, 100)   #min length 5, max length 10, 100 hashes

#pop the hash from the redis set
redis_helper.pop_set_val()

#add the hash and the url to redis
redis_helper.add_value_to_hash("key1", "value1")

#get the value from the hash
redis_helper.get_hash_value("key1")


