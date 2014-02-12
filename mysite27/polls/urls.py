from django.conf.urls import patterns, url, include
from rest_framework import routers
from polls import views

router = routers.DefaultRouter()
router.register(r'Question', views.QuestionViewSet)
router.register(r'Choice', views.ChoiceViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       #url(r'^$', views.index, name='index'),
                       #url(r'^$', views.save_data, name='save_data'),
                       # ex: /polls/5/
                       #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       # ex: /polls/5/results/
                       #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
                       # ex: /polls/5/vote/
                       #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)