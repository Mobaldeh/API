from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", bolean= True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        fullName = request.form.get('fullName')
        email = request.form.get('email')
        password1= request.form.get('password1')
        password2= request.form.get('password2')
        
        if len(fullName) < 2:
            flash('firstName must be greater than 1 character.', category='error')
        elif len(email) < 4:
            flash('email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('passwords don\'t match.', category='error')

        elif len(password1) < 7:
             flash('password must be atleast 7 characters.', category='error')

        else:
            flash( 'Account Created!', category= 'success')

    return render_template("sign_up.html", bolean= True)


