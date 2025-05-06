import matplotlib.pyplot as plt
import mplcursors

def plot_line_chart(df, x_col, y_col):
    plt.figure(figsize=(10, 5))

    line, = plt.plot(df[x_col], df[y_col],
                     marker='o', markersize=3,
                     linestyle='-', linewidth=1)

    plt.title(f"{y_col} over {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()

    cursor = mplcursors.cursor(line, hover=True)

    @cursor.connect("add")
    def on_hover(sel):
        index = int(sel.index)
        date = df[x_col].iloc[index].strftime("%b %d, %Y")
        price = f"{df[y_col].iloc[index]:.2f}"

        sel.annotation.set_text(f"{date}\n{y_col}: ${price}")
        sel.annotation.set_fontsize(9)  # ✅ fixed this line
        sel.annotation.get_bbox_patch().set(fc="#f4f4f4", ec="#333333", alpha=0.9)

    plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import seaborn as sns
import numpy as np

# Load and prepare data
df = pd.read_csv("C:\\Users\\HP\\OneDrive\\Desktop\\financial_data_visualization\\src\\charts\\nvda_stock_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)
df.set_index('Date', inplace=True)

# Calculations
df['Daily Return'] = df['Close'].pct_change()
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['Volatility'] = df['Daily Return'].rolling(window=20).std()

sns.set(style="darkgrid")

# Create main window
root = tk.Tk()
root.title("📊 NVIDIA Financial Data Visualization")
root.geometry("1080x700")
root.configure(bg="#f4f4f4")

# Title label
title_label = tk.Label(
    root, text="NVIDIA Financial Data Charts",
    font=("Segoe UI", 18, "bold"), fg="#333", bg="#f4f4f4", pady=10
)
title_label.pack()

# Menu Frame centered
menu_frame = tk.Frame(root, bg="#f4f4f4")
menu_frame.pack(pady=10)

# Chart display area
fig, ax = plt.subplots(figsize=(10.5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Chart functions
def plot_closing_price():
    ax.clear()
    ax.plot(df.index, df['Close'], label='Close Price', color='#2a9df4')
    ax.set_title("NVIDIA Closing Price Over Time", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()
    fig.tight_layout()
    canvas.draw()

def plot_moving_averages():
    ax.clear()
    ax.plot(df.index, df['Close'], label='Close Price', alpha=0.4)
    ax.plot(df.index, df['MA20'], label='20-Day MA', color='#f39c12')
    ax.plot(df.index, df['MA50'], label='50-Day MA', color='#27ae60')
    ax.set_title("Moving Averages", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()
    fig.tight_layout()
    canvas.draw()

def plot_daily_returns():
    ax.clear()
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True, color='#8e44ad', ax=ax)
    ax.set_title("Histogram of Daily Returns", fontsize=14)
    ax.set_xlabel("Daily Return")
    fig.tight_layout()
    canvas.draw()

def plot_volatility():
    ax.clear()
    ax.plot(df.index, df['Volatility'], label='20-Day Volatility', color='#e74c3c')
    ax.set_title("Volatility Over Time", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility")
    ax.legend()
    fig.tight_layout()
    canvas.draw()

def plot_volume():
    ax.clear()
    ax.bar(df.index, df['Volume'], color='#7f8c8d')
    ax.set_title("Trading Volume Over Time", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Volume")
    fig.tight_layout()
    canvas.draw()

# Buttons with modern style
button_style = {
    "font": ("Segoe UI", 10, "bold"),
    "bg": "#ffffff",
    "fg": "#333333",
    "activebackground": "#dcdcdc",
    "activeforeground": "#000000",
    "width": 18,
    "relief": tk.RAISED,
    "bd": 1,
    "padx": 5,
    "pady": 5
}

# Button list
buttons = [
    ("Closing Price", plot_closing_price),
    ("Moving Averages", plot_moving_averages),
    ("Daily Returns", plot_daily_returns),
    ("Volatility", plot_volatility),
    ("Volume", plot_volume),
]

# Create buttons and center them
for text, cmd in buttons:
    btn = tk.Button(menu_frame, text=text, command=cmd, **button_style)
    btn.pack(side=tk.LEFT, padx=10)

# Show the first chart by default
plot_closing_price()

# Run the GUI
root.mainloop()

