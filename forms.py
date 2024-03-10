from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, ValidationError

class AddPetForm(FlaskForm):
    name=StringField("Pet Name", validators=[InputRequired()])
    species=SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url=StringField("Photo URL", validators=[Optional(), URL()])
    age=IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes=StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url=StringField("Photo URL", validators=[Optional(), URL()])
    notes=StringField("Notes", validators=[Optional()])
    available=BooleanField("Available")