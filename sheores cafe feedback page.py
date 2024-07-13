import tkinter as tk
from tkinter import messagebox, ttk

# Function to handle the submission of the feedback form
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    branch = branch_var.get()
    rating = entry_rating.get()
    feedback = text_feedback.get("1.0", tk.END)
    
    if name and email and phone and branch and rating and feedback:
        # You can add your logic here to handle the feedback, e.g., save to a database or file
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        branch_var.set(branch_options[0])
        entry_rating.delete(0, tk.END)
        text_feedback.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Create the main application window
app = tk.Tk()
app.title("Sheores Cafe - Feedback and Reviews")
app.geometry("400x600")

# Create and place labels and entry widgets for the feedback form
label_title = tk.Label(app, text="Sheores Cafe Feedback", font=("Helvetica", 16))
label_title.pack(pady=10)

label_name = tk.Label(app, text="Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(app, width=50)
entry_name.pack(pady=5)

label_email = tk.Label(app, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(app, width=50)
entry_email.pack(pady=5)

label_phone = tk.Label(app, text="Phone Number:")
label_phone.pack(pady=5)
entry_phone = tk.Entry(app, width=50)
entry_phone.pack(pady=5)

label_branch = tk.Label(app, text="Branch:")
label_branch.pack(pady=5)
branch_var = tk.StringVar()
branch_options = ["Noida", "Agra", "Lucknow"]
branch_menu = ttk.Combobox(app, textvariable=branch_var, values=branch_options, state='readonly')
branch_menu.set(branch_options[0])
branch_menu.pack(pady=5)

label_rating = tk.Label(app, text="Rating (1-5):")
label_rating.pack(pady=5)
entry_rating = tk.Entry(app, width=5)
entry_rating.pack(pady=5)

label_feedback = tk.Label(app, text="Feedback:")
label_feedback.pack(pady=5)
text_feedback = tk.Text(app, height=10, width=50)
text_feedback.pack(pady=5)

# Create and place the submit button
button_submit = tk.Button(app, text="Submit Feedback", command=submit_feedback)
button_submit.pack(pady=20)

# Run the application
app.mainloop()
