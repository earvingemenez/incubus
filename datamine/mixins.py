from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import DataMine


class MineMixin(object):

    def __init__(self, *args, **kwargs):
        return super(MineMixin, self).__init__(*args, **kwargs)

    def get_mine_object(self, mine_id):
        try:
            return DataMine.objects.get(id=mine_id)
        except DataMine.DoesNotExist as e:
            raise Http404

    def data_model(self, mine_obj):
        try:
            return mine_obj.data_model.model_class()
        except Exception as e:
            # No data model assigned yet
            return None

    def datalist(self, mine_id):
        mine = self.get_mine_object(mine_id)
        model_ = self.data_model(mine)

        return model_.objects.all() if model_ else []

    def get_fields(self, mine_id):
        try:
            mine = self.get_mine_object(mine_id)
            model_ = self.data_model(mine)

            return model_._meta.get_fields()
        except Exception as e:
            raise e