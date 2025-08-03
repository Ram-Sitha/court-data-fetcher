from django import forms

class CaseQueryForm(forms.Form):
    case_type=forms.CharField(label='Case Type',max_length=50)
    case_number=forms.CharField(label='Case Number',max_length=50)
    filing_year=forms.CharField(label='Filing Year',max_length=4)
    
