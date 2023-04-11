from django.forms import *


class SafetyQuizForm(Form):
    first_name = CharField(label='First name', max_length=100)
    last_name = CharField(label='Last name', max_length=100)
    
    # # styles
    # def __init__(self, *args, **kwargs):
    #     super(SafetyQuizForm, self).__init__(*args, **kwargs)

    #     for f in self.visible_fields():
    #         f.field.widget.attrs['class'] = 'form-control'
