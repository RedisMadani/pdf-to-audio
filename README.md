# PDF to Audio Converter

This Python script allows you to convert a PDF file into an audio file using Google Text-to-Speech (gTTS) library and PyPDF2.

## Prerequisites

Make sure you have the following libraries installed:

- [gtts](https://pypi.org/project/gTTS/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Usage

1. Place the PDF file (named `name.pdf`) in the same directory as this script.

2. Run the script using the command:

   ```bash
   python pdf_to_audio.py
   ```

3. The script will extract text from each page of the PDF and combine them into a single text string.

4. It will then use the Google Text-to-Speech library to convert the text into an audio file.

5. The resulting audio file (`Audio.mp3`) will be saved in the same directory.

## Note

- If you encounter any issues with reading or extracting text from the PDF, please make sure that the PDF is not password-protected or corrupted.
## License

This script is released under the [MIT License](/link/to/license).
