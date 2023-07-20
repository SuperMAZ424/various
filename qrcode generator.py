import qrcode
from PIL import ImageTk
import tkinter as tk


link = input("Enter the link: ")

img = qrcode.make(link)


def gen_photo(image):
    root = tk.Tk()
    # Convert the image to a PhotoImage object
    photo = ImageTk.PhotoImage(image)
    root.photo = photo

    # Create a Tkinter window and a label widget to display the image
    label = tk.Label(root, image=photo)
    label.pack()

    # Start the Tkinter event loop
    root.mainloop()

gen_photo(img)