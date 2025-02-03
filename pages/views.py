from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = "index.html"
    


class AboutPageView(TemplateView):
    template_name = "about.html"



class ContactView(FormView):
        template_name = 'contact.html'
        form_class = ContactForm
        success_url = '/contact/'
        
        def form_valid(self, form):
            form.save()
            return super().form_valid(form)
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.method == 'POST' and self.form_valid(self.get_form()):
                context['message'] = 'اطلاعات فرستاده شد'
            return context
