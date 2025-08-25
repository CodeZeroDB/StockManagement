import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def check_code():
    code = entry.get()
    if code == "1324":
        root.destroy()
        # Ejecuta MainView.py
        main_view_path = os.path.join(os.path.dirname(__file__), "MainView.py")
        if os.path.exists(main_view_path):
            subprocess.Popen([sys.executable, main_view_path])
        else:
            messagebox.showerror("Error", "MainView.py no encontrado.")
    else:
        messagebox.showerror("Login Failed", "Código incorrecto.")

root = tk.Tk()
root.title("Login")
root.geometry("300x150")

tk.Label(root, text="Enter Code:").pack(pady=10)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)
tk.Button(root, text="Login", command=check_code).pack(pady=10)

root.mainloop()