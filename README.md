# PDF to Audio Converter

This Python script allows you to convert the text content of a PDF file into an audio file. It utilizes the `PyPDF2` library to extract text from each page of the PDF and the `gTTS` (Google Text-to-Speech) library to generate an audio file in mp3 format.

## Features
- Extracts text data from each page of the input PDF file.
- Converts multiline text to single line text for better audio output.
- Supports multiple languages for text-to-speech conversion.
- Provides the option to adjust the speech speed.

## Installation
1. Make sure you have Python installed on your system (version 3.6 or above).
2. Install the required libraries by running the following command:
   ```
   pip install PyPDF2 gTTS
   ```

## Usage
1. Place the PDF file you want to convert in the same directory as the script file.
2. Update the `pdf_File` variable in the script with the name of your PDF file.
3. Run the script using the following command:
   ```
   python script_name.py
   ```
4. After the script finishes executing, an audio file named "Audio.mp3" will be generated in the same directory.

## Customization
- Language: You can change the language of the generated audio by modifying the `language` variable in the script. Refer to the [gTTS documentation](https://gtts.readthedocs.io/en/latest/) for the list of supported languages.
- Speed: By default, the speech speed is set to `False`, which means it will use the default speed. If you want to slow down the speech, you can set `slow=True` in the `gTTS` function.

## Notes
- The script may not work properly if the PDF file has complex formatting or non-standard fonts.
- In case of any errors during the extraction process, the script will skip the problematic page and continue with the rest.

## Limitations
- The quality of the generated audio depends on the accuracy of the text extraction from the PDF file.
- Long PDF files or files with a large number of pages may take longer to process.

## License
This script is released under the MIT License. Feel free to modify and use it according to your needs.
