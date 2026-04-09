import os
from pdfminer.high_level import extract_text

def extract_resume_text(file_path):
    """
    Extracts raw text from a PDF file located at file_path.
    
    Args:
        file_path (str): The absolute or relative path to the PDF.
        
    Returns:
        str: Cleaned text from the PDF, or an empty string if an error occurs.
    """
    # 1. Validation: Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} was not found.")
        return ""

    # 2. Validation: Check if it's actually a PDF
    if not file_path.lower().endswith('.pdf'):
        print("Error: Provided file is not a PDF.")
        return ""

    try:
        # 3. Extraction
        # extract_text handles opening and closing the file internally
        text = extract_text(file_path)
        
        # 4. Post-Processing
        # PDFs often have excessive newlines or weird spacing
        if text:
            # Replace multiple newlines with a single one and strip outer whitespace
            cleaned_text = " ".join(text.split())
            return cleaned_text
        
        return ""

    except Exception as e:
        # Catching specific errors is better, but this handles 
        # corrupted PDFs or permission issues.
        print(f"An unexpected error occurred: {e}")
        return ""

# --- Example Usage for Testing in VS Code ---
if __name__ == "__main__":
    # Update this with a sample PDF name in your folder
    example_pdf = "my_resume.pdf" 
    
    resume_content = extract_resume_text(example_pdf)
    
    if resume_content:
        print("Successfully extracted text:")
        print(resume_content[:500]) # Print first 500 characters
    else:
        print("Failed to extract text.")