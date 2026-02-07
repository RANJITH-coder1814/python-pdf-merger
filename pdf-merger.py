from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_files, output_file):
    merger = PdfMerger()

    for pdf in pdf_files:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f" File not found: {pdf}")

    merger.write(output_file)
    merger.close()
    print(f"\n PDFs merged successfully into: {output_file}")

def main():
    print(" Python PDF Merger Tool")
    print("Enter PDF file names separated by space")
    
    files = input("PDF Files: ").split()
    output = input("Output file name (e.g. merged.pdf): ")

    merge_pdfs(files, output)

if __name__ == "__main__":
    main()
