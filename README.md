# ML-Based-Stock-Forecast-and-Efficient-Portofolio-Construction
An evaluation of the effectiveness of various forecasting models for estimating mean returns within the mean-variance optimization framework.

This repository contains the code, results, and a detailed report on forecasting stock prices and constructing optimized portfolios using various machine learning and time series models. The study focuses on stocks in China’s A-share SSE50 index and compares models based on cumulative returns over the testing period.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Data Sources](#data-sources)
- [Key Findings](#key-findings)
- [Project Members](#project-members)

## Overview
The objective is to enhance the accuracy of stock return predictions and optimize portfolio performance. Models include:
- **Time Series Models**: ARIMA, SARIMAX, Exponential Smoothing
- **Machine Learning Models**: Random Forest, Gradient Boosting (GBM), Support Vector Machine (SVM), Long Short-Term Memory (LSTM), and Linear Regression

The Random Forest model achieved the highest cumulative returns, outperforming traditional time series models and the market return benchmark.

## Repository Structure

```plaintext
ML-Based-Stock-Forecast-Portfolio/
├── Data/                   # Contains all the stock data we use in this project
│   ├── data_processing.py  # Source code for data processing
├── Results/                # Visualizations comparing model and market returns
├── Full Code.ipynb         # Jupyter notebooks for forecasting models and portfolio optimization
├── Project report.pdf      # Detailed final report on methodology, results, and analysis
└── README.md               # Project documentation (this file)
```

## Installation
1. Clone the repository
2. Install necessary dependencies
3. Run `Full Code.ipynb` to replicate model training, testing, and portfolio optimization steps

## Data Sources 
The monthly returns data, along with additional financial metrics such as the monthly riskfree rate, Price-to-Earnings (P/E) ratio, and Price-to-Book (P/B) ratio, were sourced from
[CSMAR](https://data.csmar.com/) (China Stock Market & Accounting Research Database)

## Key Findings
In the discussion of the results, it's evident that the performance of various models varies significantly, with distinct patterns emerging among the different types of models employed. Notably, the baseline Simple Mean model, along with the ARIMA and SARIMAX time series models, underperform relative to the market return in terms of overall cumulative returns. This underperformance could suggest limitations in the ability of traditional time series models to capture and leverage patterns in stock price movements effectively under the conditions tested.

In contrast, the Exponential Smoothing model shows a marginal improvement over the market return by the end of the testing period. This slight edge indicates that while simple time series methods might sometimes capture general market trends, they do not consistently provide superior returns, especially in volatile or complex market conditions. This result reinforces the notion that relying solely on traditional time series models may not be sufficient for optimizing investment strategies.

On the other hand, machine learning models demonstrate a more robust performance, consistently surpassing the market return. Notably, the Random Forest model achieves the highest final cumulative return, followed by the Gradient Boosting Machine (GBM) and Linear Regression models. The superior performance of these machine learning models suggests their greater efficacy in discerning and exploiting complex patterns in the data, likely due to their ability to model non-linear relationships and interactions that are not readily apparent or accessible to simpler statistical or time series models.

This variance in performance underscores the importance of choosing the right model based on the specific objectives and constraints of the investment strategy, with machine learning models providing a compelling option for scenarios where capturing complex market dynamics is critical.

The final cumulative returns of all the models on the last month of the testing period is listed in the table below ordered ascendingly:
| Model                   | Final Cumulative Returns  |
|-------------------------|---------------------------|
| ARIMA                   | -0.2436942325821847       |
| Simple Mean             | -0.23650128981019125      |
| SARIMAX                 | -0.15575594113950597      |
| Market Return           | -0.10344144224650875      |
| Exponential Smoothing   | -0.0903985372848991       |
| SVM                     | -0.08249145555763393      |
| LSTM                    | -0.05189191530285808      |
| Linear Regression       | 0.0357402929015731        |
| GBM                     | 0.08566223766447356       |
| Random Forest           | 0.17592660511426317       |



## Project Members
| Name                         | Contributions                           |      
|------------------------------|-----------------------------------------|
| Celline Williem              | Data preprocessing, report integration  |
| Edward Jayadi Halim          | Time series models                      |
| Jefferson Joseph Tedjojuwono | Baseline models, visualizations, testing|
| Yohanes James                | Machine learning models                 |
