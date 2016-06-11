from .models import FooterInfo, MenuNavbar

def footer(request):
	footer = FooterInfo.objects.all()
	return {'footer': footer}

def navbar(request):
	categories = MenuNavbar.objects.filter(parent__isnull=True)
	return {'categories': categories}
