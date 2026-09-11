# Time Series Weather Forecasting

This project uses the Jena Climate dataset and TensorFlow to forecast temperature from past observations.

## What I worked on

- Time-series forecasting using weather observations sampled every 10 minutes and resampled for a 2-hour view
- Exploring and visualizing the data
- Looking at trend, seasonality, and noise
- Handling invalid values in the dataset
- Splitting the data chronologically into training, validation, and test sets
- Normalizing the data using statistics calculated from the training set
- Creating windowed datasets for forecasting
- Building a baseline forecast for comparison
- Training a neural network forecast model with TensorFlow
- Evaluating forecasts with mean absolute error (MAE)
- Comparing actual and predicted temperatures

The notebook contains the data preparation, visualizations, forecasting experiments, and actual-versus-predicted results.