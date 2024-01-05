import tkinter as tk
from tkinter import filedialog
import tkinterDnD # pip install python-tkdnd
import os

def on_drop(event):
    # Get the dropped files
    files = event.data.split()  # Split the dropped data into a list of files

    # Process each dropped file
    for file in files:
        print(f"File: {file}")

        # Perform operations with the dropped file


def on_drag_enter(event):
    event.widget.focus_force()
    event.widget.focus_set()


def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")
        file_name = os.path.basename(file_path)
        file_name_no_ext = os.path.splitext(file_name)[0]  # Remove the extension from the filename

        entry1.delete(0, tk.END)
        entry1.insert(tk.END, file_name)

        entry2.delete(0, tk.END)
        entry2.insert(tk.END, file_name_no_ext)


def convert_data():
    input1 = entry1.get()  # Get text from the first input box
    input2 = selected_extension.get()  # Get selected extension from the dropdown
    print(f"Input 1: {input1}")
    print(f"Selected Extension: {input2}")
    # Perform conversion or other actions with the inputs


def drop(event):
    global a
    # This function is called when stuff is dropped into a widget
    file_path = event.data.split()[0]
    file_name = file_path.split('/')[-1]
    file_name_no_ext = os.path.splitext(file_name)[0]

    a = os.path.splitext(file_name)[1]
    entry1.delete(0, tk.END)
    entry1.insert(tk.END, file_name)

    entry2.delete(0, tk.END)
    entry2.insert(tk.END, file_name_no_ext)


def drag_command(event):
    # This function is called at the start of the drag,
    # it returns the drag type, the content type, and the actual content
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")


# Create the main window
root = tkinterDnD.Tk()
root.title("Quick Converter")

# text
stringvar = tk.StringVar()
stringvar.set('\n\nChoose a file or drop it here')

# Set the window size to 1000x800 pixels
root.geometry("800x600")

# Set the background color to grey
root.configure(bg="#d6dcdf")



label_tex = tk.Label(root, text='Quick Converter', fg="#333b40", bg='#d6dcdf', font=('Arial', 32))
label_tex.place(relx=0.45, rely=0.12, anchor=tk.SE)

# DND box
label_1 = tk.Label(root, textvar=stringvar, relief="solid", bd=2, bg="#8c9498", font=('Arial', 15))
label_1.place(relx=0.5, rely=1.0, anchor=tk.SE, y=-60, x=350, width=700, height=200)


label_b = tk.Label(root, bg="#4b96ba")
label_b.place(relx=0.5, rely=1.0, anchor=tk.SE, y=160, x=500, width=1000, height=200)


# nesto sta jednostavno treba, gleda oko misa jel dropa u box i tako
label_1.register_drop_target("*")
label_1.register_drag_source("*")
label_1.bind("<<Drop>>", drop)
label_1.bind("<<DragInitCmd>>", drag_command)
label_1.bind('<<DragEnter>>', on_drag_enter)

# FILE DIALOG button
file_button = tk.Button(root, text="Upload",  command=open_file_dialog, relief="solid", bd=2, bg="#f0f3f4", font=('Arial', 14))
file_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=210)

# ljevi box
entry1 = tk.Entry(root, font=('Arial', 16), bg='#f0f3f4')
entry1.place(relx=0.5, rely=0.2, anchor=tk.CENTER, x=-160)
# desni box
entry2 = tk.Entry(root, font=('Arial', 16), bg='#f0f3f4')
entry2.place(relx=0.5, rely=0.2, anchor=tk.CENTER, x=160)

# CONVERT button
convert_button = tk.Button(root, text="Convert", command=convert_data, width=10, bd=3, font=('Arial', 13), bg='#f0f3f4')
convert_button.place(relx=0.5, rely=0.32, anchor=tk.CENTER, x=0)

# Create a Frame widget to simulate a line
line1 = tk.Frame(root, height=5, width=60, bg="#333b40")
line1.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y = 130)

line2 = tk.Frame(root, height=20, width=5, bg="#333b40")
line2.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y = 122, x = -30)

line3 = tk.Frame(root, height=20, width=5, bg="#333b40")
line3.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y = 122, x = 30)

line4 = tk.Frame(root, height=35, width=5, bg="#333b40")
line4.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y = 100)




text_extensions = ['txt', 'pdf', 'docx']
video_extensions = ['mp4', 'mov', 'avi', 'wmv']
music_extensions = ['mp3', 'wav', 'aac']
image_extensions = ['jpg', 'png', 'gif', 'svg', 'bmp', 'tiff', 'webp', 'ico']
a = 'txt'

if a in text_extensions:

    selected_extension = tk.StringVar(root)

    # Create the OptionMenu and add options
    extension_menu = tk.OptionMenu(root, selected_extension, *text_extensions)
    extension_menu.config(font=('Arial', 7), width=5, bg='#f0f3f4')
    extension_menu.place(relx=0.5, rely=0.2, anchor=tk.CENTER, x=308)




# Run the Tkinter event loop
root.mainloop()