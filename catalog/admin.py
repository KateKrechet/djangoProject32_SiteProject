from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Breed)
# admin.site.register(Owner)
admin.site.register(Diagnosis)


# admin.site.register(Doctor)
# admin.site.register(Medicine)


# admin.site.register(Animal)


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'breed', 'owner', 'age_years', 'diagnosis', 'doctor', 'display_med', 'date')
    list_filter = ('date', 'diagnosis', 'doctor')


admin.site.register(Animal, AnimalAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'specialization', 'cost_rub')


admin.site.register(Doctor, DoctorAdmin)


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('title', 'dosage')


admin.site.register(Medicine, MedicineAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'tel')


admin.site.register(Owner, OwnerAdmin)
