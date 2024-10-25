# ML-Based-Stock-Forecast-Portfolio-
An evaluation of the effectiveness of various forecasting models for estimating mean returns within the mean-variance optimization framework.

This repository contains the code, results, and a detailed report on forecasting stock prices and constructing optimized portfolios using various machine learning and time series models. The study focuses on stocks in China’s A-share SSE50 index and compares models based on cumulative returns over the testing period.

## Project Overview
The objective is to enhance the accuracy of stock return predictions and optimize portfolio performance. Models include:
- **Time Series Models**: ARIMA, SARIMAX, Exponential Smoothing
- **Machine Learning Models**: Random Forest, Gradient Boosting (GBM), Support Vector Machine (SVM), Long Short-Term Memory (LSTM), and Linear Regression

The Random Forest model achieved the highest cumulative returns, outperforming traditional time series models and the market return benchmark.

## Project Structure
- `Data_Preprocessing.py`: Prepares data from the SSE50 index, can be found in the Data folder
- `Data`: Contains all the stock data we use in this project 
- `Full Code.ipynb`: Implements forecasting models and portfolio optimization
- `Results`: Visualizations comparing model and market returns
- `Project Report.pdf`: Detailed final report on methodology, results, and analysis

## Getting Started
1. Clone the repository
2. Install necessary dependencies
3. Run `code.ipynb` to replicate model training, testing, and portfolio optimization steps

## Key Findings
Machine learning models, especially Random Forest, provide superior return forecasts compared to traditional time series models, suggesting a robust approach for stock return predictions in portfolio management.

## Contributors
- Celline Williem: Data preprocessing, report integration
- Yohanes James: Machine learning models
- Edward Jayadi Halim: Time series models
- Jefferson Joseph Tedjojuwono: Baseline models, visualizations, testing
