Start all services:

    docker-compose up


Services:

- webapp (static webserver):  
  http://localhost
- grafana:  
  http://localhost:3000
- api (Python):  
  http://localhost:8000
- database (PostgreSQL):  
  127.0.0.1:5432


Rapid API Python development:

    python -m venv venv
    source venv/Scripts/activate
    cd apps/api/
    pip install -r requirements.txt
    flask run
