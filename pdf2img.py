import os
from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog, messagebox
from tqdm import tqdm

def select_pdfs():
    """Open file dialog to select PDF files."""
    return list(filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")]))

def select_output_folder():
    """Open dialog to select an output folder."""
    return filedialog.askdirectory()

def convert_pdfs_to_images(pdf_files, output_folder):
    for pdf in tqdm(pdf_files, desc="Converting PDFs to images", unit="file"):
        try:
            images = convert_from_path(pdf, poppler_path=r"D:\Templates\Python\poppler-24.08.0\Library\bin")
            base_name = os.path.splitext(os.path.basename(pdf))[0]
            for i, img in enumerate(images):
                # Convert image to RGB mode if it isn't already (necessary for JPG)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                img_path = os.path.join(output_folder, f"{base_name}_page_{i+1}.jpg")
                img.save(img_path, "JPEG", quality=95)  # Note: Using "JPEG" not "JPG"
        except Exception as e:
            print(f"Failed to convert {pdf}: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    
    pdf_files = select_pdfs()
    if not pdf_files:
        messagebox.showerror("Error", "No PDF files selected!")
        return
    
    output_folder = select_output_folder()
    if not output_folder:
        messagebox.showerror("Error", "No output folder selected!")
        return
    
    convert_pdfs_to_images(pdf_files, output_folder)
    messagebox.showinfo("Success", f"Images saved in: {output_folder}")

if __name__ == "__main__":
    main()
