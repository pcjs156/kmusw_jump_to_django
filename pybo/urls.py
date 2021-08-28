from django.urls import path, include

from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name = 'pybo'

# base_views.py
base_urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
]

# question_views.py
question_urlpatterns = [
    path('create/', question_views.question_create, name='question_create'),
    path('modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
]

# answer_views.py
answer_urlpatterns = [
    path('create/', answer_views.answer_create, name='answer_create'),
    path('create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
]

# comment_views.py
comment_urlpatterns = [
    path('create/question/<int:question_id>/', comment_views.comment_create_question,
         name='comment_create_question'),
    path('modify/question/<int:comment_id>/', comment_views.comment_modify_question,
         name='comment_modify_question'),
    path('delete/question/<int:comment_id>/', comment_views.comment_delete_question,
         name='comment_delete_question'),
    path('create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
]

# vote_views.py
vote_urlpatterns = [
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
]

urlpatterns = [
    path('', include(base_urlpatterns)),
    path('question/', include(question_urlpatterns)),
    path('answer/', include(answer_urlpatterns)),
    path('comment/', include(comment_urlpatterns)),
    path('vote/', include(vote_urlpatterns)),
]
