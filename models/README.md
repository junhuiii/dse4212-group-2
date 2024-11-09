# Models

The repository is structured as follows:

- **`ardl/`**: Contains scripts and notebooks for the ARDL (Autoregressive Distributed Lag) model, focusing on relationships between variables over time.
- **`lstm/`**: Contains scripts and notebooks for the LSTM (Long Short-Term Memory) model, designed to handle sequential data for time series forecasting.
- **`sarima/`**: Contains scripts and notebooks for the SARIMA (Seasonal Autoregressive Integrated Moving Average) model, suitable for time series with seasonal components.
- **`tft/`**: Contains scripts and notebooks for the TFT (Temporal Fusion Transformer) model, which leverages attention mechanisms for time series analysis.
- **`transformer/`**: Contains scripts and notebooks for the Transformer model, a deep learning approach for sequential data.

# Running the Models

Before running any of the model scripts, please ensure that the `Data` folder is set up correctly (as outlined in the [README in the `/data` folder](../data/README.md)). This setup includes the three subdirectories:

- `processed-data/` – for processed data files.
- `raw-data/` – for the raw data files.
- `results/` – for storing the output results from the model predictions and analysis.

You can access the necessary data files through this [Google Drive link](https://drive.google.com/drive/u/0/folders/1sGKPZPky4w3KAX_RrDG1Qw58VbvojLY7). Download the relevant files and place them in the appropriate subdirectories.

Once the data folder is organized, you can proceed to run the scripts in the model directories (e.g., `ardl/`, `lstm/`, `sarima/`, `tft/`, `transformer/`).

**Important**: Ensure that all required data files are in the correct subdirectories and that the `results/` folder is properly set up with the necessary result files before running the models to avoid any errors.

