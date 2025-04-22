# ChurnIQ – Customer Churn Prediction API

Lightweight FastAPI prototype for predicting subscription churn based on customer behavior. Trains a logistic regression model and exposes predictions via REST.

## 🔍 Features
- Train/test a churn prediction model
- Serve predictions with FastAPI
- Docker-ready, Postman-friendly
- Swagger UI documentation out-of-the-box

## 📁 Setup

### Run Locally
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app/churn_model.py
uvicorn app.api:app --reload
```

### Run with Docker
```bash
docker build -t churniq .
docker run -p 8000:8000 churniq
```

### Test via Swagger UI
Go to: [http://localhost:8000/docs](http://localhost:8000/docs)

### Test via Postman or Curl
**POST /predict_churn**
```bash
curl -X POST http://localhost:8000/predict_churn \
-H "Content-Type: application/json" \
-d '{"age": 30, "subscription_months": 12, "login_freq": 5}'
```

**Response**
```json
{ "churn_probability": 0.435 }
```

## 🔮 Roadmap
- PostgreSQL storage
- Time-based retraining
- Confidence intervals
- Role-based dashboard integration
