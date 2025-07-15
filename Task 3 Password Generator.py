from tkinter import *
from tkinter import messagebox
import random
import string

def generate_pass():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Invalid Input", "Length must be at least 4 for a strong password.")
            return

        use_special = special_var.get()

        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        punctuation = random.choice(string.punctuation) if use_special else random.choice(string.ascii_letters)

        pool = string.ascii_letters + string.digits + (string.punctuation if use_special else "")
        remaining = [random.choice(pool) for _ in range(length - 4)]

        password_list = list(lower + upper + digit + punctuation + ''.join(remaining))
        random.shuffle(password_list)
        password = ''.join(password_list)

        pass_display.delete(0, END)
        pass_display.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

def copy_pass():
    password = pass_display.get()
    if password:
        win.clipboard_clear()
        win.clipboard_append(password)
        messagebox.showinfo("Copied", "Password Copied!")
    else:
        messagebox.showerror("Warning", "No password to copy")

# Window Configuration
win = Tk()
win.title("🔐 Secure Password Generator")
win.configure(bg="#2d2d2d")  # Dark background

sys_x = win.winfo_screenwidth()
sys_y = win.winfo_screenheight()
c_x = int(sys_x / 2 - 225)
c_y = int(sys_y / 2 - 160)
win.geometry(f'450x320+{c_x}+{c_y}')
win.resizable(False, False)

# Fonts and styles
LABEL_FONT = ("Segoe UI", 12)
ENTRY_FONT = ("Segoe UI", 12)
BUTTON_STYLE = {"font": ("Segoe UI", 10, "bold"), "bg": "#4caf50", "fg": "white", "bd": 0, "padx": 10, "pady": 6}

# Title
Label(win, text="Secure Password Generator", font=("Segoe UI", 18, "bold"), fg="#ffffff", bg="#2d2d2d").pack(pady=15)

# Frame for length input
frame = Frame(win, bg="#2d2d2d")
frame.pack(pady=5)
Label(frame, text="Password Length:", font=LABEL_FONT, bg="#2d2d2d", fg="white").grid(row=0, column=0, padx=10)
length_entry = Entry(frame, width=5, font=ENTRY_FONT, justify='center')
length_entry.grid(row=0, column=1)

# Special character toggle
special_var = BooleanVar(value=True)
Checkbutton(win, text="Include Special Characters", variable=special_var, bg="#2d2d2d", fg="white", selectcolor="#2d2d2d").pack(pady=5)

# Generate button
Button(win, text="Generate Password", command=generate_pass, **BUTTON_STYLE).pack(pady=12)

# Password display
pass_display = Entry(win, font=("Consolas", 14), width=30, justify='center', bd=2, relief=GROOVE)
pass_display.pack(pady=5)

# Copy button
Button(win, text="Copy to Clipboard", command=copy_pass, bg="#2196f3", fg="white", font=("Segoe UI", 10, "bold"), bd=0, padx=10, pady=6).pack(pady=10)

# Footer
Label(win, text="Crafted with ❤️ using Python + Tkinter", font=("Segoe UI", 8), bg="#2d2d2d", fg="#bbbbbb").pack(side=BOTTOM, pady=10)

win.mainloop()
