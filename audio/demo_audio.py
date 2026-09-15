from pypdf import PdfReader
from gtts import gTTS

reader=PdfReader("C:\\Users\\MAHESH KUNCHALA\\OneDrive\\Documents\\abstract1 pdf2.pdf")
text=reader.pages[0].extract_text()
print(text)

tts=gTTS(text=text,lang='en')
tts.save('output.mp3')