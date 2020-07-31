from django.shortcuts import render
from django.http import HttpResponse
from ideas.forms import IdeaForm

from ideas.models import Idea

from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from .helpers import give_me_id

import json

@csrf_exempt
def vote(request):
    data = json.loads(request.body)

    if request.method == 'POST':
        print(data)
        idea = Idea.objects.get(id=data['id'])

        if data['up']:
            idea.votes += 1
        else:
            idea.votes -= 1

        idea.save()

        return HttpResponse("updoot machine go brrrrr")

@csrf_exempt
def idea(request):
    data = json.loads(request.body)

    if request.method == 'POST':
        idea_form = IdeaForm(data=data)
    
        if idea_form.is_valid():
            idea = idea_form.save()
            idea.id = give_me_id()
            idea.save()

            Idea.objects.get(id="").delete()

            print(f'Created new idea: {idea.title} #{idea.id}')

        else:
            print(idea_form.errors)

        return HttpResponse({
            'idea': idea_form
        })

    elif request.method == 'GET':
        idea = Idea.objects.get(id=data.id)

        return HttpResponse(json.dumps(idea))

def ideas(request):
    return HttpResponse(serialize('json', Idea.objects.all().reverse()))