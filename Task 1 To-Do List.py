import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, f"[ ] {task}")
        task_entry.delete(0, tk.END)
        update_task_count()
    else:
        messagebox.showinfo("Empty Task", "Please type something first!")

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
        update_task_count()
    except:
        messagebox.showinfo("No Selection", "Select a task to delete.")

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        if task.startswith("[ ]"):
            task = task.replace("[ ]", "[✔]")
            task_listbox.delete(index)
            task_listbox.insert(index, task)
    except:
        messagebox.showinfo("No Selection", "Select a task to mark as done.")

def clear_all():
    confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)
        update_task_count()

def update_task_count():
    count = task_listbox.size()
    task_count_label.config(text=f"📝 Total Tasks: {count}")

# Setup main window
root = tk.Tk()
root.title("My daily To-Do List")
root.geometry("500x350")
root.configure(bg="#1e1e2f")

# Entry and label
task_entry = tk.Entry(root, font=("Verdana", 12), width=30)
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack()

tk.Button(button_frame, text="➕ Add", command=add_task, bg="#00b894", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="✅ Done", command=mark_done, bg="#0984e3", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="❌ Delete", command=delete_task, bg="#d63031", fg="white", width=10).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="🧹 Clear All", command=clear_all, bg="#6c5ce7", fg="white", width=10).grid(row=0, column=3, padx=5)

# Listbox with scrollbar 
frame = tk.Frame(root, bg="#1e1e2f")  
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, font=("Courier New", 12), width=60, height=10, yscrollcommand=scrollbar.set, bg="#2d2d3a", fg="white", selectbackground="#636e72")
task_listbox.pack()

scrollbar.config(command=task_listbox.yview)

# Task count label
task_count_label = tk.Label(root, text="📝 Total Tasks: 0", font=("Calibri", 11), bg="#1e1e2f", fg="lightgray")
task_count_label.pack(pady=5)

root.mainloop()
