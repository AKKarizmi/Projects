import os
import shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tqdm import tqdm

def select_images():
    """Select image files manually."""
    return list(filedialog.askopenfilenames(filetypes=[
        ("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff *.PNG *.JPG *.JPEG *.BMP *.TIFF")
    ]))

def select_output_folder(title):
    """Select a folder for output or moved images."""
    return filedialog.askdirectory(title=title)

def convert_images_to_pdfs(image_files, output_folder, moved_images_folder):
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(moved_images_folder, exist_ok=True)

    for image_file in tqdm(image_files, desc="Converting images", unit="file"):
        try:
            img = Image.open(image_file).convert('RGB')
            pdf_name = os.path.splitext(os.path.basename(image_file))[0] + '.pdf'
            pdf_path = os.path.join(output_folder, pdf_name)
            img.save(pdf_path)
            print(f"Created PDF: {pdf_path}")

            moved_image_path = os.path.join(moved_images_folder, os.path.basename(image_file))
            shutil.move(image_file, moved_image_path)
            print(f"Moved image to: {moved_image_path}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

def main():
    root = tk.Tk()
    root.withdraw()

    image_files = select_images()
    if not image_files:
        messagebox.showerror("Error", "No image files selected!")
        return

    output_folder = select_output_folder("Select Output Folder for PDFs")
    if not output_folder:
        messagebox.showerror("Error", "No output folder selected!")
        return

    moved_images_folder = select_output_folder("Select Folder to Move Original Images")
    if not moved_images_folder:
        messagebox.showerror("Error", "No moved-images folder selected!")
        return

    convert_images_to_pdfs(image_files, output_folder, moved_images_folder)
    messagebox.showinfo("Success", f"PDFs saved in: {output_folder}")

if __name__ == "__main__":
    main()
