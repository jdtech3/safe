from django.forms import Form, ChoiceField

class AnalyzeForm(Form):
    VARIABLE_CHOICES = [
        ('-', '-'),
        ('courses', 'Courses'),
        ('marks', 'Quiz scores'),
        ('time-taken', 'Time taken to complete quiz'),
        ('ppe-marks', 'PPE category scores'),
        ('chemicals-marks', 'Chemicals category scores'),
        ('procedures-marks', 'Procedures category scores'),
        ('ppe-incidents', 'PPE category incidents'),
        ('chemicals-incidents', 'Chemicals category incidents'),
        ('procedures-incidents', 'Procedures category incidents'),
    ]

    x_var = ChoiceField(label='Independent (x) variable', choices=VARIABLE_CHOICES)
    y_var = ChoiceField(label='Dependent (y) variable', choices=VARIABLE_CHOICES)
