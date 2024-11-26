import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(expression)
            expression = str(result)
            input_var.set(expression)
        except Exception:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        input_var.set("")
    elif text == "←":
        expression = expression[:-1]
        input_var.set(expression)
    else:
        expression += text
        input_var.set(expression)

root = tk.Tk()
root.title("Calculator")

expression = ""
input_var = tk.StringVar()

entry = tk.Entry(root, textvar=input_var, font="Arial 20 bold", justify="right", bg="white", relief=tk.SUNKEN, bd=5)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

buttons = [
    ("C", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", ".", "=", "←")
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == "C":
            btn = tk.Button(root, text=btn_text, font="Arial 18 bold", relief=tk.RAISED, bd=3)
            btn.grid(row=i+1, column=0, columnspan=2, ipadx=10, ipady=10, sticky="nsew")
        elif btn_text == "%":
            btn = tk.Button(root, text=btn_text, font="Arial 18 bold", relief=tk.RAISED, bd=3)
            btn.grid(row=i+1, column=3, ipadx=10, ipady=10, sticky="nsew")
        else:
            btn = tk.Button(root, text=btn_text, font="Arial 18 bold", relief=tk.RAISED, bd=3)
            btn.grid(row=i+1, column=j, ipadx=10, ipady=10, sticky="nsew")
        btn.bind("<Button-1>", click)


for i in range(6):  
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
