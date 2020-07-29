from django.shortcuts import render
from django.http import HttpResponse
from ideas.forms import IdeaForm

from ideas.models import Idea

from django.core.serializers import serialize

import json

def idea(request, idea_id=None):
    data = json.loads(request.body)

    if request.method == 'POST':
        idea_form = IdeaForm(data=data)
    
        if idea_form.is_valid():
            idea = idea_form.save()

            print(f'Created new idea: {idea.title} #{idea.id}')
        else:
            print(idea_form.errors)

        return HttpResponse({
            'idea': idea_form
        })

    elif request.method == 'GET':
        if idea_id:
            idea = Idea.objects.get(id=idea_id)

            return HttpResponse(json.dumps(idea))

def ideas(request):
    with json.loads(request.body) as r:
        return HttpResponse(serialize('json', Idea.objects.all()[
            r.skip_pages * r.page_count : r.page_count * r.pages
        ]))