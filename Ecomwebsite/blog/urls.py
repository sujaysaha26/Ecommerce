from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    # Here "<int:id>" is uesd to call it using id, so we can use it by calling by it's id name, after adding here it we have to mention it's id in views.py so that we can use it 
    # in any other places, by just calling it's id, we can get all it's variable declared in models.py
    path("blogpost/<int:id>", views.blogpost, name="blogpost")
]
