from django.contrib import admin
from .models import *


@admin.register(Anketa)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "region", "create_at", "select", "rezerv")


# @admin.register(Position)
# class PositionAdmin(admin.ModelAdmin):
#     list_display = ("id", "position_name")
#
#
# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ("id", "department_name")
#
#
# @admin.register(Staff)
# class StaffAdmin(admin.ModelAdmin):
#     list_display = ("full_name", "b_date", "phone", "address", "department", "position", "date_join", "status")

@admin.register(Users)
class ListUsers(admin.ModelAdmin):
    list_display = ("name", "user_name")


@admin.register(Work)
class List(admin.ModelAdmin):
    list_display = ("image", "work_title")


admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(ToDo)
admin.site.register(ExecutionTime)


