# -*- coding: utf-8 -*-
import sys
import os
from PyPDF2 import PdfMerger
import datetime

def merge_pdfs(file_paths):
    try:
        # Reverse the passed filenames-array so the item clicked first is the first in resulting PDF
        file_paths.reverse()
    
        # Use the directory of the first selected PDF file as the output directory
        output_directory = os.path.dirname(file_paths[0])
    
        # Get the current timestamp in the desired format
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        # Create the output filename with the timestamp
        output_path = os.path.join(output_directory, f'{timestamp}-merged.pdf')

        pdf_merger = PdfMerger()

        for file_path in file_paths:
            # Check for PDF extension before processing, ignore all other files
            if file_path.endswith(".pdf"):
                try:
                    with open(file_path, 'rb') as pdf_file:
                        pdf_merger.append(pdf_file)
                except FileNotFoundError:
                    print(f"File not found: {file_path}")
                except Exception as e:
                    print(f"Error merging {file_path}: {e}")
            else:
                print(f"Skipping non-PDF file: {file_path}")

        # Write out the merged PDF
        with open(output_path, 'wb') as output_pdf:
            pdf_merger.write(output_pdf)

        print(f"Merged PDF saved as: {output_path}")
    except Exception as e:
        # Log the full stack trace to a log file for debugging
        with open(f'{output_directory}\\pdfmerge-error.log', 'w') as log_file:
            log_file.write(f"Error occurred:\n{str(e)}\n")
        print(f"An error occurred. Check error_log.txt for details.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python merge_pdfs.py <pdf1> <pdf2> ... <pdfN>")
        sys.exit(1)

    input_pdfs = sys.argv[1:]

    merge_pdfs(input_pdfs)

