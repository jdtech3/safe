from django.forms import Form, CharField


class SafetyQuizForm(Form):
    first_name = CharField(label='First name', max_length=100)
    last_name = CharField(label='Last name', max_length=100)
