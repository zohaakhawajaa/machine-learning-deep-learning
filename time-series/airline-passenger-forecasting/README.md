# Airline Passengers Time Series Forecasting

## Project Overview

This project analyzes monthly airline passenger data and builds a time-series forecasting workflow using exploratory analysis, seasonal decomposition, stationarity testing, lag-based features, and linear regression.

The notebook is designed as a practical learning project and keeps the complete analysis in one reproducible Jupyter notebook.

## Dataset

`AirPassengers.csv` contains 144 monthly observations from January 1949 through December 1960. The dataset includes:

- `Month`: observation month
- `#Passengers`: number of airline passengers

## Objective

The objective is to understand the structure of the passenger series and predict future passenger counts from historical lag values while evaluating the predictions on a chronological holdout set.

## Technologies and Libraries

- Python
- Jupyter Notebook
- pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- statsmodels
- scikit-learn

## Analysis Workflow

### Data Preprocessing

The notebook loads the CSV, converts `Month` to a datetime value, assigns it as a monthly time-series index, checks the data range and frequency, and verifies missing values.

### Time-Series Visualization

Static Matplotlib charts and interactive Plotly charts show the monthly passenger series and its overall movement over time.

### Trend and Seasonality Analysis

Yearly totals, monthly averages, and a 12-month moving average are used to highlight the long-term upward trend and recurring annual passenger pattern.

### Seasonal Decomposition

A multiplicative seasonal decomposition separates the observed series into trend, seasonal, and residual components using a 12-month period.

### Stationarity Analysis

An Augmented Dickey-Fuller test is applied to the original series. The result is interpreted alongside the visible trend and seasonality to assess whether the series is stationary.

### Train/Test Splitting

The data is split chronologically, with 80% used for training and the final 20% reserved for testing. This preserves the temporal order and avoids random shuffling.

### Lag Features

The forecasting dataset uses the following historical passenger values as predictors:

- `lag_1`: previous month
- `lag_2`: two months earlier
- `lag_3`: three months earlier
- `lag_12`: same month in the previous year

Rows with missing lag values are removed before modeling.

### Forecasting Model

A scikit-learn `LinearRegression` model predicts current passenger counts from the lag features. The model is trained on the earlier portion of the lag-based dataset and evaluated on the later portion.

### Evaluation Metrics

The notebook reports:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

It also plots actual and predicted passenger counts for the test period using Matplotlib and Plotly.

## Results

The analysis shows a strong upward trend, clear yearly seasonality, and non-stationarity in the original passenger series. The lag-based linear regression model produces test-set forecasts whose MAE and RMSE are printed directly by the notebook. The final actual-versus-predicted charts provide a visual comparison of forecast quality across the holdout period.

## Key Learnings

- Time-series data must be split in chronological order.
- Visualization helps reveal trend, seasonality, and changing variability before modeling.
- Seasonal decomposition makes the main components of a series easier to interpret.
- ADF testing provides a statistical complement to visual stationarity checks.
- Lag features turn historical observations into supervised-learning inputs.
- A simple baseline model is useful for understanding the problem before applying more advanced forecasting methods.

## How to Run the Notebook

From this project directory, create or activate a Python environment and install the required libraries:

```bash
python -m pip install pandas numpy matplotlib seaborn plotly statsmodels scikit-learn jupyter
```

Open `airline_passenger_forecasting.ipynb` in VS Code or Jupyter and run the cells from top to bottom. Keep `AirPassengers.csv` in the same directory as the notebook so the relative data path resolves correctly.
