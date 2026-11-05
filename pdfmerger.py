import PyPDF2
import os
from pathlib import Path

working_dir = Path('.')
list_of_files_in_working_dir = [f.name for f in working_dir.iterdir() if f.is_file()]
list_of_pdf_files = [i for i in list_of_files_in_working_dir if (i.endswith(".pdf"))]
print("Total Number of Pdf Files in Your Current Directory : ", len(list_of_pdf_files))
print("".center(50))
print(f"Names of Pdf files in Your Current {os.getcwd()} are :{"".center(50)}\n{list_of_pdf_files}")
print("".center(50))
# input("Enter To Continue........")
os.system("Pause")
Merged_pdf = PyPDF2.PdfMerger()

for pdf in list_of_pdf_files:
    with open(pdf, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        Merged_pdf.append(pdf_reader)
        
Merged_pdf.write("merged.pdf")
Merged_pdf.close()