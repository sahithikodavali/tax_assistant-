Tax Assistant

 Overview
A Flask-based API to automate tax calculations, extract text from financial documents using OCR, and generate PDF reports.

Setup
1. Clone the repository: https://github.com/sahithikodavali/tax-assistant-.git
2. Install dependencies
pip install -r requirements.txt


3. Run the Flask app:
python tax.py

4. API is now running on `http://127.0.0.1:5000`

Usage
- **Calculate Tax:**  
POST /calculate_tax JSON: { "income": 50000, "deductions": 10000 }

mathematical

- **Extract Text from Image:**  
POST /extract_text (Upload an image file)

- **Generate Tax Report (PDF):**  
POST /generate_report JSON: { "income": 50000, "deductions": 10000 }
