from .models import FooterInfo, Menu

def footer(request):
	footer = FooterInfo.objects.all()
	return {'footer': footer}

def navbar(request):
	categories = Menu.objects.all().order_by('order')
	return {'categories': categories}
