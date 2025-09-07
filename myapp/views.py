from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product,Feedback,Cart,Billing
from django.contrib.auth import login,logout,authenticate
from .forms import FeedbackForm
from django.urls import reverse
from django.shortcuts import render
from .models import Product
from django.shortcuts import render


# Create your views here.
def index_page(request):
    return render(request,'index.html')
    
def sign_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
       


        user = User.objects.filter(username = username,email=email)


        if user.exists():
            messages.error(request,"user already exists")
        elif password1 != password2:
            messages.error(request,"password aren't match")  
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,
                                            username=username,
                                            email=email,
                                            password=password1
                                             )   
    

        login(request,user)
        return redirect('main')


    return render(request,'signup.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password1 = request.POST.get("password1")


        user = authenticate(username = username,password = password1)

        if user:
            login(request,user)
            return redirect('main')
        
        else:
            messages.error(request,'email and password are not incorrect')


    return render(request,'login.html')
    
def logout_page(request):
    logout(request)
    return redirect('/')
    


def main_page(request):
    products = Product.objects.all()
    context = {'prods':products}
    return render(request,'main.html',context)




def viewDetail(request):
    product_id = request.GET['id']
    product = Product.objects.get(id=product_id)
    form = FeedbackForm()
    feedback = Feedback.objects.all()
    context={
        'product':product,
        'form':form,
        'feedbacks':feedback

            }
    return render(request,'view_detail.html',context)


def search(request):
    q = request.GET['q']
    products = Product.objects.filter(name__icontains=q)
    context = {'prods':products}
    return render(request,'search_results.html',context)

def addfeedback(request,id):
    product = Product.objects.get(id = id)
    feedbacks = Feedback.objects.all()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            user = request.user
            Feedback.objects.create(
                user = user,
                product=product,
                feedback_msg = comment
            )

            form = FeedbackForm()
        context={
            'product':product,
            'form':form,
            'feedbacks':feedbacks
        }  

    return render(request,'view_detail.html',context)  
    


def updateFeedback(request,id):
        feedback = Feedback.objects.get(id=id)
        product = feedback.product
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                comment = form.cleaned_data['comment']
                feedback.feedback_msg = comment
                feedback.save()
                url = reverse('viewDetail')
                return redirect(f'{url}?id={product.id}')
            

        form = FeedbackForm(initial={'comment':feedback.feedback_msg})

        context={
            'form':form,
            'product':product,
            'feedback':feedback
        }    

        return render(request,'update_feedback.html',context)



def delete_feedback(request,id):
    fb=Feedback.objects.get(id=id)
    prod_id=fb.product.id
    fb.delete()
    url = reverse('viewDetail')
    return redirect(f'{url}?id={prod_id}')


def addToCart(request,id):
    product = Product.objects.get(id=id)
    user = request.user
    item ,created = Cart.objects.get_or_create(product=product,user=user)
    if not created:
        item.quantity+=1
        item.save()
    return redirect("viewCart")     



    
def ViewCart(request):
    user = request.user
    cart_items = Cart.objects.filter(user = user)
    total_price = sum(i.product.price * i.quantity for i in cart_items)
    context ={
        'carts':cart_items,
        'total_price':total_price
    }
    return render(request,'Cart.html',context)


def InQty(request,id):
   item=Cart.objects.get(id=id)
   item.quantity+=1
   item.save()
   return redirect('viewCart')


def DeQty(request,id):
   item=Cart.objects.get(id=id)
   if item.quantity > 1:
       item.quantity-=1
       item.save()
       return redirect('viewCart')
   


def DeleteCart(request,id):
    item=Cart.objects.get(id=id)
    item.delete()
    return redirect('viewCart')



def checkout(request):
    total = request.GET['params']
    return render(request,'checkout.html',{'total_price':total})

def checkoutBilling(request):
    if request.method == "POST":
        Firstname = request.POST.get('first_name')
        Lastname = request.POST.get('last_name')
        Username = request.POST.get('user_name')
        Email = request.POST.get('email')
        Address = request.POSt.get('address') 
        Country = request.POST.get('country')
        State = request.POST.get('state')
        Pincode = request.POST.get('Pincode')
        Payment = request.POST.get('payment')
        TotalAmount = request.POST.get('totalamount')
        Billing.objects.create(Firstname = Firstname,Lastname = Lastname,Username = Username,Email = Email,Address = Address, Country = Country,State = State,Pincode = Pincode,Payment = Payment,TotalAmount = TotalAmount )   
    return render(request,'success.html')  
    
def product_list(request):
    category = request.GET.get('category')
    if category and category != "All":
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})    



def checkoutbilling(request):
    # your logic here
    return render(request, "checkoutbilling.html")




def checkoutbilling(request):
    # You can pass context if needed
    return render(request, "checkoutbilling.html")
