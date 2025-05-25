## Tiny Url service


### Description 

The tiny url service for making the url redirection using the flask service , using the redis as the storage of the keys as the redis and using the unique has generator the key storage system. 


## Reqs 

- docker run -d --name redis --network my_network -p 6379:6379 redis:latest
- pip install git+https://github.com/abhishekprakash256/redis-helper-kit.git
- pip install git+https://github.com/abhishekprakash256/hash-utils.git
 


## The ports

- 5050
- flask run --port=5050
- gunicorn app:app --bind 0.0.0.0:5050


## Notes 

- run the redis 
- docker run -d --name redis --network my_network -p 6379:6379 redis:latest
- 