from flask import Flask, render_template, request
from rules import diagnose

app = Flask(__name__)

# 1. Main Home Route (Handles initial page visit)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# 2. Diagnosis Route (Handles form submission when user clicks "Diagnose")
@app.route('/diagnose', methods=['POST'])
def handle_diagnosis():
    selected_symptoms = request.form.getlist('symptoms')
    disease_name, precautions_list = diagnose(selected_symptoms)
    
    return render_template(
        'index.html', 
        disease=disease_name, 
        precautions=precautions_list
    )

# 3. Application Entry Point
if __name__ == '__main__':
    app.run(debug=True)