from django.shortcuts import render
def home(request):
    # You can add data to the context if needed, e.g., student info or messages
    context = {
        'page_title': 'Student Home',  # Example of passing dynamic data to the template
    }
    
    # Rendering the "student/home.html" template with the context data
    return render(request, "student/home.html", context)

