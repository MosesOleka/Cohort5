from fpdf import FPDF

# Ask for user input
title = input("Enter the title of the PDF: ")
subject = input("Enter the subject of the PDF: ")
body = input("Enter the body text of the PDF: ")

# Create a PDF object
pdf = FPDF()

# Set document information
pdf.set_title(title)
pdf.set_subject(subject)

# Add a page
pdf.add_page()

# Set font and text color
pdf.set_font('Arial', '', 12)
pdf.set_text_color(255, 255, 255) # white

# Set background color for the title section
pdf.set_fill_color(255, 0, 0) # red
pdf.rect(0, 0, pdf.w, 30, 'F')

# Write the title
pdf.cell(0, 10, title, ln=1, align='C')

# Set background color for the body section
pdf.set_fill_color(0, 255, 0) # green
pdf.rect(0, 30, pdf.w, pdf.h-30, 'F')

# Write the body text
pdf.set_xy(10, 40)
pdf.multi_cell(0, 10, body)

# Save the PDF file
pdf.output(title + ".pdf", 'F')