
# views.py
from django.shortcuts import render, redirect
from urllib.parse import quote
from .models import Product,Review,casual,western,kurtis,kids,store,latest
from.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def index(request):
    stor=store.objects.all()
    late= latest.objects.all()
    return render(request, 'index.html', {'stor': stor, 'late': late})

def purchase_product(request, product_id):
    product = Product.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)
def purchase_latest(request, product_id):
    product = latest.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)

def purchased_kidd(request, product_id):
    product = kids.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)


def purchased_kurtis(request, product_id):
    product = kurtis.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)



def purchased_western(request, product_id):
    product = western.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)
def purchased_saree(request, product_id):
    product = Saree.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)

def purchased_lehenga(request, product_id):
    product = Lehenga.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)

def purchased_casual(request, product_id):
    product = casual.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)






from .models import Fabric,Saree,Lehenga
def saree(request):
    sar = Saree.objects.all()
    return render(request, 'saree.html', {'sar': sar})
def kid(request):
    k = kids.objects.all()
    return render(request, 'kids.html', {'k': k})
def kur(request):
    kurti = kurtis.objects.all()
    return render(request, 'kurti.html', {'kurti': kurti})
def casuals(request):
    casu= casual.objects.all()
    return render(request, 'casual.html', {'casu': casu})
def wesdress(request):
    wes= western.objects.all()
    return render(request, 'western.html', {'wes': wes})
def lehen(request):
    l = Lehenga.objects.all()
    return render(request, 'lehenga.html', {'l': l})



def customize(request):
    fabrics = Fabric.objects.all()
    return render(request, 'customize.html', {'fabrics': fabrics})

def customize_product(request, product_id):
    product = Fabric.objects.get(id=product_id)
    message = f"Hi, I would like to buy {product.name} for {product.price}. Here is the image: {product.image}"
    whatsapp_number = "6380543813"  # Replace with your WhatsApp number
    whatsapp_message = quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    return redirect(whatsapp_url)





def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
def blog_view(request):
    # Your view logic here
    return render(request, 'blog.html')




def blog_details_view(request):
    # Your view logic here
    return render(request, 'blog_details.html')

def shopping_cart_view(request):
    # Your view logic here
    return render(request, 'shopping_cart.html')

def checkout_view(request):
    # Your view logic here
    return render(request, 'checkout.html')

def faq_view(request):
    # Your view logic here
    return render(request, 'faq.html')

def register_view(request):
    # Your view logic here
    return render(request, 'register.html')

def login_view(request):
    # Your view logic here
    return render(request, 'login.html')

def about(request):
    # Your view logic here
    return render(request, 'about.html')

from django.shortcuts import render, redirect
from .forms import ReviewForm

def story(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('story')  # Redirect to the appropriate URL after submission
    else:
        form = ReviewForm()
    return render(request, 'story.html', {'form': form,'reviews': reviews})
