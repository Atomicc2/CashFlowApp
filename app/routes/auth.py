from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required
from app import db
from app.models.user import User
from app.forms.auth_forms import RegisterForm, LoginForm

# Criando um blueprint chamado 'auth_bp'
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name_complete=form.name_complete.data,
            nameuser=form.nameuser.data,
            email=form.email.data,
            senha=form.senha.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso! Agora faça o login.', 'success')
        return redirect(url_for('auth.login'))  # <-- Precisa do prefixo do blueprint
    return render_template('auth/register.html', form=form)  # Certifique-se de que o caminho está correto

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nameuser=form.username.data).first()  # Corrigido para 'username'
        if user and user.senha == form.password.data:  # Corrigido para 'password'
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index.index'))  # Redireciona para a página inicial
        else:
            flash('Usuário ou senha incorretos.', 'danger')
    return render_template('auth/login.html', form=form)  # Certifique-se de que o caminho está correto

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado!', 'info')
    return redirect(url_for('auth.login'))
