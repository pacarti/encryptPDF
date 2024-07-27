import PyPDF2, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pdfFile = open('meetingminutes1.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFile)

pdfWriter = PyPDF2.PdfWriter()

for pageNum in range(len(pdfReader.pages)):
    pdfWriter.add_page(pdfReader.pages[pageNum])

pdfWriter.encrypt('swordfish')

resultPdf = open('encryptedminutes.pdf', 'wb')

pdfWriter.write(resultPdf)

resultPdf.close()