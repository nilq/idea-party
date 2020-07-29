from django import forms
from ideas.models import Idea

from ideas.helpers import give_me_id

class IdeaForm(forms.ModelForm):
    id = give_me_id()

    class Meta():
        model = Idea
        fields = ('title', 'pitch')