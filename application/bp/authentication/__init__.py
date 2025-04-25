from flask import Blueprint, render_template, redirect, url_for, flash, request
from application.bp.authentication.forms import RegisterForm, LoginForm

authentication = Blueprint('authentication', __name__, template_folder='templates')

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    pass


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    pass


@authentication.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
