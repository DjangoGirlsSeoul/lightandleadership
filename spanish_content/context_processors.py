from .models import FooterInfo, Menu, SubMenu

def footer_spanish(request):
	footer_sp = FooterInfo.objects.all()
	return {'footer_sp': footer_sp}

def navbar_spanish(request):
	categories_sp = Menu.objects.all().order_by('order')
	return {'categories_sp': categories_sp}

