import pandas as pd

def load_csv_data(filepath):
    try:
        df = pd.read_csv(filepath)

        df['Date'] = pd.to_datetime(df['Date'])

        df = df.sort_values('Date')

        df = df.dropna()

        df = df.reset_index(drop=True)

        df['Daily Change %'] = df['Close'].pct_change() * 100
        df['7-Day MA'] = df['Close'].rolling(window=7).mean()
        df['Price Range'] = df['High'] - df['Low']

        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def load_amd_data(filepath="data/amd_stock_data.csv"):
    try:
        df = pd.read_csv(filepath)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')
        df = df.dropna().reset_index(drop=True)
        df['Daily Return'] = df['Close'].pct_change()
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        df['Volatility'] = df['Daily Return'].rolling(window=20).std()
        return df
    except Exception as e:
        print(f"Error loading AMD data: {e}")
        return None


