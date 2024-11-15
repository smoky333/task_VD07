from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import EditProfileForm

# Объявляем Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        flash('Профиль успешно обновлен!', 'success')
        return redirect(url_for('main.edit_profile'))
    return render_template('edit_profile.html', form=form)


