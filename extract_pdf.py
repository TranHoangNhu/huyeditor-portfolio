import fitz
import os

pdf_path = r"img/Port.pdf"
output_dir = r"img/port-pages"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

doc = fitz.open(pdf_path)
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    # increase resolution
    zoom = 2.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    pix.save(os.path.join(output_dir, f"page_{page_num + 1}.jpg"))

print(f"Extracted {len(doc)} pages.")
