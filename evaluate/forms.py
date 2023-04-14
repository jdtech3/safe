from django.forms import Form, CharField, ChoiceField, Textarea
from django.templatetags.static import static

from .widgets import PictureMCQ, VideoMCQ

class SafetyQuizForm(Form):
    first_name = CharField(label='First name', max_length=100, disabled=True)
    last_name = CharField(label='Last name', max_length=100, disabled=True)

    MCQ_CHOICES = [
        ('-', '-'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    q_fire_hazard = ChoiceField(label='1. Which pictogram indicates that an object may be a fire hazard?', 
                                choices=MCQ_CHOICES, 
                                widget=PictureMCQ(picture_url=static('evaluate/assets/q_fire_hazard.png')))
    
    q_env_hazard = ChoiceField(label='2. The image below represents what type of safety hazard?', 
                               choices=MCQ_CHOICES, 
                               widget=PictureMCQ(picture_url=static('evaluate/assets/q_env_hazard.png')))
    
    FIRE_EXTINGUISHER_CHOICES = [
        ('-', '-'),
        ('A', '0-2 ft'),
        ('B', '3-5 ft'),
        ('C', '6-8 ft'),
        ('D', '9-11 ft'),
    ]
    q_fire_extinguisher = ChoiceField(label='3. Watch the video. How far should you be from the fire when using a fire extinguisher?',
                                      choices=FIRE_EXTINGUISHER_CHOICES,
                                      widget=VideoMCQ(youtube_id='lUojO1HvC8c'))
    
    PASS_ACRONYM_CHOICES = [
        ('-', '-'),
        ('A', 'Pray And Succumb Silently'),
        ('B', 'Pull Aim Squeeze Sweep'),
        ('C', 'Please Always Stand Still'),
        ('D', 'Post All Snapchat Stories'),
    ]
    q_pass_acronym = ChoiceField(label='4. From the video, what does the acronym P.A.S.S stand for?', choices=PASS_ACRONYM_CHOICES)

    q_list_ppe = CharField(label='5. List three pieces of personal protective equipment (PPE) in the lab.', widget=Textarea(attrs={'rows': 3, 'cols': 20}))
