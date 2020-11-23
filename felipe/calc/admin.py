from django.contrib import admin

# Register your models here.

admin.site.reqister(Calc)
#admin.site.reqister(Students)
#admin.site.reqister(Teachers)
#admin.site.reqister(Courses)
#admin.site.reqister(Subjects)


# class Calc(models.Model):
#     name        = models.CharField(max_length=50)
#     address     = models.CharField(max_length=100, blank=True)
#     phone       = models.CharField(max_length=14, blank=True)
#     city        = models.CharField(max_length=60, blank=True)