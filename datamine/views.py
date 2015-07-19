from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .forms import DataMineForm
from .mixins import MineMixin


class CreateMineView(TemplateView):
    """ Class based view that let users create
        a scraping request.
    """
    template_name = 'datamine/create.html'
    context = {}

    def get(self, *args, **kwargs):
        self.context['form'] = DataMineForm()

        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        data = self.request.POST
        form = DataMineForm(data)

        if form.is_valid():
            mine = form.save()
            # Redirect to the mine's settings page
            return HttpResponseRedirect(reverse('dashboard'))


class MineHomeView(MineMixin, TemplateView):
    """ Class based view that contains the
        configuration of the specified MINE.
    """
    template_name = 'datamine/configure.html'
    context = {}

    def get(self, *args, **kwargs):
        mine_id = kwargs.get('mine_id')
        self.context['mine'] = self.get_mine_object(mine_id)

        return render(self.request, self.template_name, self.context)


class DataListView(MineMixin, TemplateView):
    """ Class based view that contains the list of
        scraped data.
    """
    template_name = 'datamine/datalist.html'
    context = {}

    def get(self, *args, **kwargs):
        mine_id = kwargs.get('mine_id')
        datalist = serializers.serialize('python', self.datalist(mine_id))

        self.context['datalist'] = datalist
        self.context['fields'] = self.get_fields(mine_id)

        return render(self.request, self.template_name, self.context)