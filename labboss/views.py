from django.views import generic

# Home Page


class Home(generic.TemplateView):
    """
    Displays the home page
    """
    template_name = 'index.html'