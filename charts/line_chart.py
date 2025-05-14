import matplotlib.pyplot as plt
import mplcursors
import pandas as pd
import seaborn as sns

# Load and prepare data

df = pd.read_csv("/Users/adam/Desktop/financial_data_visualization/data/nvda_stock_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)
df['Daily Return'] = df['Close'].pct_change()
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['Volatility'] = df['Daily Return'].rolling(window=20).std()
df.set_index('Date', inplace=True)

amd_df = pd.read_csv("/Users/adam/Desktop/financial_data_visualization/data/amd_stock_data.csv")
amd_df['Date'] = pd.to_datetime(amd_df['Date'])
amd_df = amd_df.sort_values('Date')
amd_df['Daily Return'] = amd_df['Close'].pct_change()
amd_df['Volatility'] = amd_df['Daily Return'].rolling(window=20).std()
amd_df['MA20'] = amd_df['Close'].rolling(window=20).mean()
amd_df['MA50'] = amd_df['Close'].rolling(window=50).mean()

def plot_line_chart(df, x_col, y_col):
    plt.close('all') 

    fig, ax = plt.subplots(figsize=(10, 5))

    line, = ax.plot(df[x_col], df[y_col], marker='o', markersize=3, linestyle='-', linewidth=1)
    ax.set_title("Closing Price over Time")
    ax.set_xlabel(x_col)
    ax.set_ylabel("Closing Price")
    ax.grid(True)
    fig.tight_layout()

    cursor = mplcursors.cursor(line, hover=True)

    @cursor.connect("add")
    def on_hover(sel):
        index = int(sel.index)
        date = df[x_col].iloc[index].strftime("%b %d, %Y")
        price = f"{df[y_col].iloc[index]:.2f}"
        sel.annotation.set_text(f"{date}\n{y_col}: ${price}")
        sel.annotation.set_fontsize(9)
        sel.annotation.get_bbox_patch().set(fc="#f4f4f4", ec="#333333", alpha=0.9)

    plt.show()

def plot_closing_price(ax, canvas, df):
    ax.clear()
    ax.plot(df.index, df['Close'], label='Close Price', color='#2a9df4')
    ax.set_title("NVIDIA Closing Price Over Time", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()
    canvas.draw()

def plot_moving_averages(ax, canvas, df):
    ax.clear()
    ax.plot(df.index, df['Close'], label='Close Price', alpha=0.4)
    ax.plot(df.index, df['MA20'], label='20-Day MA', color='#f39c12')
    ax.plot(df.index, df['MA50'], label='50-Day MA', color='#27ae60')
    ax.set_title("Moving Averages", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()
    canvas.draw()

def plot_daily_returns(ax, canvas, df):
    ax.clear()
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True, color='#8e44ad', ax=ax)
    ax.set_title("Histogram of Daily Returns", fontsize=14)
    ax.set_xlabel("Daily Return")
    canvas.draw()

def plot_volatility(ax, canvas, df):
    ax.clear()
    ax.plot(df.index, df['Volatility'], label='20-Day Volatility', color='#e74c3c')
    ax.set_title("Volatility Over Time", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility")
    ax.legend()
    canvas.draw()

def plot_volume(ax, canvas, df):
    
    ax.clear()
    ax.bar(df.index, df['Volume'], color='darkred')

    ax.set_title("Trading Volume Over Time", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Volume")

    import matplotlib.ticker as mticker
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

    canvas.draw()


def generate_chart(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='#2a9df4', marker='o', markersize=3)
    plt.title("NVIDIA Closing Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/line_chart.png")
    plt.close()

def plot_nvda_vs_amd(ax, canvas, nvda_df, amd_df):
    merged = pd.merge(
        nvda_df.reset_index()[['Date', 'Close', 'MA20', 'MA50']],
        amd_df[['Date', 'Close', 'MA20', 'MA50']],
        on='Date',
        suffixes=('_NVDA', '_AMD')
    )

    ax.clear()
    ax.plot(merged['Date'], merged['Close_NVDA'], label='NVIDIA (Close)', color='#2a9df4', linewidth=2)
    ax.plot(merged['Date'], merged['MA20_NVDA'], label='NVIDIA MA20', linestyle='--', color='#2a9df4', alpha=0.7)
    ax.plot(merged['Date'], merged['MA50_NVDA'], label='NVIDIA MA50', linestyle=':', color='#2a9df4', alpha=0.5)

    ax.plot(merged['Date'], merged['Close_AMD'], label='AMD (Close)', color='#d62728', linewidth=2)
    ax.plot(merged['Date'], merged['MA20_AMD'], label='AMD MA20', linestyle='--', color='#d62728', alpha=0.7)
    ax.plot(merged['Date'], merged['MA50_AMD'], label='AMD MA50', linestyle=':', color='#d62728', alpha=0.5)

    ax.set_title("NVIDIA vs AMD: Closing Prices with Moving Averages", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()
    canvas.draw()


if __name__ == "__main__":
    plot_line_chart(df.reset_index(), 'Date', 'Close')
