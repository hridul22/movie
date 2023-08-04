from . import views
from django.urls import path, include
app_name='avgapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('avenger/<int:avg_id>/',views.details,name='details'),
    path('add/',views.add_hero,name='add_hero'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]