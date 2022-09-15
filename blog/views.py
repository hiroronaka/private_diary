from django.views import generic

from .forms import InquiryForm


class BlogView(generic.TemplateView):
    template_name = "blog.html"

class Inquiry1View(generic.FormView):
    template_name = "inquiry1.html"
    form_class = InquiryForm
