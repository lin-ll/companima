from django.shortcuts import render

# home page
def index(request):
	return render(request, 'website/index.html')

