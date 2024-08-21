from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView
# Create your views here


def home_page_view(request):  # new
    context = {  # new
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
        "current_time": datetime.now(),
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["address"] = "Azad Chaiwala Institute Rawalpindi"
        context["phone_number"] = "555-555-5555"
        return context
