import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Display courses
def Courses():
    return "\n1. Bachelor of Science in Computer Technology\n2. Bachelor of Science in Office Administration\n3. Bachelor of Science in Business Administration\n4. Bachelor of Criminology\n5. Bachelor of Secondary Education"

# Register students
def create_student():
    def save_student():
        student_name = name_entry.get()
        student_birthday = birthday_entry.get()
        student_origin = origin_entry.get()
        student_address = address_entry.get()
        
        if student_name and student_birthday and student_origin and student_address:
            with open("students.txt", "a") as file:
                file.write(f"{student_name}|{student_birthday}|{student_origin}|{student_address}\n")
            messagebox.showinfo("Success", f"Student '{student_name}' has been registered!")
            registration_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    registration_window = tk.Toplevel(root)
    registration_window.title("Register Student")
    registration_window.config(bg="#f0f0f0")
    
    tk.Label(registration_window, text="Student Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, pady=5, padx=10)
    tk.Label(registration_window, text="Birthday (MM/DD/YYYY):", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, pady=5, padx=10)
    tk.Label(registration_window, text="Origin:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, pady=5, padx=10)
    tk.Label(registration_window, text="Address:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, pady=5, padx=10)

    name_entry = tk.Entry(registration_window, font=("Arial", 12), width=30)
    birthday_entry = tk.Entry(registration_window, font=("Arial", 12), width=30)
    origin_entry = tk.Entry(registration_window, font=("Arial", 12), width=30)
    address_entry = tk.Entry(registration_window, font=("Arial", 12), width=30)

    name_entry.grid(row=0, column=1, pady=5, padx=10)
    birthday_entry.grid(row=1, column=1, pady=5, padx=10)
    origin_entry.grid(row=2, column=1, pady=5, padx=10)
    address_entry.grid(row=3, column=1, pady=5, padx=10)
    
    tk.Button(registration_window, text="Register", command=save_student, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", width=20).grid(row=4, columnspan=2, pady=20)

# Read students
def read_students():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            students = file.readlines()
        if students:
            student_list_window = tk.Toplevel(root)
            student_list_window.title("Registered Students")
            student_list_window.config(bg="#f0f0f0")
            
            tk.Label(student_list_window, text="List of Registered Students", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
            
            for idx, student in enumerate(students, start=1):
                details = student.strip().split("|")
                tk.Label(student_list_window, text=f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Origin: {details[2]}, Address: {details[3]}", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        else:
            messagebox.showinfo("No Students", "No students are registered yet.")
    else:
        messagebox.showerror("Error", "No student data file found.")

# Update student
def update_student():
    def save_updated_student():
        student_idx = int(student_idx_entry.get()) - 1
        new_name = new_name_entry.get()
        new_birthday = new_birthday_entry.get()
        new_origin = new_origin_entry.get()
        new_address = new_address_entry.get()

        if new_name and new_birthday and new_origin and new_address:
            with open("students.txt", "r") as file:
                students = file.readlines()
            
            if 0 <= student_idx < len(students):
                students[student_idx] = f"{new_name}|{new_birthday}|{new_origin}|{new_address}\n"
                with open("students.txt", "w") as file:
                    file.writelines(students)
                messagebox.showinfo("Success", "Student information has been updated!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid student number.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    update_window = tk.Toplevel(root)
    update_window.title("Update Student Information")
    update_window.config(bg="#f0f0f0")
    
    tk.Label(update_window, text="Student Number to Update:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, pady=5, padx=10)
    tk.Label(update_window, text="New Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, pady=5, padx=10)
    tk.Label(update_window, text="New Birthday (MM/DD/YYYY):", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, pady=5, padx=10)
    tk.Label(update_window, text="New Origin:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, pady=5, padx=10)
    tk.Label(update_window, text="New Address:", font=("Arial", 12), bg="#f0f0f0").grid(row=4, column=0, pady=5, padx=10)

    student_idx_entry = tk.Entry(update_window, font=("Arial", 12), width=30)
    new_name_entry = tk.Entry(update_window, font=("Arial", 12), width=30)
    new_birthday_entry = tk.Entry(update_window, font=("Arial", 12), width=30)
    new_origin_entry = tk.Entry(update_window, font=("Arial", 12), width=30)
    new_address_entry = tk.Entry(update_window, font=("Arial", 12), width=30)

    student_idx_entry.grid(row=0, column=1, pady=5, padx=10)
    new_name_entry.grid(row=1, column=1, pady=5, padx=10)
    new_birthday_entry.grid(row=2, column=1, pady=5, padx=10)
    new_origin_entry.grid(row=3, column=1, pady=5, padx=10)
    new_address_entry.grid(row=4, column=1, pady=5, padx=10)

    tk.Button(update_window, text="Update", command=save_updated_student, font=("Arial", 12), bg="#FF9800", fg="white", relief="raised", width=20).grid(row=5, columnspan=2, pady=20)

# Search student
def search_student():
    def search_for_student():
        search_name = search_entry.get().strip().lower()
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as file:
                students = file.readlines()
            found_students = [student for student in students if search_name in student.lower()]
            if found_students:
                result_window = tk.Toplevel(root)
                result_window.title("Search Results")
                result_window.config(bg="#f0f0f0")
                for student in found_students:
                    details = student.strip().split("|")
                    tk.Label(result_window, text=f"Name: {details[0]}, Birthday: {details[1]}, Origin: {details[2]}, Address: {details[3]}", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
            else:
                messagebox.showinfo("No Results", "No students found with that name.")
        else:
            messagebox.showerror("Error", "No student data file found.")

    search_window = tk.Toplevel(root)
    search_window.title("Search Student")
    search_window.config(bg="#f0f0f0")

    tk.Label(search_window, text="Enter student name to search:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
    search_entry = tk.Entry(search_window, font=("Arial", 12), width=30)
    search_entry.pack(pady=10)
    tk.Button(search_window, text="Search", command=search_for_student, font=("Arial", 12), bg="#2196F3", fg="white", relief="raised", width=20).pack(pady=10)

# Main menu window
def menu():
    global root
    root = tk.Tk()
    root.title("School Management Database 2024")
    root.config(bg="#f0f0f0")

    tk.Button(root, text="View Courses", command=lambda: messagebox.showinfo("Courses", Courses()), font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", width=30).pack(pady=10)
    tk.Button(root, text="Register Student", command=create_student, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", width=30).pack(pady=10)
    tk.Button(root, text="View Registered Students", command=read_students, font=("Arial", 14), bg="#2196F3", fg="white", relief="raised", width=30).pack(pady=10)
    tk.Button(root, text="Update Student Information", command=update_student, font=("Arial", 14), bg="#FF9800", fg="white", relief="raised", width=30).pack(pady=10)
    tk.Button(root, text="Search Student", command=search_student, font=("Arial", 14), bg="#2196F3", fg="white", relief="raised", width=30).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, font=("Arial", 14), bg="#f44336", fg="white", relief="raised", width=30).pack(pady=10)

    root.mainloop()

# Start the program
if __name__ == "__main__":
    menu()
