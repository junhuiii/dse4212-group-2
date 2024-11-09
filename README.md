# DSE4212 Group 2: Oil and Gas Stock Price Prediction
This repository contains our codes for the DSE4212 Group Project in AY 24/25 Semester 1.

# Project Introduction
# Project Overview

Stock price prediction remains a challenging task in the field of financial forecasting. The inherent volatility and noise in the stock market make it difficult to accurately predict future price movements. Traditional approaches such as fundamental analysis and technical analysis have been widely used, but often fall short in capturing the intricate and nonlinear patterns influencing stock prices, particularly in highly volatile markets such as oil and gas.

To address these limitations, researchers have explored various statistical and machine learning techniques. Time series analysis methods, such as AutoRegressive Integrated Moving Average (ARIMA), have been widely employed to model and forecast time series data. In recent years, machine learning techniques have emerged as a powerful tool for stock price prediction, with Neural Networks (NN) like Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks proving particularly effective for handling time series data.

This project aims to compare the performance of statistical and machine learning techniques on predicting closing prices for oil and gas stocks. We explore five models:
- **Seasonal Auto-Regressive Integrated Moving Average (SARIMA)**
- **Autoregressive Distributed Lag (ARDL)**
- **Long Short-Term Memory (LSTM)**
- **Transformer**
- **Temporal Fusion Transformer (TFT)**

By evaluating the performance of these models against a naive baseline (using the previous day's closing price as the prediction), we aim to identify the most effective approach for predicting future price movements in the volatile oil and gas market.

## Repository Structure
```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── data
│   ├── processed-data
│   ├── raw-data
│   ├── results
│   └── README.md
├── data-pull
│   ├── processed-data
│   └── README.md
├── evaluation
│   ├── evaluation.ipynb
│   └── README.md
├── feature engineering
│   ├── feature_engineering.ipynb
│   └── README.md
├── models
│   ├── ardl
│   │   └── ardl.ipynb
│   ├── lstm
│   │   └── lstm.py
│   ├── sarima
│   │   ├── models.py
│   │   ├── sarima_bp.ipynb
│   │   ├── sarima_cvx.ipynb
│   │   ├── sarima_eqnr.ipynb
│   │   ├── sarima_oxy.ipynb
│   │   ├── sarima_shel.ipynb
│   │   ├── sarima_xom.ipynb
│   │   ├── stat_plot.py
│   │   └── stattest.py
│   ├── tft
│   │   └── tft.ipynb
│   └── transformer
│       └── transformer.ipynb
```
## Setup

1. Install [pipenv](https://pypi.org/project/pipenv/):

   ```shell
   pip install pipenv
   ```

2. Create a virtual environment and install dependencies:

   ```shell
   pipenv install --dev
   ```

3. Adding dependencies:

   If you need to add a new dependency, use the following command:

   ```shell
   pipenv install <package-name>
   ```

## Help Page for installations

If you encounter this error for the installation of Ta-lib:
```
fatal error: ta-lib/ta_libc.h: No such file or directory
```

1. Download [this](http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz)
2. cd /path/to/download
3. Run this code : 
    ```
    tar xf ta-lib-0.4.0-src.tar.gz
    cd ta-lib
    ./configure --prefix=/usr/local
    make
    sudo make install
    ```
4. Then:
    ```
    pip install TA-Lib
    ```