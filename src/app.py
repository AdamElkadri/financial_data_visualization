from data_processing.load_data import load_csv_data
from charts.line_chart import plot_line_chart

# Example usage
data = load_csv_data("data/example_stock_data.csv")

if data is not None:
    plot_line_chart(data, "Date", "Close")
