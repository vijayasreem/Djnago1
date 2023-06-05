from django.urls import path

urlpatterns = [
    path('configure_jira/', configure_jira, name='configure_jira'),
    path('jira_edit/<int:id>', jira_edit, name='jira_edit'),
    path('jira_delete/<int:id>', jira_delete, name='jira_delete'),
]