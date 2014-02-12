from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Question, Choice
import json
from django.core import serializers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework import renderers
from polls.serializers import ChoiceSerializer, QuestionSerializer
from django.views.decorators.csrf import csrf_exempt,requires_csrf_token
from django.http import Http404

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    #@link(renderer_classes=[renderers.StaticHTMLRenderer])
    #def highlight(self, request, *args, **kwargs):
        #snippet = self.get_object()
        #return HttpResponse(Question.highlighted)

   # def pre_save(self, obj):
        #obj.owner = self.request.user


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
        })
    data = serializers.serialize('json', latest_question_list)
    return HttpResponse(json.dumps(data), content_type="application/json")

    #return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context))

def save_data(request):
    if request.method == 'POST':
        json_data = serializers.deserialize('json',request._body)# simplejson.loads(request.raw_post_data)
        try:
            return HttpResponse("Got json data in post")
        except KeyError:
            return HttpResponse("Malformed data!")
    return HttpResponse("Got json data")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)