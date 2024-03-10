from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet
from forms import AddPetForm, EditPetForm

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='abc'

db.init_app(app)

toolbar = DebugToolbarExtension(app)

@app.route('/')
def list_pets():
    pets=Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form=AddPetForm()
    if form.validate_on_submit():
        new_pet=Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('list_pets'))
    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet=Pet.query.get_or_404(pet_id)
    form=EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.commit()
        return redirect(url_for('list_pets'))
    return render_template('edit_pet.html', form=form, pet=pet)

if __name__ == "__main__":
    app.run(debug=True)
