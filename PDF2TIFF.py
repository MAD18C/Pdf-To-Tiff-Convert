import os
from pdf2image import convert_from_path
from PIL import Image

# Source folder containing PDFs
source_folder = r"E:\Criminal_Justice\Source_Test"

# Destination folder for TIFF images
destination_folder = r"E:\Criminal_Justice\TIFF_Output"
os.makedirs(destination_folder, exist_ok=True)

# Global counter for TIFF filenames
tiff_counter = 1

# Loop through all PDF files in the source folder
for filename in sorted(os.listdir(source_folder)):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(source_folder, filename)
        print(f"Processing: {pdf_path}")

        try:
            # Convert PDF to images
            images = convert_from_path(pdf_path, dpi=300)

            # Save each page as a TIFF with 3-digit numbering
            for image in images:
                output_filename = f"{tiff_counter:03}.tiff"  # e.g., 001.tiff, 002.tiff
                output_path = os.path.join(destination_folder, output_filename)
                image.save(output_path, format='TIFF')
                print(f"Saved: {output_path}")
                tiff_counter += 1

        except Exception as e:
            print(f" Failed to process {filename}: {e}")
