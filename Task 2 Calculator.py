import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Oops!")

root = tk.Tk()
root.title("CALCULATOR")
root.configure(bg="#202124")

entry = tk.Entry(root, font=("Courier New", 22), width=22, bd=10, insertbackground="white",
                 bg="#1F1B24", fg="#00FF99", relief="sunken", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=8, pady=15)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
    ('CLEAR',5,0,4)
]

for item in buttons:
    text = item[0]
    row = item[1]
    col = item[2]
    colspan = item[3] if len(item) > 3 else 1

    if text == 'CLEAR':
        cmd = clear
        bg, fg = "#FF3D00", "#FFFFFF"
    elif text == '=':
        cmd = calculate
        bg, fg = "#00B8D4", "#000000"
    else:
        cmd = lambda t=text: press(t)
        bg, fg = "#37474F", "#FFFFFF"

    btn = tk.Button(root, text=text, command=cmd, width=8*colspan, height=2,
                    font=("Courier New", 14, "bold"), bg=bg, fg=fg, relief="raised", bd=4)
    btn.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4)

root.mainloop()
