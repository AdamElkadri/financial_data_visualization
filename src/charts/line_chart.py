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
