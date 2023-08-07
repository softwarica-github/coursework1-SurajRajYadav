import tkinter as tk
from tkinter import messagebox
import os
def open_dashboard():
# Function to hide a file
    def hide_file():
        filename = filename_entry.get()
        try:
            os.rename(filename, f".{filename}")
            messagebox.showinfo("Hide File", f"File '{filename}' hidden successfully!")
        except FileNotFoundError:
            messagebox.showerror("Hide File", f"File '{filename}' not found.")

    # Function to unhide a file
    def unhide_file():
        filename = filename_entry.get()
        try:
            os.rename(f".{filename}", filename)
            messagebox.showinfo("Unhide File", f"File '{filename}' unhidden successfully!")
        except FileNotFoundError:
            messagebox.showerror("Unhide File", f"Hidden file '{filename}' not found.")

    # Function to view hidden files
    def view_hidden_files():
        hidden_files = [file for file in os.listdir() if file.startswith(".")]
        if hidden_files:
            messagebox.showinfo("View Hidden Files", "Hidden files:\n" + "\n".join(hidden_files))
        else:
            messagebox.showinfo("View Hidden Files", "No hidden files found.")

    # Function to reset the vault
    def reset_vault():
        hidden_files = [file for file in os.listdir() if file.startswith(".")]
        for file in hidden_files:
            os.remove(file)
        messagebox.showinfo("Reset Vault", "Vault reset successful!")

    # Function to perform the chosen action
    def perform_action():
        action = selected_action.get()

        if action == 1:
            hide_file()
        elif action == 2:
            unhide_file()
        elif action == 3:
            view_hidden_files()
        elif action == 4:
            window.destroy()
        elif action == 5:
            reset_vault()

    # Create the main window
    window = tk.Tk()
    window.title("File Vault")
    window.config(bg='skyblue')

    # Set the window size and position
    window.geometry("700x400")
    window.resizable(False, False)

    # Create labels and entry field for the filename
    filename_label = tk.Label(window, text="Enter filename:")
    filename_label.pack()
    filename_entry = tk.Entry(window)
    filename_entry.pack()

    # Create checkboxes for different options
    selected_action = tk.IntVar()

    hide_checkbox = tk.Radiobutton(window, text="Hide a file", variable=selected_action, value=1)
    hide_checkbox.pack()

    unhide_checkbox = tk.Radiobutton(window, text="Unhide a file", variable=selected_action, value=2)
    unhide_checkbox.pack()

    view_checkbox = tk.Radiobutton(window, text="View hidden files", variable=selected_action, value=3)
    view_checkbox.pack()

    exit_checkbox = tk.Radiobutton(window, text="Exit", variable=selected_action, value=4)
    exit_checkbox.pack()

    reset_checkbox = tk.Radiobutton(window, text="Reset the vault", variable=selected_action, value=5)
    reset_checkbox.pack()

    # Create the perform action button
    action_button = tk.Button(window, text="Perform Action", command=perform_action)
    action_button.pack()

    # Run the main window's event loop
    window.mainloop()
