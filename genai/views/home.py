from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from genai.models import User
from genai import db, login_manager

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

@blueprint.route('/style_transfer')
@login_required
def style_transfer():
    return render_template('home/style_transfer.html')

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None
