from .models import FooterInfo, Menu

def footer(request):
    footer = FooterInfo.objects.all()
    return {'footer': footer}

def spanish_navbar(request):
    categories = Menu.objects.all().order_by('order')
    return {'spanish_categories': categories}

