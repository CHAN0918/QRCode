import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

# Function to generate QR Code
def generate_qr():
    data = entry_link.get()
    name = entry_filename.get()

    if data == "" or name == "":
        messagebox.showwarning("Input Error", "Please enter both link and image name.")
        return

    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill='black', back_color='white')

    filename = name + ".png"
    image.save(filename)
    messagebox.showinfo("Success", f"QR Code saved as '{filename}'")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x250")

# Link input
tk.Label(root, text="Enter Link:").pack(pady=5)
entry_link = tk.Entry(root, width=40)
entry_link.pack(pady=5)

# File name input
tk.Label(root, text="Image File Name (without .png):").pack(pady=5)
entry_filename = tk.Entry(root, width=40)
entry_filename.pack(pady=5)

# Generate button
btn_generate = tk.Button(root, text="Generate QR Code", command=generate_qr)
btn_generate.pack(pady=20)

# Run the GUI
root.mainloop()
