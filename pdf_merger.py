import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir("./pdfs"):
    if file.endswith(".pdf"):
        print("file: ", file)
        merger.append(f"./pdfs/{file}")
        merger.write("./pdfs/combined.pdf")
    else:
        print("Not a PDF! ->", file)
