from django.forms.widgets import Select

class PictureMCQ(Select):
    template_name = 'widgets/picture_mcq.html'

    def __init__(self, attrs=None, choices=(), picture_url=None):
        super().__init__(attrs, choices)
        self.picture_url = picture_url

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        
        context['widget']['picture_url'] = self.picture_url

        return context
