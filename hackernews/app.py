from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username[0].isupper() or not password.isalnum():
            error_message = "Usuario o contraseña inválidos. Asegúrate de que el usuario comience con mayúscula y la contraseña contenga letras y números."
        else:
            return redirect(url_for('login_success'))
    
    return render_template('login.html', error_message=error_message)

@app.route('/login_success')
def login_success():
    return render_template('login_success.html')

if __name__ == '__main__':
    app.run(debug=True)
