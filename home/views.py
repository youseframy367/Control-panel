from django.shortcuts import render, redirect
from .models import Customer ,Supplier ,Order ,ManageStore
from django.http import JsonResponse
from decimal import Decimal, InvalidOperation
from django.core import serializers
def manageStory(request):
    stores = ManageStore.objects.all()  # جلب كل الفروع أو المواقع من قاعدة البيانات
    return render(request, 'dashbord/ManageStore.html', {'location': stores})


def Inventory(request):
    return render(request ,'dashbord/inventory.html')

def dashbord(request):
    return render(request ,'dashbord/dashbord.html')

def creatAcount(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # تأكد إن الإيميل مش موجود قبل كده
        if Customer.objects.filter(email=email).exists():
            return render(request, 'logIn/creatAcount.html', {
                'error': '❌ This email already exists!'
            })

        Customer.objects.create(
            full_name=name,
            email=email,
            password=password  # ⚠️ في مشروع حقيقي استخدم تشفير
        )
        return redirect('login')

    return render(request, 'logIn/creatAcount.html')


def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # نحاول نجيب المستخدم اللي عنده نفس الإيميل
        customer = Customer.objects.filter(email=email).first()

        if customer is None:
            # مفيش إيميل كده
            return render(request, 'logIn/logIn.html', {
                'error': '❌ Email not found!'
            })

        # لو فيه إيميل، نتحقق من الباسورد
        if customer.password != password:
            return render(request, 'logIn/logIn.html', {
                'error': '❌ Wrong password!'
            })

        # لو كله تمام → دخّله على الداشبورد
        request.session['customer_id'] = customer.id
        request.session['customer_name'] = customer.full_name
        return redirect('dashboard')

    # لو الطلب GET (فتح الصفحة فقط)
    return render(request, 'login/login.html')

# الموردين


def add_supplier(request):
    if request.method == 'POST':
        supplier_name = request.POST.get('SupplierName')
        product = request.POST.get('Product')
        category = request.POST.get('Category')
        buying_price = request.POST.get('BuyingPrice')
        contact_number = request.POST.get('ContactNumber')
        email = request.POST.get('Email')
        supplier_type = request.POST.get('Type')

        # ✅ تحقق من أن السعر رقم
        try:
            buying_price = Decimal(buying_price)
        except (InvalidOperation, TypeError):
            suppliers = Supplier.objects.all()
            suppliers_json = serializers.serialize('json', suppliers)
            return render(request, 'dashbord/suppliers.html', {
                'suppliers_json': suppliers_json,
                'error_message': '⚠️ Buying price must be a number!'
            })

        # ✅ إنشاء مورد جديد
        Supplier.objects.create(
            SupplierName=supplier_name,
            Product=product,
            Category=category,
            BuyingPrice=buying_price,
            ContactNumber=contact_number,
            Email=email,
            Type=supplier_type
        )

        return redirect('Suppliers')

    # ✅ لو الطلب GET (عرض الصفحة)
    suppliers = Supplier.objects.all()
    suppliers_json = serializers.serialize('json', suppliers)
    return render(request, 'dashbord/suppliers.html', {'suppliers_json': suppliers_json})


def suppliers_json(request):
    suppliers = Supplier.objects.all()
    suppliers_json = serializers.serialize('json', suppliers)
    return JsonResponse({'suppliers': suppliers_json})


def orders_view(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_id = request.POST.get('product_id')
        category = request.POST.get('category')
        order_value = request.POST.get('order_value')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        buying_price = request.POST.get('buying_price')
        date_of_delivery = request.POST.get('date_of_delivery')

        try:
            order_value = Decimal(order_value)
            buying_price = Decimal(buying_price)
        except (InvalidOperation, TypeError):
            orders = Order.objects.all()
            orders_json = serializers.serialize('json', orders)
            return render(request, 'dashbord/Orders.html', {
                'orders_json': orders_json,
                'error_message': '⚠️ Please enter valid numeric values for prices.'
            })

        Order.objects.create(
            product_name=product_name,
            product_id=product_id,
            category=category,
            order_value=order_value,
            quantity = quantity ,
            unit=unit,
            buying_price=buying_price,
            date_of_delivery=date_of_delivery
        )

        return redirect('orders')

    orders = Order.objects.all()
    orders_json = serializers.serialize('json', orders)
    return render(request, 'dashbord/Orders.html', {'orders_json': orders_json})

def orders_json(request):
    orders = Order.objects.all()
    orders_json = serializers.serialize('json', orders)
    return JsonResponse({'orders': orders_json})