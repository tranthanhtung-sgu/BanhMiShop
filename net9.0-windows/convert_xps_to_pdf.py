import fitz  # PyMuPDF
import sys

# Get input and output file paths from command line arguments
if len(sys.argv) != 3:
    print("Usage: python convert_xps_to_pdf.py <input_xps_path> <output_pdf_path>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

try:
    # Open the XPS document
    xps_doc = fitz.open(input_path)

    # Create a new empty PDF document
    pdf_doc = fitz.open()

    # Loop through all pages in the XPS file
    for page in xps_doc:
        # Render each page as an image (rasterize)
        pix = page.get_pixmap(dpi=100)  # 200 DPI gives good quality
        rect = fitz.Rect(0, 0, pix.width, pix.height)

        # Create a new one-page PDF and insert the image
        page_pdf = pdf_doc.new_page(width=pix.width, height=pix.height)
        page_pdf.insert_image(rect, pixmap=pix)

    # Save to PDF
    pdf_doc.save(output_path)

    # Close files
    xps_doc.close()
    pdf_doc.close()

    print("SUCCESS: Conversion completed:", output_path)
    
except Exception as e:
    print(f"ERROR: Conversion failed: {str(e)}")
    sys.exit(1)