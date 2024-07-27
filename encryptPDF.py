import PyPDF2, os, sys
from getpass import getpass

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PDFfilenameToOpen = sys.argv[1]

pdfFile = open(PDFfilenameToOpen, 'rb')

pdfFile = open(PDFfilenameToOpen, 'rb')

pdfReader = PyPDF2.PdfReader(pdfFile)

pdfWriter = PyPDF2.PdfWriter()

for pageNum in range(len(pdfReader.pages)):
    pdfWriter.add_page(pdfReader.pages[pageNum])

password = getpass("Type password to encrypt: ")

pdfWriter.encrypt(password)

resultPdfNameBase = PDFfilenameToOpen.split('.pdf')

resultPdfName = resultPdfNameBase[0] + 'Encrypted' + '.pdf'

resultPdf = open(resultPdfName, 'wb')

pdfWriter.write(resultPdf)

resultPdf.close()
