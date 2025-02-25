import flask
from flask import Flask, request, jsonify
import pdfkit
import pytesseract
from PIL import Image

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Tax Assistant API!"

# Tax calculation
@app.route('/calculate_tax', methods=['POST'])
def tax_api():
    if not request.is_json:
        return jsonify({"message": "Use a POST request with JSON data (income & deductions)."}), 400

    data = request.json
    income = data.get('income', 0)
    deductions = data.get('deductions', 0)
    tax_due = max(0, income - deductions) * 0.2  # Example tax rate: 20%

    return jsonify({"tax_due": tax_due})

# OCR function to extract text
@app.route('/extract_text', methods=['POST'])
def extract_text():
    file = request.files['file']
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return jsonify({"extracted_text": text})

# Generate PDF report
@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    income = data.get('income', 0)
    deductions = data.get('deductions', 0)
    tax_due = max(0, income - deductions) * 0.2

    report_html = f"""
    <h1>Tax Report</h1>
    <p>Income: {income}</p>
    <p>Deductions: {deductions}</p>
    <p>Tax Due: {tax_due}</p>
    """
    pdfkit.from_string(report_html, 'tax_report.pdf')

    return jsonify({"message": "PDF generated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
