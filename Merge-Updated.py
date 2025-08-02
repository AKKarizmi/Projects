import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
from tqdm import tqdm
import sys

def merge_pdfs(pdf_list, output_filename):
    """
    Merge multiple PDF files into one with error handling and password support.
    """
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf in tqdm(pdf_list, desc="Merging PDFs", unit="file"):
        try:
            with open(pdf, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                if reader.is_encrypted:
                    password = input(f"Enter password for {pdf}: ")
                    reader.decrypt(password)
                pdf_merger.append(reader)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Skipping {pdf} due to error: {e}")

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)
    print(f"Merged PDF saved as: {output_filename}")
    pdf_merger.close()

def select_files():
    """Open file dialog to select PDF files."""
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    return list(files)

def select_output():
    """Open file dialog to specify output file."""
    return filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    pdf_files = select_files()
    if not pdf_files:
        messagebox.showerror("Error", "No PDF files selected!")
        return
    
    output_file = select_output()
    if not output_file:
        messagebox.showerror("Error", "No output file selected!")
        return
    
    merge_pdfs(pdf_files, output_file)
    messagebox.showinfo("Success", f"Merged PDF saved as: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf_files = sys.argv[1:-1]
        output_file = sys.argv[-1]
        merge_pdfs(pdf_files, output_file)
    else:
        main()
