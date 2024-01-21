from django.views.generic import TemplateView
from django.shortcuts import render
from .models import About1
from . import models


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_description'] = models.HomeDescription.objects.first()
        # context['link'] = models.Link.objects.first()

        context['about_info'] = About1.objects.first()
        context['transactions'] = models.About2.objects.all()

        context['token_description'] = models.TokenDescription.objects.first()

        context['activity'] = models.Activity.objects.first()

        # context['time'] = models.Timer.objects.first()
        # context['timer'] = models.Event.objects.first()

        context['activity1_list'] = models.Roadmap1.objects.first()
        context['activity2_list'] = models.Roadmap2.objects.all()

        context['footer_description'] = models.FooterDescription.objects.first()
        context['footer_links'] = models.FooterLinks.objects.all()

        # context['messages'] = Message.objects.all()  # اضافه کردن همه پیام‌ها به context
        # context['form'] = UserMessageForm()

        return context

    # def post(self, request, *args, **kwargs):
    #     form = UserMessageForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')  # هدایت کاربر به URL موفقیت پس از ذخیره فرم
    #     # اگر فرم صحیح نبود، دوباره همان صفحه را با نمایش خطاها بارگذاری کنید.
    #     return self.render_to_response(self.get_context_data(form=form))

    def render_to_response(self, context, **response_kwargs):
        # اینجا شما می‌توانید شرایط خاصی را برای رندر کردن چک کنید
        if all(key in context for key in ['about_info', 'transactions', 'activity1_list', 'token_description']):
            return render(self.request, self.template_name, context)
        else:
            # برای حالات دیگر، اجازه دهید که منطق پیش‌فرض به کار گرفته شود.
            return super().render_to_response(context, **response_kwargs)

