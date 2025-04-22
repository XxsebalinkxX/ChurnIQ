# ChurnIQ – Customer Churn Prediction API

ChurnIQ is a lightweight FastAPI-based prototype that predicts customer churn likelihood using behavioral data. It uses logistic regression to generate churn probabilities and serves predictions via a RESTful API with interactive Swagger UI.

## 🔍 Features
- Trains a logistic regression model using customer behavior metrics
- Returns churn probability via a `/predict_churn` endpoint
- Fully containerized with Docker
- Swagger UI and curl/Postman-friendly

## 📁 Project Structure
```
churniq/
├── app/
│   ├── churn_data.csv
│   ├── churn_model.py
│   ├── api.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env
└── README.md
```

## ⚙️ Local Setup

### 1. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/Scripts/activate     # Git Bash on Windows
```

### 2. Install requirements
```bash
pip install --upgrade pip
pip install --force-reinstall -r requirements.txt
```

### 3. Train the model
```bash
python app/churn_model.py
```

### 4. Start the API server
```bash
uvicorn app.api:app --reload
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Setup

### 1. Build the Docker image
```bash
docker build -t churniq .
```

### 2. Run the container
```bash
docker run -p 8000:8000 churniq
```

Then open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔮 API Details

**POST** `/predict_churn`  
Returns churn probability for a customer.

### Sample Request
```json
{
  "age": 30,
  "subscription_months": 12,
  "login_freq": 5
}
```

### Sample Response
```json
{
  "churn_probability": 0.435
}
```

### Curl Example
```bash
curl -X POST http://localhost:8000/predict_churn \
-H "Content-Type: application/json" \
-d '{"age": 30, "subscription_months": 12, "login_freq": 5}'
```

---

## 🔧 Tech Stack
Python · FastAPI · scikit-learn · pandas · Uvicorn · Docker · Swagger (OpenAPI)

---

## 🧠 Next Steps
- Add PostgreSQL for prediction storage
- Implement scheduled model retraining
- Expand to support tiered churn risk levels (Low / Medium / High)
