"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
admin.autodiscover()
import users_app.views

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_app.views.index),
    path('add_user', users_app.views.AddUserView.as_view()),
    path('get_user/<int:pk>', users_app.views.GetUserView.as_view()),
    path('edit_user/<int:user_id>', users_app.views.edit_user),
    path('delete_user/<int:user_id>', users_app.views.delete_user),
]



# add_user
# get_user/id
# edit_user/id
# delete_user/id
