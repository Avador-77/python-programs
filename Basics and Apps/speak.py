import pyttsx3
import PyPDF2

pdfFile = open('intro.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
how_many_pages = pdfReader.numPages
#print(how_many_pages)
speaker = pyttsx3.init()
speaker.setProperty("rate", 110)
#rate = speaker.getProperty("rate")
#print(rate)
for num in range(26, how_many_pages):
    from_page = pdfReader.getPage(26)
    page_text = from_page.extractText()
    speaker.say(page_text)
    speaker.runAndWait()