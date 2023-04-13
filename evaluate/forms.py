from django.forms import Form, CharField, ChoiceField
from django.templatetags.static import static

from .widgets import PictureMCQ

class SafetyQuizForm(Form):
    first_name = CharField(label='First name', max_length=100, disabled=True)
    last_name = CharField(label='Last name', max_length=100, disabled=True)

    MCQ_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    q_fire_hazard = ChoiceField(label='Which pictogram indicates that an object may be a fire hazard?', 
                                choices=MCQ_CHOICES, 
                                widget=PictureMCQ(picture_url=static('evaluate/assets/q_fire_hazard.png')))
    q_env_hazard = ChoiceField(label='The image below represents what type of safety hazard?', 
                               choices=MCQ_CHOICES, 
                               widget=PictureMCQ(picture_url=static('evaluate/assets/q_env_hazard.png')))
