from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm
from .models import About1
from . import models


# from .models import SiteVisit


class HomePageView(TemplateView, FormView):
    template_name = 'home.html'
    form_class = ContactForm  # افزودن فرم به ویو

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_description'] = models.HomeDescription.objects.first()

        context['about_info'] = About1.objects.first()
        context['transactions'] = models.About2.objects.all()

        context['token_description'] = models.TokenDescription.objects.first()

        context['activity'] = models.Activity.objects.first()

        context['activity1_list'] = models.Roadmap1.objects.first()
        context['activity2_list'] = models.Roadmap2.objects.all()

        context['footer_description'] = models.FooterDescription.objects.first()
        context['footer_links'] = models.FooterLinks.objects.all()

        context['ob'] = models.Timer.objects.first()

        # site_visit, created = SiteVisit.objects.get_or_create(pk=1)
        # site_visit.admin_only_count += 1
        # site_visit.save()

        return context

    def form_valid(self, form):

        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # ارسال ایمیل به آدرس مورد نظر
        subject = f'New Contact Message from '
        from_email = 'par@shab76.monster'
        to_email = "hajimollaparnia7676@gmail.com"
        message_body = f'Name: \nEmail: {email}\n\n{message}'

        send_mail(subject, message_body, from_email, [to_email])
        messages.success(self.request, 'Your message has been sent successfully.')

        # self.success_url = self.request.path

        # return super().form_valid(form)

        # return HttpResponseRedirect(self.request.path)

        response_data = {'success': True}
        return JsonResponse(response_data)

    def render_to_response(self, context, **response_kwargs):
        # اینجا شما می‌توانید شرایط خاصی را برای رندر کردن چک کنید
        if all(key in context for key in ['about_info', 'transactions', 'activity1_list', 'token_description']):
            return render(self.request, self.template_name, context)
        else:
            # برای حالات دیگر، اجازه دهید که منطق پیش‌فرض به کار گرفته شود.
            return super().render_to_response(context, **response_kwargs)
