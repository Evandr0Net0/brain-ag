from django.contrib import admin
from producers.models import Producer

# Register your models here.


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('cpforcnpj', 'farm_name', 'city', 'state', 'total_area_hectares', 'arable_area_hectares',
                    'vegetation_area_hectares', 'planted_types')


admin.site.register(Producer, ProducerAdmin)
