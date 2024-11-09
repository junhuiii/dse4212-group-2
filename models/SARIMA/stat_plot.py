import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def plot_all_acf(df:pd.DataFrame, lags=100, alpha =0.05):
    # Number of symbols and grid configuration
    symbols = df.columns
    n_symbols = len(symbols)
    n_rows = (n_symbols // 3) + (n_symbols % 3 > 0)  # Calculate the number of rows needed

    # Create a figure with subplots
    fig, axes = plt.subplots(n_rows, 3, figsize=(18, n_rows * 5))

    # Flatten axes array for easy iteration
    axes = axes.flatten()

    # Iterate through each symbol and plot ACF
    for i, symbol in enumerate(symbols):
        plot_acf(df[symbol].dropna(), lags=lags, ax=axes[i], alpha=alpha)
        axes[i].set_title(f'ACF Plot for {symbol}')

    # Remove any unused subplots in the grid
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the combined ACF plot
    plt.show()

def plot_all_pacf(df, lags=100, alpha=0.05):
    # Number of symbols and grid configuration
    symbols = df.columns
    n_symbols = len(symbols)
    n_rows = (n_symbols // 3) + (n_symbols % 3 > 0)  # Calculate the number of rows needed

    # Create a figure with subplots for PACF
    fig, axes = plt.subplots(n_rows, 3, figsize=(18, n_rows * 5))

    # Flatten axes array for easy iteration
    axes = axes.flatten()

    # Iterate through each symbol and plot PACF
    for i, symbol in enumerate(symbols):
        plot_pacf(df[symbol].dropna(), lags=lags, ax=axes[i],alpha=alpha)
        axes[i].set_title(f'PACF Plot for {symbol}')

    # Remove any unused subplots in the grid
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the combined PACF plot
    plt.show()


def plot_seasonal_decomp(df, period):

    # Iterate through each symbol in the DataFrame and apply seasonal decomposition
    for symbol in df.columns:
        # Drop NaN values for the symbol's data
        symbol_data = df[[symbol]]

        # Perform seasonal decomposition (assuming daily frequency, modify freq if needed)
        res = seasonal_decompose(symbol_data, model='multiplicative', period=period)

        fig = plt.figure()  
        fig = res.plot()  
        plt.title(symbol) 
        fig.set_size_inches(12, 8)
        plt.show()

# to generate and collate QQ
def plot_qq(df: pd.DataFrame):
    # Define the number of rows and columns for the plot grid
    symbols = df.columns
    n_symbols = len(symbols)
    n_rows = (n_symbols // 3) + (n_symbols % 3 > 0)  # To accommodate 3 plots per row

    # Create a figure for the QQ plots
    fig, axes = plt.subplots(n_rows, 3, figsize=(18, n_rows * 5))

    # Flatten axes array for easy indexing
    axes = axes.flatten()

    # create a QQ plot for each symbol
    for i, symbol in enumerate(symbols):
        symbol_data = df[symbol]

        qqplot(symbol_data, line='s', ax=axes[i])
        axes[i].set_title(f'QQ Plot for {symbol}')

    # Remove any unused subplots in the grid
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout
    plt.tight_layout()

    # Show the QQ plots
    plt.show()

def plot_prices_yearly(train_df):
    # Ensure the index is in datetime format if it isn't already
    if not isinstance(train_df.index, pd.DatetimeIndex):
        train_df.index = pd.to_datetime(train_df.index)

    # Get a list of symbols (columns of the DataFrame)
    symbols = train_df.columns

    # Define unique years present in the data
    unique_years = sorted(train_df.index.year.unique())
    num_years = len(unique_years)

    # Create a color map with a distinct color for each year
    cmap = cm.get_cmap('tab10', num_years)
    colors = [cmap(i) for i in range(num_years)]

    # Determine the layout: 3 plots per row
    num_symbols = len(symbols)
    rows = (num_symbols // 3) + (1 if num_symbols % 3 != 0 else 0)
    fig, axs = plt.subplots(rows, 3, figsize=(18, 6 * rows))  # Removed sharey=True

    # Flatten the axs array in case it's 2D
    axs = axs.flatten()

    # Loop through each symbol and plot data by year
    for idx, symbol in enumerate(symbols):
        # Group data by year
        for i, year in enumerate(unique_years):
            # Select data for the current year and remove any NaN values
            data = train_df[symbol][train_df.index.year == year].dropna()
            # Plot each year’s data as a simple line graph without markers
            axs[idx].plot(data.index.month + data.index.day / 31.0, data.values, 
                          label=str(year), color=colors[i], linestyle='-')

        # Set subplot title and labels
        axs[idx].set_title(symbol)
        axs[idx].set_xlabel('Month')
        axs[idx].set_ylabel('Close Price')
        axs[idx].set_xticks(range(1, 13))
        axs[idx].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Remove any unused subplots
    for i in range(num_symbols, len(axs)):
        fig.delaxes(axs[i])

    # Add a single legend for all years under all subplots
    handles = [plt.Line2D([0], [0], color=colors[i], label=str(year)) for i, year in enumerate(unique_years)]
    fig.legend(handles=handles, loc='lower center', title='Years', bbox_to_anchor=(0.5, -0.05), ncol=3)

    # Set an overall title and adjust layout
    fig.suptitle('Stock Prices Over Time by Year (Monthly)', fontsize=16)
    plt.tight_layout(rect=[0, 0.05, 1, 0.96])  # Adjust rect to leave space for the global title and legend

    # Show the plot
    plt.show()
