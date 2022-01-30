from django.urls import path
from . import views
# A clean, elegant URL scheme is an important detail in a high-quality web application. 
# Django lets you design URLs however you want, with no framework limitations.

urlpatterns = [
    path('', views.index_view),
    path('frontier',
         views.stock_create_efficient_frontier_view,
         name='frontier'),
    path('calcualteFrontier',
         views.plot_efficient_frontier,
         name='calcualteFrontier'),
    path('saveFrontierData', views.save_stock_entry_view, name='saveFrontierData'),
    path('volatility', views.stock_create_volatility_view),
    path('delete_stock/<stock_id>', views.delete_stock, name='delete-stock'),
    path('showlist', views.showlist, name="showlist")
    # path('calculate_frontier',
    #      views.calculate_frontier,
    #      name='calculate-frontier'),
    # path('add_stock', views.add_stock),
]
