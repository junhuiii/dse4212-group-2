import pandas as pd
from scipy.stats import shapiro
from statsmodels.tsa.stattools import adfuller

def adf_test(df: pd.DataFrame):
    for symbol in df.columns:
        symbol_data=df[symbol]
        print([symbol])
        adf_result = adfuller(symbol_data)
        print(f'ADF Statistic for {symbol}: {adf_result[0]}')
        print(f'p-value for {symbol}: {adf_result[1]}')

        # Interpret the p-value
        if adf_result[1] < 0.05:
            print(f"{symbol} is stationary (reject null hypothesis of unit root).")
        else:
            print(f"{symbol} is non-stationary (fail to reject null hypothesis of unit root).")

def shapiro_test(df):
    # Perform Shapiro-Wilk test for normality on the symbol's data
    for symbol in df.columns:
        symbol_data=df[symbol]
        print([symbol])
        shapiro_result = shapiro(symbol_data)
        print(f'Shapiro-Wilk Statistic for {symbol}: {shapiro_result[0]}')
        print(f'p-value for Shapiro-Wilk test for {symbol}: {shapiro_result[1]}')

        # Interpret the p-value for normality
        if shapiro_result[1] > 0.05:
            print(f"{symbol} follows a normal distribution (fail to reject null hypothesis).")
        else:
            print(f"{symbol} does not follow a normal distribution (reject null hypothesis).")
