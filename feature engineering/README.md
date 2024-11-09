# Set up

Before proceeding, please refer to the [README in the `/data` folder](../data/README.md) for instructions on how to properly organize and prepare the data directory.

1. **Organize the Data Folder**:  
   Set up the `/data` folder with subdirectories as specified in the README, including the `raw-data` folder.

2. **Access Data**:  
   Download the required data files from this [Google Drive link](https://drive.google.com/drive/folders/1lgnXAPzCs-zCzhWVeugy_N3AHvRELp8E?usp=drive_link) and place them in the `raw-data` folder within the `/data` directory.

---

We have data for the following tickers, representing six stocks in the oil and gas industry and two futures:

- **BP**: BP p.l.c. (British Petroleum)
- **SHEL**: Shell plc (formerly Royal Dutch Shell)
- **OXY**: Occidental Petroleum Corporation
- **XOM**: Exxon Mobil Corporation
- **CVX**: Chevron Corporation
- **EQNR**: Equinor ASA
- **CL1**: Crude Oil Futures (Generic 1st Future)
- **NG1**: Natural Gas Futures

The [Feature engineering.ipynb](Feature%20engineering.ipynb) notebook includes several sections to guide you through the data preparation:

- Load data
- Data engineering
- Exploratory Data Analysis
- Feature Engineering
- Partitioning the Dataset

Ensure the `/data` folder setup is complete to allow smooth execution of the feature engineering steps.