from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobilis/<int:car_id>/', views.automobilis_detail, name='automobilis_detail'),
    path('uzsakymai/', views.OrderListView.as_view(), name='uzsakymai'),
    path('uzsakymas/<uuid:order_id>/', views.order_detail, name='order_detail'),
    path('uzsakymas/<uuid:order_id>/', views.order_detail, name='order-detail'),
    path('search/', views.search, name='search'),
    path('mano_uzsakymai/', views.KlientoUzsakymuSarasas.as_view(), name='mano-uzsakymai'),
    path('mano_uzsakymai/<uuid:pk>', views.KlientoUzsakymas.as_view(), name='mano-uzsakymas'),
    path('mano_uzsakymai/new', views.OrderByUserCreateView.as_view(), name='mano-uzsakymas-new'),
    path('mano_uzsakymai/<uuid:pk>/update', views.OrderByUserUpdateView.as_view(), name='mano-uzsakymas-update'),
    path('mano_uzsakymai/<uuid:pk>/delete', views.OrderByUserDeleteView.as_view(), name='mano-uzsakymas-delete'),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),
    path('i18n/', include('django.conf.urls.i18n')),

]


