from PIL import Image
import os
import shutil

def convert_images_to_individual_pdfs(image_folder, output_folder, moved_images_folder):
    # Ensure the output and moved images folders exist
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(moved_images_folder, exist_ok=True)

    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'bmp', 'BMP', 'tiff', 'TIFF'))]

    if not image_files:
        print("No image files found in the specified folder.")
        return

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        pdf_name = os.path.splitext(image_file)[0] + '.pdf'
        pdf_path = os.path.join(output_folder, pdf_name)

        # Open the image and convert to PDF
        img = Image.open(image_path).convert('RGB')
        img.save(pdf_path)
        print(f"Created PDF: {pdf_path}")

        # Move the original image to the moved images folder
        moved_image_path = os.path.join(moved_images_folder, image_file)
        shutil.move(image_path, moved_image_path)
        print(f"Moved image to: {moved_image_path}")

# Example usage
image_folder_path = './'  # Replace with your images folder path
output_folder_path = './pdfs'  # Replace with your desired output folder path
moved_images_folder_path = './moved_images'  # Replace with your desired moved images folder path

convert_images_to_individual_pdfs(image_folder_path, output_folder_path, moved_images_folder_path)