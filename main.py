#implement PyPDF2 to my project
from PyPDF2 import PdfMerger

#This project Merge mulitple PDFs to one PDF

#define my input PDFs
pdfs = ['example1.pdf', 'example2.pdf']

merger = PdfMerger()

#adding PDFS to merger
for pdf in pdfs:
    merger.append(pdf)

#create new PDF and set that name
merger.write("result.pdf")
merger.close()