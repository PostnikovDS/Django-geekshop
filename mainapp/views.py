import json
import os.path
from mainapp.models import Products, ProductCategory
from django.shortcuts import render
from django.templatetags.static import static

module_dir = os.path.dirname(__file__)

links_menu = [
        {'href': 'products_all', 'name': 'Всё!'},
        {'href': 'products_home', 'name': 'Дом))0)'},
        {'href': 'products_office', 'name': 'О-Ф-И-С'},
        {'href': 'products_classic', 'name': 'классика <3'},
    ]

menu = [
    {'href': 'index', 'name': 'главная'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


def index(request):
    context = {'title': 'ололо Магазин'}
    return render(request, 'mainapp/index.html', context)


# def products(request):
#     context = {'title': 'ололо Каталог'}
#     return render(request, 'mainapp/products.html', context)


def products(request, pk=None):
    print(pk)
    # file_path = os.path.join(module_dir, 'fixtures/products.json')
    # products = json.load(open(file_path, encoding='utf-8'))

    # products = [
    #
    #     {'name': 'Стул повышенного качества', 'text': 'Не оторваться', 'img': static('img/product-1.jpg')},
    #     {'name': 'Стул повышенного качества', 'text': 'Не оторваться', 'img': static('img/product-2.jpg')},
    #     {'name': 'Стул повышенного качества', 'text': 'Не оторваться', 'img': static('img/product-3.jpg')},
    #     {'name': 'Стул повышенного качества', 'text': 'Не оторваться', 'img': static('img/product-4.jpg')},
    #     {'name': 'Стул повышенного качества', 'text': 'Не оторваться', 'img': static('img/product-21.jpg')},
    #     {'name': 'Стул повышенного качества', 'text': 'Не оторваться', 'img': static('img/product-11.jpg')},
    # ]

    # content = {
    #     'title': 'Продукт',
    #     'links_menu': links_menu,
    #     'products': products,
    #     'menu': menu,
    # }

    return render(request, 'mainapp/products.html') #, content)


def contact(request):
    return render(request, 'mainapp/contact.html')
# Create your views here.


def main(request):
    title = 'главная'
    product = Products.objects.all()[:4]
    content = {'title': title, 'products': product}
    return render(request, 'mainapp/products.html', content)


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
