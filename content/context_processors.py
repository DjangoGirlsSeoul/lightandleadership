from .models import FooterInfo

def footer(request):
	footer = FooterInfo.objects.all()
	return {'footer': footer}
