# from django import forms
# from .models import Store


# class StoreForm(forms.ModelForm):
#     class Meta:
#         model = Store
#         fields = [
#             "name",
#             "business_name",
#             "address",
#             "owner",
#             "email",
#             "alternate_email",
#             "phone_number",
#             "alternate_phone_number",
#             "bio",
#             "about",
#             "display_picture",
#             "is_registered",
#             "rc_number",
#             "registration_certificate",
#             "bank_name",
#             "account_name",
#             "account_number",
#             "bvn",
#             "is_open",
#         ]

#     def __init__(self, *args, **kwargs):
#         super(StoreForm, self).__init__(*args, **kwargs)

#         # Add 'form-control' class to all input fields
#         for field_name in self.fields:
#             self.fields[field_name].widget.attrs["class"] = "form-control m-1"
#             # self.fields[field_name].widget.attrs["style"] = "border-radius: 0%;"

#         # # Add custom class 'form-floating' to each field's div
#         # for key, value in self.fields.items():
#         #     value.widget.attrs["class"] = "form-floating " + value.widget.attrs.get(
#         #         "class", ""
#         #     )
