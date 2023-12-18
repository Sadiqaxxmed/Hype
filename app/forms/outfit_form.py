from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired
from app.models import Outfit

class OutfitForm(FlaskForm):
    description       = StringField('Description', validators=[DataRequired()])
    outfitPrice       = IntegerField('OutfitPrice', validators=[DataRequired()])
    image             = FileField('Image', validators=[FileRequired()])  
    catagory          = StringField('Catagory', validators=[DataRequired()])
    owner_id          = IntegerField('Owner_id', validators=[DataRequired()])
