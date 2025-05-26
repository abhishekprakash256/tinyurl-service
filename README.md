

# Tiny URL Service

A lightweight Flask-based URL shortening service powered by Redis and a custom hash generator. This service allows users to shorten long URLs and redirect to them using unique, randomly generated short hashes.

---

## 📋 Features

* Shortens long URLs to tiny, unique hashes
* Stores mapping in Redis for fast lookup
* Hash collision avoidance via Redis-backed uniqueness checks
* Simple API with endpoints for submission and redirection
* Supports both Flask development server and Gunicorn for production

---

## 🚀 Quick Start

### ✅ Requirements

* Python 3.7+
* Redis server (local or Docker)
* Pip

### 📦 Installation

```bash
# Clone your service repo if needed
# git clone git@github.com:abhishekprakash256/tinyurl-service.git
# cd tinyurl-service

# Install dependencies
pip install git+https://github.com/abhishekprakash256/redis-helper-kit.git
pip install git+https://github.com/abhishekprakash256/hash-utils.git
```

---

## 🐳 Redis Setup with Docker

```bash
docker network create my_network

docker run -d \
  --name redis \
  --network my_network \
  -p 6379:6379 \
  redis:latest
```

---

## 🔌 Running the Service

### Development (Flask)

```bash
flask run --host=0.0.0.0 --port=5050
```

### Production (Gunicorn)

```bash
gunicorn app:app --bind 0.0.0.0:5050
```

---

## 🔧 Configuration

Environment variables / constants used in the app:

* `REDIS_HOST`: Host for Redis (default: `localhost`)
* `PRIMARY_SET`: Set of unused/generated hashes
* `SECONDARY_SET`: Set of used hashes to avoid collisions
* `HASH_NAME`: Redis hash for storing `short_hash -> long_url` mappings

---

## 🔁 API Usage

### ➕ Submit a URL

**Endpoint**: `POST /tu/submit`

**Request Body**:

Pass the url with https or http

```json
{
  "url": "https://example.com"
}
```

**Response**:

```json
{
  "tinyurl": "https://meabhi.me/tu/abc123"
}
```

---

### 🔍 Redirect to Original URL

**Endpoint**: `GET /tu/<hash>`

**Example**:

```bash
curl -i http://localhost:5050/tu/abc123
```

Will return a 302 redirect to the original URL.

---

## 📝 Notes

* Ensure Redis is running **before starting Flask/Gunicorn**
* The service pre-generates a batch of unique hashes and stores them in a Redis set
* You can scale the hash generation and storage strategy based on your load

---

## 🧪 Future Enhancements

* URL expiration and TTL support
* Custom hash support
* Rate limiting and abuse protection
* Basic UI for submitting and viewing short links