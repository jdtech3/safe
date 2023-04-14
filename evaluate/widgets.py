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

class VideoMCQ(Select):
    template_name = 'widgets/video_mcq.html'

    def __init__(self, attrs=None, choices=(), youtube_id=None):
        super().__init__(attrs, choices)
        self.youtube_id = youtube_id

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        
        context['widget']['youtube_id'] = self.youtube_id

        return context
