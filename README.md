# SendToPdfMerger
merge multiple PDF files into one from "Send-to" in Windows Explorer

Python must be installed. 
Get it here: https://www.python.org/downloads/

# HowTo
1. In Windows CMD or PowerShell execute: "pip install PyPDF2" to install needed PDF libraries.
2. copy "merge_pdfs.py" to any directory where you want to install.
3. Right-click on "merge_pdfs.py".
4. Select "Create shortcut".
5. Press Win + R to open the Run dialog.
6. Type "shell:sendto" and press Enter. This will open the "Send to" folder.
7. Move the shortcut you created to this folder.
8. Rename as you like. Example: "Merge PDFs".

Done

# Info
- select PDFs in Explorer, then right-click and select "Send to" -> "your shortcut name"
- Files not ending with ".pdf" will be ignored.
- the order that you click on pdf files to select will be the order in the merged pdf. 

Result: YYYY-MM-DD-HH-MM-SS-merged.pdf

have fun ....

# License and Copyright
This is free software.
