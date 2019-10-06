from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from genai.models import User
from genai import db, login_manager
import os
import base64

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')

@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists')
            return redirect(url_for('home.signup'))

        # Create new user
        password_hash = generate_password_hash(password, method='sha256')
        new_user = User(email=email, name=name, password=password_hash)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home.login'))

    return render_template('home/signup.html')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Email not found or incorrect password!')
            return redirect(url_for('home.login'))

        login_user(user, remember=remember)
        return redirect(url_for('account.index'))

    return render_template('home/login.html')

@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))

@blueprint.route('/style_transfer', methods=['GET', 'POST'])
@login_required
def style_transfer():
    # Check if we are doing another style transfer operation
    user_image = 'louvre.jpg'
    base_directory = 'genai/static/output'
    user_directory = '/' + current_user.email + '/'
    directory = base_directory + user_directory
    lock_file_path = directory + '_lock'
    user_generated_image_file_path = 'static/output' + user_directory + 'generated_image.jpg'

    is_locked = True if os.path.exists(lock_file_path) else False
    has_user_generated_image = True if os.path.exists('genai/' + user_generated_image_file_path) else False

    if request.method == 'POST' and not is_locked:
        # First, save the user image
        #data = request.get_json()
        print(request)
        #print(request.form['picture'])
        #print(request.args.get('file'))
        #print(data)
        #if data is not None:
            #img_data = data['img']
            #b64_string += '=' * (-len(img_data) % 4)
            #with open(directory + 'test.jpg', 'wb') as image:
                #image.write(base64.decodebytes(b64_string.encode()))

        # Then, tart the style transfer operation
        #import subprocess
        #command = "python neural_trans.py " + directory + " " + user_image + " >/dev/null 2>&1"
        #subprocess.Popen(command, stdout=None, stderr=None, shell=True)
        return render_template('home/style_transfer.html', is_locked=True, has_user_generated_image=False)

    return render_template('home/style_transfer.html', is_locked=is_locked, has_user_generated_image=has_user_generated_image, generated_image=user_generated_image_file_path)

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None
