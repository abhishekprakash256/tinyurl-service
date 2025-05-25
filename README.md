## Tiny Url service


### Description 

The tiny url service for making the url redirection using the flask service , using the redis as the storage of the keys as the redis and using the unique has generator the key storage system. 


## The ports

- 5050
- flask run --port=5050
- gunicorn app:app --bind 0.0.0.0:5050
