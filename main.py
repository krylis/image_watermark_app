from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


def get_image_file():
    filepath = filedialog.askopenfilename()
    image = Image.open(filepath)
    resized_image = image.resize((350, 300))
    photo = ImageTk.PhotoImage(resized_image)
    img_label.config(image=photo)
    img_label.image = photo


def add_watermark():
    pass


root = Tk()
root.title("Image Watermarking Application")
root.geometry('600x450')

mainframe = ttk.Frame(root, padding=(10, 15))
mainframe.pack()

img_label = ttk.Label(mainframe, text='Your Image Here', relief='groove', borderwidth=1, padding=(10, 5))
img_label.pack(pady=5)

choose_img_btn = ttk.Button(mainframe, text='Select Image', command=get_image_file)
choose_img_btn.pack(pady=5)

watermark_text = StringVar()
watermark_entry = ttk.Entry(mainframe, textvariable=watermark_text)
watermark_entry.pack(pady=5)

add_watermark_btn = ttk.Button(mainframe, text='Add Text Watermark', command=add_watermark)
add_watermark_btn.pack(pady=5)

root.mainloop()