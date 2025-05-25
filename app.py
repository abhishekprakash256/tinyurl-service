"""
This file contains the main application logic for the tiny URL service.
This flask application provides endpoints to create a short URL, retrieve the original URL,
The application uses redis to store the mapping between the short hashes and the orginla urls

"""

from flask import Flask, request, jsonify



