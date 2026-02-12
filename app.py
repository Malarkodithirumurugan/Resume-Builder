from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Form lendhu data-va fetch pannrom
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    education = request.form.get('education')
    skills = request.form.get('skills')
    experience = request.form.get('experience')

    # Resume template-ku data-va anuprom
    return render_template('resume.html', 
                           name=name, email=email, phone=phone, 
                           education=education, skills=skills, 
                           experience=experience)

if __name__ == '__main__':
    app.run(debug=True)