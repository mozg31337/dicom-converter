
import os
import argparse
from PIL import Image
import pydicom
import numpy as np

def dicom_to_image(dicom_path, output_path, output_format):
    """Converts a DICOM file to a specified image format (TIFF or PNG)."""
    try:
        # Read the DICOM file
        dicom_file = pydicom.dcmread(dicom_path)

        # Get the pixel data
        pixel_array = dicom_file.pixel_array

        # Normalize the pixel data to 0-255
        pixel_array = pixel_array - np.min(pixel_array)
        if np.max(pixel_array) > 0:
            pixel_array = pixel_array / np.max(pixel_array)
        pixel_array = (pixel_array * 255).astype(np.uint8)

        # Create an image from the pixel data
        image = Image.fromarray(pixel_array)

        # Save the image in the specified format
        image.save(output_path, format=output_format)
        print(f"Successfully converted {dicom_path} to {output_path}")

    except Exception as e:
        print(f"Error converting {dicom_path}: {e}")

def main():
    """Main function to handle command-line arguments and convert DICOM files."""
    parser = argparse.ArgumentParser(description="Convert DICOM images to TIFF or PNG format.")
    parser.add_argument("input_dir", help="Directory containing DICOM files.")
    parser.add_argument("output_dir", help="Directory to save the converted images.")
    parser.add_argument("--format", choices=["tiff", "png"], default="tiff", help="Output image format (tiff or png).")
    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # Convert each DICOM file in the input directory
    for filename in os.listdir(args.input_dir):
        if filename.lower().endswith(".dcm"):
            dicom_path = os.path.join(args.input_dir, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.{args.format}"
            output_path = os.path.join(args.output_dir, output_filename)
            dicom_to_image(dicom_path, output_path, args.format.upper())

if __name__ == "__main__":
    main()
