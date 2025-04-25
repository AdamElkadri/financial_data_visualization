import matplotlib.pyplot as plt

def plot_line_chart(df, x_col, y_col):
    plt.figure(figsize=(10, 5))
    plt.plot(df[x_col], df[y_col])
    plt.title(f"{y_col} over {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
