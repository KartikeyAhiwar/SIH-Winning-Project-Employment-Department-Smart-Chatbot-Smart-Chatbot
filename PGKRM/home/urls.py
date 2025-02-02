from django.urls import path, include
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.registration,name='registration'),
    path('login/',views.login_page,name='login_page'),
    path('login1/',views.log_view,name='login_view'),
    path('classify/',views.find_user_view,name='face_login'),
    path('cv_generation',views.cv_generate,name='cv_generate'),
    path('profile/',views.profile,name="profile"),
]