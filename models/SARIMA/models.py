
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.statespace.sarimax import SARIMAX


def run_sarima(train_df, test_df, order=(1, 1, 1), seasonal_order=(1, 1, 4, 63)):
    # Define train and test sets
    num_symbols = len(test_df.columns)
    rows = (num_symbols // 3) + (1 if num_symbols % 3 != 0 else 0)
    fig, axs = plt.subplots(rows, 3, figsize=(18, 6 * rows))
    axs = axs.flatten()

    models = {}
    result_dict = {}

    for idx, symbol in enumerate(test_df.columns):
        actuals = test_df[symbol].values
        dates = test_df.index

        # Initialize history with training data for rolling forecast as a list
        history = list(train_df[symbol].values)
        predictions = []

        # Iteratively fit model and forecast for each step in the test set
        for t in range(len(test_df)):
            # Fit SARIMAX model on the current history without exogenous variables
            model = SARIMAX(history, order=order, seasonal_order=seasonal_order,
                            enforce_stationarity=False, enforce_invertibility=False)
            try:
                model_fit = model.fit(disp=False)
            except Exception as e:
                print(f"Model for {symbol} failed to converge at step {t}: {e}")
                break

            # Forecast the next step
            forecast = model_fit.forecast(steps=1)[0]
            predictions.append(forecast)

            # Append actual test value to history for rolling window
            history.append(test_df[symbol].iloc[t])

        # Create a DataFrame to store predictions and errors
        errors = np.array(predictions) - actuals
        result_df = pd.DataFrame({
            'datetime': dates,
            'actual': actuals,
            'predicted': predictions,
            'error': errors
        })
        result_dict[symbol] = result_df

        # Plotting the results
        axs[idx].plot(train_df.index, train_df[symbol], label='Train')
        axs[idx].plot(test_df.index, test_df[symbol], label='Test')
        axs[idx].plot(test_df.index, predictions, label='T+1 Forecast', color='green')
        axs[idx].set_title(f'SARIMAX Model T+1 Rolling Forecast for {symbol}')
        axs[idx].set_xlabel('Date')
        axs[idx].set_ylabel('Price')
        axs[idx].legend()

        # Display performance metrics
        mae = mean_absolute_error(test_df[symbol], predictions)
        print(f'{symbol} - Mean Absolute Error: {mae}')
        models[symbol] = model_fit  # Store the last fitted model for each symbol

    # Remove any extra subplots
    for i in range(num_symbols, len(axs)):
        fig.delaxes(axs[i])

    plt.tight_layout()
    plt.show()

    return models, result_dict

def run_sarimax(train_df, test_df, exog_train: pd.DataFrame, exog_test: pd.DataFrame, order=(1, 1, 1), seasonal_order=(1, 1, 4, 63)):
    # Define train and test sets
    num_symbols = len(test_df.columns)
    rows = (num_symbols // 3) + (1 if num_symbols % 3 != 0 else 0)
    fig, axs = plt.subplots(rows, 3, figsize=(18, 6 * rows))
    axs = axs.flatten()

    models = {}
    result_dict = {}

    for idx, symbol in enumerate(test_df.columns):
        actuals = test_df[symbol].values
        dates = test_df.index

        # Initialize history with training data for rolling forecast as a list
        history = list(train_df[symbol].values)
        predictions = []

        # Iteratively fit model and forecast for each step in the test set
        for t in range(len(test_df)):
            # Concatenate exogenous variables up to the current step
            exog_history = pd.concat([exog_train, exog_test.iloc[:t]]) if exog_train is not None else None
            exog_step = exog_test.iloc[[t]].values if exog_test is not None else None
            
            # Fit SARIMAX model on the current history with exogenous variables
            model = SARIMAX(history, order=order, seasonal_order=seasonal_order, exog=exog_history,
                            enforce_stationarity=False, enforce_invertibility=False)
            try:
                model_fit = model.fit(disp=False)
            except Exception as e:
                print(f"Model for {symbol} failed to converge at step {t}: {e}")
                break

            # Forecast the next step with the corresponding exogenous variable from test set
            forecast = model_fit.forecast(steps=1, exog=exog_step).iloc[0]
            predictions.append(forecast)

            # Append actual test value to history for rolling forecast
            history.append(test_df[symbol].iloc[t])

        # Create a DataFrame to store predictions and errors
        errors = np.array(predictions) - actuals
        result_df = pd.DataFrame({
            'datetime': dates,
            'actual': actuals,
            'predicted': predictions,
            'error': errors
        })
        result_dict[symbol] = result_df

        # Plotting the results
        axs[idx].plot(train_df.index, train_df[symbol], label='Train')
        axs[idx].plot(test_df.index, test_df[symbol], label='Test')
        axs[idx].plot(test_df.index, predictions, label='T+1 Forecast', color='green')
        axs[idx].set_title(f'SARIMAX Model T+1 Rolling Forecast for {symbol}')
        axs[idx].set_xlabel('Date')
        axs[idx].set_ylabel('Price')
        axs[idx].legend()

        # Display performance metrics
        mae = mean_absolute_error(test_df[symbol], predictions)
        print(f'{symbol} - Mean Absolute Error: {mae}')
        models[symbol] = model_fit  # Store the last fitted model for each symbol

    # Remove any extra subplots
    for i in range(num_symbols, len(axs)):
        fig.delaxes(axs[i])

    plt.tight_layout()
    plt.show()

    return models, result_dict

