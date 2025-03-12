# Bookmark Manager Service

## High-Level Design
- FastAPI-based RESTful API
- PostgreSQL for persistent storage
- Redis for caching and rate limiting
- Docker containerization

## Setup Development Environment

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

These steps ensure isolated development environment with correct package versions.

## Installation & Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run with Docker Compose: `docker-compose up -d`

## API Endpoints
- POST /shorten/ - Create short URL
- GET /bookmarks/ - List bookmarks
- GET /bookmarks/{id} - Get bookmark
- GET /analytics/ - View statistics

## Deployment
1. Build Docker image: `docker build -t bookmark-manager .`
2. Deploy using docker-compose: `docker-compose up -d`
3. Access API at http://localhost:8000

## CI/CD Pipeline
The project uses GitHub Actions for continuous integration and deployment:

1. Automated testing on every push and PR
2. Docker image building and pushing to Docker Hub
3. Automatic deployment to Docker Desktop

### Setup CI/CD:
1. Add secrets to GitHub repository:
   - DOCKER_HUB_USERNAME
   - DOCKER_HUB_ACCESS_TOKEN
2. Push to main branch to trigger deployment

## Testing
Run tests using: `pytest tests/`
