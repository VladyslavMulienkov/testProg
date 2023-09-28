import tkinter as tk

def on_click(text):
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Калькулятор")

# Вікно для вводу та виводу
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Helvetica 20")
entry.grid(row=0, column=0, columnspan=4)

# Кнопки калькулятора
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font="Helvetica 15", command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
