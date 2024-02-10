from django.contrib import admin

from api.serializers import ClientSerializer
from web.models import *
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json


class WriterAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        chart_data = (
            Client.objects
            .annotate(y=Count("id"))
            .order_by("last_name")
            .order_by("first_name")
        )
        as_json = json.dumps(list(chart_data), cls=ClientSerializer)
        print("Json %s" % as_json)
        extra_context = extra_context or {"chart_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Client, WriterAdmin)
admin.site.register(MassageSession)
