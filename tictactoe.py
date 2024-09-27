import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")
arr = [[0] * 3 for _ in range(3)]
count = 0


def mark(row, col):
    if arr[row][col] == "":
        if count % 2 == 0:
            arr[row][col] = "x"
            tk.Button[row][col].config(text="X")
        else:
            arr[row][col] = "o"
            tk.Button[row][col].config(text="O")
    else:
        print("it is occupied")


def result():
    button = [
        (0, 1, mark(0, 1))(0, 2, mark(0, 2))(1, 0, mark(1, 0))(1, 1, mark(1, 1))(
            1, 2, mark
        )(2, 0, mark)(2, 1, mark)(2, 2, mark)
    ]


for row, col, cmd in button:
    tk.Button(root, text="", padx=50, pady=50, command=cmd).grid(row=row, column=col)

root.mainloop()
