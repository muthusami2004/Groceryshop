from django.urls import path
from myapp import views 
from django.urls import path
from . import views





urlpatterns = [
    path('',views.index_page,name='index'),
    path('signup/',views.sign_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('main/',views.main_page,name='main'),
    path('logout/',views.logout_page,name='logout'),
    path('viewDetail/',views.viewDetail,name='viewDetail'),
    path('search/',views.search,name='search'),
    path('addFeedback/<int:id>',views.addfeedback,name='addFeedback'),
    path('updateFeedback/<int:id>',views.updateFeedback,name='updateFeedback'),
    path('delete_Feedback/<int:id>',views.delete_feedback,name='delete_Feedback'),
    path('addToCart/<int:id>',views.addToCart,name='addToCart'),
    path('viewCart/',views.ViewCart,name='viewCart'),
    path('InQty/<int:id>',views.InQty,name='InQty'),
    path('DeQty/<int:id>',views.DeQty,name='DeQty'),
    path('DeleteCart/<int:id>',views.DeleteCart,name='DeleteCart'),
    path('checkout/',views.checkout,name='checkout'),
    path("checkoutbilling/", views.checkoutbilling, name="checkoutbilling"),
    
    

    
    

    
    


    

]