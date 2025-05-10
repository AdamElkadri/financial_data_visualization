import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from charts.line_chart import (
    df as nvda_df,
    amd_df,
    plot_closing_price,
    plot_moving_averages,
    plot_daily_returns,
    plot_volatility,
    plot_volume,
    plot_nvda_vs_amd
)

# Create main GUI window
root = tk.Tk()
root.title("📊 Stock Visualization App")
root.geometry("1080x700")
root.configure(bg="#f4f4f4")

# Title label
title_label = tk.Label(
    root, text="NVIDIA & AMD Financial Data Charts",
    font=("Segoe UI", 18, "bold"), fg="#333", bg="#f4f4f4", pady=10
)
title_label.pack()

# Button menu frame
menu_frame = tk.Frame(root, bg="#f4f4f4")
menu_frame.pack(pady=10)

# Matplotlib chart area
fig, ax = plt.subplots(figsize=(10.5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Button definitions
button_style = {
    "font": ("Segoe UI", 10, "bold"),
    "bg": "#ffffff",
    "fg": "#333333",
    "activebackground": "#dcdcdc",
    "activeforeground": "#000000",
    "width": 22,
    "relief": tk.RAISED,
    "bd": 1,
    "padx": 5,
    "pady": 5
}

buttons = [
    ("Closing Price", lambda: plot_closing_price(ax, canvas, nvda_df)),
    ("Moving Averages", lambda: plot_moving_averages(ax, canvas, nvda_df)),
    ("Daily Returns", lambda: plot_daily_returns(ax, canvas, nvda_df)),
    ("Volatility", lambda: plot_volatility(ax, canvas, nvda_df)),
    ("Volume", lambda: plot_volume(ax, canvas, nvda_df)),
    ("Compare NVDA vs AMD", lambda: plot_nvda_vs_amd(ax, canvas, nvda_df, amd_df)),
]

# Create and display buttons
for text, cmd in buttons:
    tk.Button(menu_frame, text=text, command=cmd, **button_style).pack(side=tk.LEFT, padx=10)

# Show default chart on startup
plot_closing_price(ax, canvas, nvda_df)

# Start GUI loop
root.mainloop()