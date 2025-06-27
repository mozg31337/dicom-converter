# DICOM to Image Converter

This Python application converts DICOM (Digital Imaging and Communications in Medicine) xray images to TIFF and PNG formats.

## Features

- Convert DICOM files to TIFF or PNG images.
- Command-line interface for easy use.
- Batch conversion of all DICOM files in a directory.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/dicom-converter.git
   cd dicom-converter
   ```

2. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To convert DICOM images, run the `main.py` script from the command line:

```bash
python main.py <input_directory> <output_directory> [--format <format>]
```

### Arguments

- `input_directory`: The directory containing the DICOM files you want to convert.
- `output_directory`: The directory where the converted images will be saved.
- `--format` (optional): The output image format. Choose between `tiff` (default) and `png`.

### Examples

- **Convert to TIFF (default):**

  ```bash
  python main.py samples output
  ```

- **Convert to PNG:**

  ```bash
  python main.py samples output --format png
  ```

## How It Works

The application uses the following libraries:

- **`pydicom`**: To read the DICOM files and extract the pixel data.
- **`Pillow`**: To create and save the images in the specified format.
- **`numpy`**: To perform numerical operations on the pixel data.

## To-Do

- Add support for more image formats.
- Add a graphical user interface (GUI).
- Improve error handling.
