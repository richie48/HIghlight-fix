import fitz  # PyMuPDF

def modify_drawings(source_pdf_path, target_pdf_path, output_pdf_path):
    # Open the source PDF
    source_doc = fitz.open(source_pdf_path)

    # Open the target PDF
    target_doc = fitz.open(target_pdf_path)

    # Iterate through each page in the source PDF
    for source_page_num in range(source_doc.page_count):
        source_page = source_doc[source_page_num]

        # Get drawings on the source page
        source_drawings = source_page.get_drawings()

        # Iterate through each page in the target PDF
        for target_page_num in range(target_doc.page_count):
            target_page = target_doc[target_page_num]

            # Get the corresponding page in the target PDF
            # Assuming that the pages are in the same order in both PDFs
            if target_page_num == source_page_num:

                print(f"presently on page {target_page}\n\n")

                # Iterate through the drawings on the source page
                for source_drawing in source_drawings:
                    # Check if the source drawing has the desired opacity
                    if source_drawing["fill_opacity"] == 0.20000000298023224:
                        # Apply the same highlight to the corresponding region in the target page
                        rect = source_drawing["rect"]
                        highlight = target_page.add_highlight_annot(rect,rect)
                        highlight.info['title'] = "highlight"

    # Save the modified target PDF
    target_doc.save(output_pdf_path)
    target_doc.close()

# Example usage
source_pdf = "The Bash Cookbook.pdf"  # Replace with the path to your source PDF
target_pdf = "bashcookbook.pdf"  # Replace with the path to your target PDF
output_pdf = "output.pdf"  # Replace with the desired output path
modify_drawings(source_pdf, target_pdf, output_pdf)
