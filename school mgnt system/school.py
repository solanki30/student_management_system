import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.geometry("1350x700+0+0")
win.title("STUDENT MANAGEMENT SYSTEM")

title_label=tk.Label(win,text="STUDENT MANAGEMENT SYSTEM", font=("Arial",30,"bold") ,border=12,relief='groove',bg="yellow")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame=tk.LabelFrame(win,text="ENTER DETAILS",font=("Arial",20),bd=12,relief='groove',bg="yellow")
detail_frame.place(x=20,y=90,width=420,height=575)

data_frame=tk.Frame(win,bd=12,bg="lightgrey",relief='groove')
data_frame.place(x=475,y=90,width=810,height=575)

name_label = tk.Label(detail_frame, text="STUDENT NAME:", font=("Arial", 15), bg="blue")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(detail_frame, font=("Arial", 15))
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Roll Number
roll_label = tk.Label(detail_frame, text="ROLL NUMBER:", font=("Arial", 15), bg="blue")
roll_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
roll_entry = tk.Entry(detail_frame, font=("Arial", 15))
roll_entry.grid(row=1, column=1, padx=10, pady=10)

# Gender (dropdown)
gender_label = tk.Label(detail_frame, text="GENDER:", font=("Arial", 15), bg="blue")
gender_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
gender_combo = ttk.Combobox(detail_frame, font=("Arial", 15), state="readonly")
gender_combo['values'] = ("Male", "Female", "Other")
gender_combo.grid(row=2, column=1, padx=10, pady=10)


# Date of Birth
dob_label = tk.Label(detail_frame, text="DATE OF BIRTH:", font=("Arial", 15), bg="blue")
dob_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
dob_entry = tk.Entry(detail_frame, font=("Arial", 15))
dob_entry.grid(row=3, column=1, padx=10, pady=10)

'''# Add Submit Button (optional)
submit_btn = tk.Button(detail_frame, text="Submit", font=("Arial", 15, "bold"), bg="green", fg="white")
submit_btn.grid(row=4, column=0, columnspan=2, pady=20)'''


table = ttk.Treeview(data_frame, columns=("name", "roll", "gender", "dob"), show="headings")

# Define column headers
table.heading("name", text="NAME")
table.heading("roll", text="ROLL NO.")
table.heading("gender", text="GENDER")
table.heading("dob", text="DOB")

# Set column widths
table.column("name", width=200)
table.column("roll", width=200)
table.column("gender", width=200)
table.column("dob", width=200)

# Add sample data (you'll connect this to form later)
table.insert("", "end")
table.insert("", "end")

# Add scrollbar (optional)
scroll_y = ttk.Scrollbar(data_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scroll_y.set)

scroll_y.pack(side="right", fill="y")
table.pack(fill="both", expand=1)
def add_data():
    name = name_entry.get()
    roll = roll_entry.get()
    gender = gender_combo.get()
    dob = dob_entry.get()
    
    # Check if all fields are filled
    if name and roll and gender and dob:
        table.insert("", "end", values=(name, roll, gender, dob))
        # Optionally clear the form after adding
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        dob_entry.delete(0, tk.END)
        gender_combo.current(0)

submit_btn = tk.Button(detail_frame, text="Submit", font=("Arial", 15, "bold"), bg="green", fg="white", command=add_data)
submit_btn.grid(row=4, column=0, columnspan=2, pady=20)

win.mainloop()