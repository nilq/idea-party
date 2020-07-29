from django import forms
from ideas.models import Idea

from ideas.helpers import give_me_id

import random

class IdeaForm(forms.ModelForm):
    class Meta():
        model = Idea
        fields = ('title', 'pitch')