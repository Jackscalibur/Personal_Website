from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Render the index page of the portfolio.
    """
    return render(request, 'portfolio/index.html')