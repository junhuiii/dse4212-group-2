# dse4212-group-2
This repository contains our codes for the DSE4212 Group Project in AY 24/25 Semester 1.

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