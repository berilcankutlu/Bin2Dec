import tkinter as tk
import Bin2Dec
from PIL import Image, ImageTk

def convert_dec():
    decimal = int(decimal_entry.get())
    result_label.config(text="Binary equivalent: " + Bin2Dec.dectobin(decimal),font=("Helvetica", 15))

def convert_bin():
    binary = binary_entry.get()
    result_label.config(text="Decimal equivalent: " + str(Bin2Dec.bintodec(binary)),font=("Helvetica", 15))


root = tk.Tk()
root.title("Bin2Dec")
image = Image.open("background.jpg")
background_image = ImageTk.PhotoImage(image)


background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

main_label = tk.Label(root, text="Decimal to Binary/\nBinary to Decimal Converter",font=("Helvetica", 20), background= "#ffd9d8")
main_label.pack(pady=20)

decimal_label = tk.Label(root, text="Enter a decimal number:",font=("Helvetica", 15), background="#ffd3d4")
decimal_label.pack()

decimal_entry = tk.Entry(root)
decimal_entry.pack()

convert_dec_button = tk.Button(root, text="Convert", command=convert_dec,font=("Helvetica", 15))
convert_dec_button.pack(pady=20)

binary_label = tk.Label(root, text="Enter a binary number:",font=("Helvetica", 15), background= "#ffc4ca")
binary_label.pack()

binary_entry = tk.Entry(root)
binary_entry.pack()

convert_bin_button = tk.Button(root, text="Convert", command=convert_bin,font=("Helvetica", 15))
convert_bin_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 15), background="#dbc7d3")
result_label.pack(pady=50)


root.mainloop()
