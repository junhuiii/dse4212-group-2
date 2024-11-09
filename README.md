# dse4212-group-2
This repository contains our codes for the DSE4212 Group Project in AY 24/25 Semester 1.

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