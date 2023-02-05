# import re
# from django.core.exceptions import ValidationError
# from .models import Var
#
#
# def valid_name_if_format(value):
#     founded_vars = [
#         var[2:-2] for var in
#         re.findall("{{\w*}}", value)
#     ]
#     if len(founded_vars):
#         mistakes = [
#             var for var in founded_vars
#             if var not in Var.get_
#         ]
#
#         raise ValidationError(" format error found in ", params=mistakes)
