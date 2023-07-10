# Importing Libraries
from gtts import gTTS
from PyPDF2 import PdfReader

# Open PDF file
pdf_File = open('name.pdf', 'rb')

# Create PDF Reader object
pdf_Reader = PdfReader(pdf_File)
count = len(pdf_Reader.pages)  # counts number of pages in pdf
textList = []

# Extracting text data from each page of the PDF file
for i in range(count):
    try:
        page = pdf_Reader.pages[i]
        textList.append(page.extract_text())
    except:
        pass

# Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

# Set language to English (en)
language = 'en'

# Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

# Save as mp3 file
myAudio.save("Audio.mp3")
