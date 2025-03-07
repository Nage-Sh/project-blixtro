from django import forms
from inventory.models import Issue
from config.mixins import form_mixin

class IssueReportForm(form_mixin.BootstrapFormMixin, forms.ModelForm):
    reg_no = forms.CharField(max_length=255, required=False, label="Registration No")
    admission_no = forms.CharField(max_length=255, required=False, label="Admission No")

    class Meta:
        model = Issue
        fields = ['reg_no', 'admission_no', 'subject', 'description', 'room']

    def clean(self):
        cleaned_data = super().clean()
        reg_no = cleaned_data.get("reg_no")
        admission_no = cleaned_data.get("admission_no")

        if not reg_no and not admission_no:
            raise forms.ValidationError("Please provide either Registration No or Admission No.")
        return cleaned_data
