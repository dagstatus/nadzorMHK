import tkinter as tk
from tkinter import ttk
import pandas as pd

root = tk.Tk()
root.title('Надзор')

sample = {"File Name": [f"file_{i}" for i in range(5)],
          'Sheet Name': [f"sheet_{i}" for i in range(5)],
          'Number Of Rows': [f"row_{i}" for i in range(5, 10)],
          'Number Of Columns': [f"col_{i}" for i in range(5)]
          }
df = pd.DataFrame(sample)
cols = list(df.columns)


def treeview_sort_column(tv, col, reverse):
    l = [(tv.item(k)["text"], k) for k in tv.get_children()]  # Display column #0 cannot be set
    l.sort(key=lambda t: t[0], reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


tree = ttk.Treeview(root)
tree.pack()
tree["columns"] = cols
for i in cols:
    tree.column(i, anchor="w")
    tree.heading(i, text=i, anchor='w')

    tree.heading(i, command=lambda: treeview_sort_column(tree, i, False))

for index, row in df.iterrows():
    tree.insert("", 0, text=index, values=list(row))

root.mainloop()
