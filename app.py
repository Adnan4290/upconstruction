# app.py
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/services')
def services():
    return render_template('services.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/project')
def project():
    return render_template('projects.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/service-details')
def serviceDetails():
    return render_template('service-details.html')
@app.route('/project-details')
def projectDetails():
    return render_template('project-details.html')
@app.route('/blog-details')
def blogDetails():
    return render_template('blog-details.html')

@app.route('/connect', methods=['POST'])
def connect():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']

        # Save the form data to a file (e.g., data.txt)
        with open('data.txt', 'a') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Phone: {phone}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Message: {message}\n")
            file.write('\n')  # Separate entries with a newline

    return "Success"

@app.route('/contactForm', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Save the form data to a file (e.g., data_contact_form.txt)
        with open('data_contact_form.txt', 'a') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Message: {message}\n")
            file.write('\n')  # Separate entries with a newline
    return "success"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
