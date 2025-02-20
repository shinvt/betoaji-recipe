"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path,include
from recipes import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from donate import views as donate_views


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),

    re_path(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    re_path(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    re_path(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    re_path(r'^recipes/$', views.RecipeListView.as_view(), name='recipes'),
    re_path(r'^recipes/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
    re_path(r'^recipes/(?P<pk>\d+)/like/$', views.recipe_like, name='recipe_like'),
    re_path(r'^recipes/new/$', views.new_recipe, name='new_recipe'),
    re_path(r'^recipes/filter_by_user/$', views.filter_by_user, name='user_recipes'),
    re_path(r'^recipes/favorite/$', views.liked_by_user, name='favorite_recipes'),
    re_path(r'^recipes/edit/(?P<pk>\d+)/$',views.RecipeUpdateView.as_view(),name='edit_recipe'),

    re_path(r'^donation/$', donate_views.donation, name='donation'),
    re_path(r'^donation/update_chart$', donate_views.update_chart, name='donation_chart'),
    re_path(r'^donation/charge$', donate_views.charge, name='charge'),
    re_path(r'^donation/success$',  donate_views.charge_success, name='charge_success'),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
