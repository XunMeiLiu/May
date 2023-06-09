from django.urls import path
from policyengine import views


urlpatterns = [
    path('initialize_starterkit', views.initialize_starterkit),
    path('error_check', views.error_check),
    path('get_autocompletes', views.get_autocompletes),
    path('policy_action_save', views.policy_action_save),
    path('policy_action_remove', views.policy_action_remove),
    path('policy_action_recover', views.policy_action_recover),
    path('role_action_save', views.role_action_save),
    path('role_action_remove', views.role_action_remove),
    path('role_action_users', views.role_action_users),
    path('document_action_save', views.document_action_save),
    path('document_action_remove', views.document_action_remove),
    path('document_action_recover', views.document_action_recover),
    path('disable_integration', views.disable_integration),
]
