from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = "thanks.html"


class HomePage(TemplateView):
    template_name = "base.html"

class ContactPage(TemplateView):
    template_name = "contact.html"

class AboutHtml(TemplateView):
    template_name = "about.html"