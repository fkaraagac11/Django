from django.db import models


class Calc(models.Model):
    name        = models.CharField(max_length=50)
    address     = models.CharField(max_length=100, blank=True)
    phone       = models.CharField(max_length=14, blank=True)
    city        = models.CharField(max_length=60, blank=True)

# Create your models here.
# Question = [
#     {
#         question_id:1,
#         question_text:"What is the capital city of Egypt",    
#     },
#     {
#         question_id:2,
#         question_text:"What is the capital city of ",    
#     },
#     {
#         question_id:3,
#         question_text:"What is the capital city of Greece",    
#     },
#     {
#         question_id:4,
#         question_text:"What is the capital city of Canada",    
#     },
#     {
#         question_id:5,
#         question_text:"What is the capital city of ABD",    
#     },
    
#     ]