from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['titlu', 'continut', 'locatie', 'latitudine', 'longitudine']
        widgets = {
            'latitudine': forms.HiddenInput(),
            'longitudine': forms.HiddenInput(),
        }
