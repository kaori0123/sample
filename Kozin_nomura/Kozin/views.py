import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import ContactForm,InformationCreateForm
from .models import Information



logger=logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name="index.html"

class ContactView(generic.FormView):
    template_name="contact.html"
    form_class=ContactForm
    success_url=reverse_lazy('Kozin:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class  InformationlistView(LoginRequiredMixin,generic.ListView):
    model= Information
    template_name='information_list.html'
    paginate_by=4

    def get_queryset(self):
        informations=Information.objects.filter(user=self.request.user).order_by('-created_at')
        return informations

class InformationDetailView(LoginRequiredMixin,generic.DetailView):
    model = Information
    template_name = 'information_detail.html'

class InformationCreateView(LoginRequiredMixin,generic.CreateView):
    model = Information
    template_name = 'information_create.html'
    form_class = InformationCreateForm
    success_url = reverse_lazy('Kozin:information_list')

    def form_valid(self, form):
        diary = form.save(commit = False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request,'情報を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"情報の作成に失敗しました。")
        return super().form_invalid(form)

class InformationUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Information
    template_name = 'information_update.html'
    form_class = InformationCreateForm

    def get_success_url(self):
        return reverse_lazy('Kozin:information_detail',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request,'情報を更新しました。')
        return super().form_valid(form) 

    def form_invalid(self, form):
        messages.error(self.request,"情報の更新に失敗しました。")
        return super().form_invalid(form)

class InformationDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Information
    template_name = 'information_delete.html'
    success_url = reverse_lazy('Kozin:information_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request,"情報を削除しました。")
        return super().delete(request, *args, **kwargs)

# Create your views here.
