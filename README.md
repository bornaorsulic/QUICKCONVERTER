# QUICK CONVERTER

Welcome to the official documentation for the `QUICK CONVERTER` project! This This Python-based utility empowers you to seamlessly convert files across various formats, enabling effortless transformation between video, audio, text, and image files. The script harnesses the capabilities of several powerful libraries, offering a versatile toolset for format conversion.


## Instalation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all libraries

You can download ffmpeg using git command down below or on the following link [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html). If downloaded from the link it will be install on the computer but if by the git command it will only install in the repository.

```bash
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
pip install pydub
pip install Pillow
pip install reportlab
pip install python-docx
pip install PyMuPDF
``` 

## Usage


Class **`Video`** facilitates the conversion of video files. Supported formats include MP4, MOV, AVI and WMV.

```python
class Video:

    #video: mp4, mov, avi, wmv

    def convert(input_file, output_file):
        try:
            cmd = ['ffmpeg', '-i', input_file, output_file]
            subprocess.run(cmd, check=True)
            print(f"Conversion successful: {input_file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {input_file} to {output_file}: {e}")
        except FileNotFoundError:
            print("ffmpeg command not found. Make sure ffmpeg is installed and in your system's PATH.")
         
``` 
<br/>

Class **`Music`** specializes in audio file conversion, allowing seamless transformation among formats like MP3, WAV and AAC.

``` python 
class Music:

    # music: mp3, wav, aac

    def convert(input_file, output_file):
        x = input_file.split('.')[-1]
        y = output_file.split('.')[-1]   
        audio = AudioSegment.from_file(input_file, format=x)
        audio.export(output_file, format=y)
``` 
<br/>

Class **`Text`** offers capabilities for converting various document formats, including PDFs, DOCX files and TXT.
``` python
class Text:
    
    # text: pdf, docx, txt

    def convert(input_file, output_file):
        extension = input_file.split('.')[-1].lower()
        extension_output = output_file.split('.')[-1].lower()

        if extension == 'pdf':

            if extension_output == 'txt':
                ... pdf -> txt

            if extension_output == 'docx':
                ... pdf -> docx

        elif extension == 'docx':

            if extension_output == 'txt':
                ... docx -> txt
            
            if extension_output == 'pdf':
                ... docx -> pdf

        elif extension == 'txt':

            if extension_output == 'pdf':
                ... txt -> pdf
        
            if extension_output == 'docx':
                ... txt -> docx
``` 
<br/>

Function **`on_drop(event)`**
Purpose: This function is triggered when files are dropped into a widget.
Functionality: Extracts dropped file paths from the event data. Processes each dropped file path by printing the file names and can perform  operations with the dropped files.
``` python
def on_drop(event):
    # Get the dropped files
    files = event.data.split()  # Split the dropped data into a list of files

    # Process each dropped file
    for file in files:
        print(f"File: {file}")

``` 
<br/>

Function **`on_drag_enter(event)`**
Purpose: This function is triggered when a drag event enters the widget.
Functionality: Focuses on the widget when a drag event enters.
``` python
def on_drag_enter(event):
    event.widget.focus_force()
    event.widget.focus_set()

``` 
<br/>

Function **`open_file_dialog()`**
Purpose: Opens a file dialog for selecting a file.
Functionality: Uses filedialog to prompt the user to select a file. Prints the selected file path. Extracts the file name, extension, and filename without extension. Inserts file information into specific entry widgets.
Determines the type of extension selected (text, video, music, image) and creates an option menu based on the selected type.
``` python
def open_file_dialog():
    global file_path, file_name_ext, selected_ext, extension_menu
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")
        file_name = os.path.basename(file_path)
        file_name_no_ext = os.path.splitext(file_name)[0]  # Remove the extension from the filename
        file_name_ext = (os.path.splitext(file_name)[1])[1:].lower()

        entry1.delete(0, tk.END)
        entry1.insert(tk.END, file_name)

        entry2.delete(0, tk.END)
        entry2.insert(tk.END, file_name_no_ext)

    if 'file_name_ext' in globals():
        if file_name_ext in text_extensions:
            selected_ext = text_extensions
        elif file_name_ext in video_extensions:
            selected_ext = video_extensions
        elif file_name_ext in music_extensions:
            selected_ext = music_extensions
        elif file_name_ext in image_extensions:
            selected_ext = image_extensions      
    else:
        selected_ext = text_extensions
    extension_menu.destroy()
    extension_menu = tk.OptionMenu(root, selected_extension, *selected_ext)
    extension_menu.config(font=('Arial', 7), width=5, bg='#f0f3f4')
    extension_menu.place(relx=0.5, rely=0.2, anchor=tk.CENTER, x=308)
``` 
<br/>

Function **`convert_data()`**
Purpose: Converts or processes selected data based on user inputs.
Functionality: Retrieves user inputs from entry boxes and dropdown menu. Generates a new file path based on the input data. Performs conversion or actions based on the selected extension (text, video, music, image) using an external converting module.
``` python
def convert_data():
    # selected_extension = tk.StringVar(root)
    
    input1 = entry1.get()  # Get text from the first input box
    file_path_name, file_path_ext = os.path.splitext(file_path)
    lowercase_input1 = file_path_ext.lower()
    input1 = file_path_name + lowercase_input1

    input2 = entry2.get()
    inputExt = selected_extension.get()  # Get selected extension from the dropdown

    
    new_path = os.path.dirname(file_path)
    print(file_path)
    print(f"Input 1: {input1}")
    print(f"Input 1: {input2}")
    print(f"Selected Extension: {inputExt}")
    # Perform conversion or other actions with the inputs
    
    if inputExt in text_extensions:
        converting.Text.convert(file_path, f'{new_path}\\{input2}.{inputExt}')
    elif inputExt in video_extensions:
        converting.Video.convert(file_path, f'{new_path}\\{input2}.{inputExt}')
    elif inputExt in music_extensions:
        converting.Music.convert(file_path, f'{new_path}\\{input2}.{inputExt}')
    elif inputExt in image_extensions:
        converting.Image.convert(file_path, f'{new_path}\\{input2}.{inputExt}')

``` 
<br/>

Function **`drop(event)`**
Purpose: This function handles dropped files.
Functionality: Retrieves dropped file information and updates entry widgets accordingly. Determines the file extension type (text, video, music, image) and creates an option menu based on the type.
``` python
def drop(event):
    global file_path, file_name_ext, selected_ext, extension_menu
    # This function is called when stuff is dropped into a widget
    file_path = event.data.split()[0]
    file_name = file_path.split('/')[-1]
    file_name_no_ext = os.path.splitext(file_name)[0]
    file_name_ext = (os.path.splitext(file_name)[1])[1:].lower()

    entry1.delete(0, tk.END)
    entry1.insert(tk.END, file_name)

    entry2.delete(0, tk.END)
    entry2.insert(tk.END, file_name_no_ext)

    if 'file_name_ext' in globals():
        if file_name_ext in text_extensions:
            selected_ext = text_extensions
        elif file_name_ext in video_extensions:
            selected_ext = video_extensions
        elif file_name_ext in music_extensions:
            selected_ext = music_extensions
        elif file_name_ext in image_extensions:
            selected_ext = image_extensions      
    else:
        selected_ext = text_extensions
    extension_menu.destroy()
    extension_menu = tk.OptionMenu(root, selected_extension, *selected_ext)
    extension_menu.config(font=('Arial', 7), width=5, bg='#f0f3f4')
    extension_menu.place(relx=0.5, rely=0.2, anchor=tk.CENTER, x=308)

``` 
<br/>

Function **`drag_command(event)`**
Purpose: Prepares for a drag event.
Functionality: Returns drag type, content type, and content at the start of a drag event.
``` python
def drag_command(event):
    # This function is called at the start of the drag,
    # it returns the drag type, the content type, and the actual content
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")

``` 


## How to run

1. Run `gui_tkinter.py` file
2. Select file dialog or drag and drop file 
3. If you want, change the name of the file you want to convert
4. Select the extension you want to change the file to
5. Click `Convert` button and the file will be downloaded

> **_NOTE:_**  Before running the file be sure everything is installed right!

## Contact
If you have any questions, suggestions, or feedback about this project, feel free to reach out:

- **Name**: Borna Oršulić
- **GitHub**: [bornaorsulic](https://github.com/bornaorsulic)
  <br/> <br/>
- **Name**: Luka Taslak
- **GitHub**: [lukataslak](https://github.com/lukataslak)
<br/> <br/>
- Project link: [https://github.com/bornaorsulic/QUICKCONVERTER](https://github.com/bornaorsulic/QUICKCONVERTER)
