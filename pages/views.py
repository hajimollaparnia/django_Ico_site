from django.shortcuts import render, redirect
from .forms import UserMessageForm, AdminReplyForm, EmailForm

from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from .models import Transaction, About1, Activity1, Activity2, Activity3, Message, AdminReply,Email

from django.core.mail import send_mail


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'


class RoadMapPageView(TemplateView):
    template_name = 'pages/Roadmap.html'


class ActivityPageView(TemplateView):
    template_name = 'pages/activity.html'


class TeamPageView(TemplateView):
    template_name = 'pages/team.html'


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.all()
        context['about_info'] = About1.objects.first()
        context['activity1_list'] = Activity1.objects.first()
        context['activity2_list'] = Activity2.objects.all()
        context['activity3_list'] = Activity3.objects.first()
        context['messages'] = Message.objects.all()  # اضافه کردن همه پیام‌ها به context
        context['replies'] = AdminReply.objects.all()
        context['form'] = UserMessageForm()

        return context

    def post(self, request, *args, **kwargs):
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # هدایت کاربر به URL موفقیت پس از ذخیره فرم
        # اگر فرم صحیح نبود، دوباره همان صفحه را با نمایش خطاها بارگذاری کنید.
        return self.render_to_response(self.get_context_data(form=form))


    # def post(self, request, *args, **kwargs):
    #     user_message_form = UserMessageForm(request.POST)
    #     admin_reply_form = AdminReplyForm(request.POST)
    #
    #     if user_message_form.is_valid():
    #         user_message = user_message_form.save()
    #         # می‌توانید اینجا کدی برای ارسال ایمیل به ادمین نوشته و اطلاعات مورد نیاز را ارسال کنید
    #
    #     if admin_reply_form.is_valid():
    #         admin_reply = admin_reply_form.save(commit=False)
    #         admin_reply.user_message = Message.objects.get(pk=request.POST.get('user_message_id'))
    #         admin_reply.save()
    #
    #     return redirect('home')

    # تغییر متد render_to_response برای شرایط خودتان (به صورت اختیاری)
    # def render_to_response(self, context, **response_kwargs):
    #     # اینجا شما می‌توانید شرایط خاصی را برای رندر کردن چک کنید
    #     if all(key in context for key in ['about_info', 'transactions', 'activity1_list']):
    #         return render(request, self.template_name, context)
    #     else:
    #         # برای حالات دیگر، اجازه دهید که منطق پیش‌فرض به کار گرفته شود.
    #         return super().render_to_response(context, **response_kwargs)

    def render_to_response(self, context, **response_kwargs):
        if 'about_info' in context and 'transactions' in context and 'activity1_list' in context:
            return render(self.request, self.template_name, context)
        else:
            return super().render_to_response(context, **response_kwargs)


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_instance = form.save()
            try:
                send_mail(
                    email_instance.subject,
                    email_instance.message,
                    email_instance.from_email,
                    [email_instance.to_email],
                    fail_silently=False,
                )
                email_instance.sent = True
                email_instance.save()
                messages.success(request, 'ایمیل با موفقیت ارسال شد.')
            except Exception as e:
                messages.error(request, f'خطا در ارسال ایمیل: {e}')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})
#
# from django.views.generic import TemplateView
# from django.core.mail import send_mail
# from django.http import HttpResponse, HttpResponseRedirect
# from .forms import ReplyForm, MessageForm  # اطمینان حاصل کنید که کلاس MessageForm در forms.py تعریف شده است
# from .models import ContactMessage, Transaction, About1, Activity1, Activity2, Activity3
#
#
# class HomePageView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['transactions'] = Transaction.objects.all()
#         context['about_info'] = About1.objects.first()
#         context['activity1_list'] = Activity1.objects.first()
#         context['activity2_list'] = Activity2.objects.all()
#         context['activity3_list'] = Activity3.objects.first()
#         context['form'] = MessageForm()
#         # اضافه کردن ReplyForm به context
#         context['reply_form'] = ReplyForm()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         # تشخیص اینکه آیا پست برای پیام است یا پاسخ
#         message_form = MessageForm(request.POST or None)
#         reply_form = ReplyForm(request.POST or None)
#
#         if 'message_id' in request.POST:
#             # به‌روز رسانی این قسمت با شناسه‌ی پیام و ارسال پاسخ
#             message_id = request.POST.get('message_id')
#             if reply_form.is_valid():
#                 return self.reply_to_message(request, message_id)
#         elif message_form.is_valid():
#             # منطق برای ذخیره‌ی پیام جدید
#             message_form.save()
#             return HttpResponseRedirect(self.request.path_info)
#
#         # İf هیچکدام صحیح نیست، درخواست را با فرم‌های شامل خطاها رندر کنید
#         return self.render_to_response(context)
#
#     def reply_to_message(self, request, message_id):
#         message = ContactMessage.objects.get(id=message_id)
#         reply_form = ReplyForm(request.POST)
#
#         if reply_form.is_valid():
#             subject = reply_form.cleaned_data['subject']
#             reply_message = reply_form.cleaned_data['message']
#             recipient_email = message.email
#             send_mail(subject, reply_message, 'your_email@example.com', [recipient_email])
#             return HttpResponse('پیام با موفقیت ارسال شد')
#         return HttpResponse('خطا در ارسال پیام')

# دیگر متدها بدون تغییر باقی می‌مانند...

