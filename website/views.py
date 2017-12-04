from django.shortcuts import render

# home page
def index(request):
	return render(request, 'website/index.html')

# pet listings
def pets(request):
	return render(request, 'website/pets.html')

# home page
def contact(request):
	return render(request, 'website/contact.html')

# home page
def donate(request):
	return render(request, 'website/donate.html')

# home page
def volunteer(request):
	return render(request, 'website/volunteer.html')

# home page
def team(request):
	return render(request, 'website/team.html')

