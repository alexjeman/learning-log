from django.urls import path

import apps.learning_logs.views as views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new-topic/', views.new_topic, name='new_topic'),
    path('new-entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
