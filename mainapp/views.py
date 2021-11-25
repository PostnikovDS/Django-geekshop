from django.shortcuts import render


def index(request):
    context = {'title': 'ололо Магазин'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'ололо Каталог'}
    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')
# Create your views here.

def context(request):
    context = {
        'title': 'test context',
        'header': 'Добро пожаловать на сайт',
        'username': 'Джон',
        'products': [
            {'name': 'Стулья', 'price': 6548},
            {'name': 'Диваны', 'price': 25468},
            {'name': 'Столы', 'price': 14546}
        ]
    }
    return render(request, 'mainapp/test_context.html', context)


def menu(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    return render(request, 'inc_categories_menu.html', links_menu)
