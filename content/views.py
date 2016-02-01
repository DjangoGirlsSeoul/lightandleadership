from django.shortcuts import render

# Create your views here.
def our_story(request):
    return render(request, 'content/our_story.html', {})
