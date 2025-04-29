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
