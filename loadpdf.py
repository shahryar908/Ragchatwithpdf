import fitz
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2 
"""def load_pdf():
    root=Tk()
    root.withdraw()
    filepath=askopenfilename(filetypes=[("PDF Files","*.pdf")])
    return filepath"""
def extract_textwithpymupdf(pdf_path):
    doc=fitz.open(pdf_path)
    text=""
    for page in doc:
        text +=page.get_text()
    return text
def extract_text(uploaded_file):
    
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
def save_text(text, pdf_path, output_folder="data"):
    os.makedirs(output_folder, exist_ok=True)
    base_name = os.path.basename(pdf_path).replace(".pdf", ".txt")
    output_path = os.path.join(output_folder, base_name)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"✅ Extracted text saved to: {output_path}")   
"""pdf_path = load_pdf()
    
if pdf_path:
    print(f"📄 Selected PDF: {pdf_path}")
    text = extract_text(pdf_path)
    save_text(text, pdf_path)
else:
    print("❌ No file selected.")    """