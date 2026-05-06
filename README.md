# End-to-End Sales Forecasting System with API

## Project Overview

This project builds a production-ready time series forecasting system to predict the next 8 weeks of sales for each state using historical sales data.

The system trains multiple forecasting models, compares their performance using MAE (Mean Absolute Error), automatically selects the best-performing model, and exposes predictions through a REST API using FastAPI.

## API Documentation Preview

![Swagger UI](images/swagger_ui.png)

## Features

### Forecasting Models
- Prophet
- XGBoost (with lag features)
- ARIMA

### Feature Engineering
- Lag Features (`lag_1`, `lag_7`)
- Rolling Mean
- Month Feature
- Day of Week Feature

### Additional Features
- Model Evaluation using MAE
- Automatic Best Model Selection
- Forecast generation for all states
- REST API using FastAPI
- Interactive Swagger UI Documentation
- Production-style project structure

## Dataset

The dataset contains state-wise sales data with the following columns:

- State
- Date
- Total Sales
- Category

Historical sales data was used to forecast the next 8 weeks of sales for each state.

## Models Implemented

### 1. Prophet
Used for capturing trend and seasonality patterns in time-series forecasting.

### 2. XGBoost
Machine learning forecasting model using engineered lag features.

### 3. ARIMA
Classical statistical time-series forecasting model.

## Model Evaluation

Models were compared using:
- Mean Absolute Error (MAE)

The system automatically selected the best-performing model based on evaluation scores.

## Tech Stack

- Python
- Pandas
- NumPy
- Prophet
- XGBoost
- ARIMA (Statsmodels)
- Scikit-learn
- FastAPI
- Uvicorn
- Matplotlib
- Google Colab
- GitHub

## Project Structure

```text
sales_forecasting_system/
│
├── app.py
├── all_states_forecast.csv
├── sales_forecasting_pipeline.ipynb
├── README.md
│
├── images/
│   └── swagger_ui.png
│
├── data/
│   └── Forecasting_Case_Study.xlsx
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ayank17/sales_forecasting_system.git
```

### 2. Navigate to the project folder

```bash
cd sales_forecasting_system
```

### 3. Install required libraries

```bash
pip install pandas numpy prophet xgboost scikit-learn statsmodels fastapi uvicorn matplotlib
```

## Run the API

Start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

Open in browser:

```bash
http://127.0.0.1:8000
```

## API Endpoints

### Home 

```bash
GET /
```

Returns the API status message.

---

### Forecast for All States

```bash
GET /forecast
```

Returns forecasted sales data for all states.

---

### Forecast for Specific State

```bash
GET /forecast/{state}
```

Example:

```bash
GET /forecast/California
```

Returns forecasted sales data for the selected state.

---

### Swagger API Documentation

```bash
GET /docs
```

Opens interactive Swagger UI documentation for API testing.

## Swagger API Documentation

Interactive API documentation is available at:

```bash
http://127.0.0.1:8000/docs
```

The Swagger UI allows:
- API testing directly from browser
- Endpoint visualization
- Response preview
- Parameter testing

## Output

The final forecast output is stored in:

```bash
all_states_forecast.csv
```

The output contains:
- Forecasted sales values
- Date-wise predictions
- State-wise forecasting results

## Project Workflow

1. Data Preprocessing  
2. Feature Engineering  
3. Model Training  
4. Model Evaluation using MAE  
5. Best Model Selection  
6. Forecast Generation  
7. API Deployment using FastAPI  

## Project Demo

The project demonstrates:
- Data preprocessing
- Feature engineering
- Forecast generation
- Model comparison
- REST API deployment
- Swagger API testing

## Author

**Mayank Tarneja**

### Connect With Me

- LinkedIn: https://www.linkedin.com/in/mayank-tarneja-a6577a270/
- GitHub: https://github.com/ayank17
- Portfolio: https://personal-portfolio-tan-seven.vercel.app/

## Future Improvements

- Add LSTM-based deep learning forecasting
- Deploy API on cloud platforms (AWS / Render)
- Build a real-time forecasting pipeline
- Add dashboard integration for visualization

## Project Status

Completed and Submission Ready
