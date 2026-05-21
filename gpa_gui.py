import tkinter as tk
from tkinter import ttk, messagebox
from gpa_calculate import calculate_gpa, grades

# List of allowed grades for the dropdown list
ALLOWED_GRADES = list(grades.keys())

BG = "#fde2e4"
root = tk.Tk()
root.title("GPA Calculator")
root.geometry("560x520")
root.resizable(False, False)
root.configure(bg=BG)

rows = [ ]  # stores (grade, credit)

# allow only digits
def valid_number(text):
    if text == "":
        return True
    return text.isdigit()

vcmd = (root.register(valid_number), "%P")

# Title
title = tk.Label(root, text="GPA Calculator", font=("Arial", 18), bg=BG)
title.pack(pady=10)

# Number of courses
top = tk.Frame(root, bg=BG)
top.pack(pady=5)

tk.Label(top, text="How many courses?", bg=BG).pack(side="left", padx=6)
num_entry = tk.Entry(top, width=8, justify="center")
num_entry.pack(side="left", padx=6)

# Table
table = tk.Frame(root, bg=BG)
table.pack(pady=15)

# Result
result_var = tk.StringVar(value="GPA: --")
msg_var = tk.StringVar(value="")

result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), bg=BG)
result_label.pack(pady=5)

msg_label = tk.Label(root, textvariable=msg_var, font=("Arial", 11), bg=BG)
msg_label.pack()

# Functions
def clear_table():
    for w in table.winfo_children():
        w.destroy()
    rows.clear()

def create_courses():
    try:
        n = int(num_entry.get())
        if n <= 0:
            raise ValueError
        if n > 7:
            messagebox.showerror("Error", "Max 7 courses")
            return
    except:
        messagebox.showerror("Error", "Enter a valid number of courses")
        return

    clear_table()

    # Headers
    tk.Label(table, text="Course", bg=BG).grid(row=0, column=0, padx=8)
    tk.Label(table, text="Grade", bg=BG).grid(row=0, column=1, padx=8)
    tk.Label(table, text="Credits", bg=BG).grid(row=0, column=2, padx=8)

    # Rows
    for i in range(1, n + 1):
        tk.Label(table, text=f"Course {i}", bg=BG).grid(row=i, column=0, pady=6)

        grade_var = tk.StringVar(value="A")
        grade_box = ttk.Combobox(
            table,
            textvariable=grade_var,
            values=ALLOWED_GRADES,
            state="readonly",
            width=8
        )
        grade_box.grid(row=i, column=1, pady=6)

        credit_entry = tk.Entry(
            table,
            width=10,
            validate="key",
            validatecommand=vcmd
        )
        credit_entry.grid(row=i, column=2, pady=6)

        rows.append((grade_box, credit_entry))

def calculate():
    if not rows:
        messagebox.showerror("Error", "Press Create first")
        return

    courses = [ ]

    for i, (grade_box, credit_entry) in enumerate(rows, start=1):
        grade = grade_box.get()
        credit_text = credit_entry.get()

        if credit_text == "":
            messagebox.showerror("Error", f"Course {i}: credits is empty")
            return

        try:
            credit = int(credit_text)
            if credit <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", f"Course {i}: invalid credits")
            return

        courses.append((grade, credit))

    gpa, msg = calculate_gpa(courses)
    result_var.set(f"GPA: {gpa:.2f}")
    msg_var.set(msg)

def reset_all():
    num_entry.delete(0, tk.END)
    clear_table()
    result_var.set("GPA: --")
    msg_var.set("")

# Buttons
buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=15)

tk.Button(buttons, text="Create", command=create_courses).pack(side="left", padx=8)
tk.Button(buttons, text="Calculate", command=calculate).pack(side="left", padx=8)
tk.Button(buttons, text="Reset", command=reset_all).pack(side="left", padx=8)

root.mainloop()
