from django import forms


#Code from Here

DEPARTMENT_CHOICES = (
    ('PWSLab DevOps Support','PWSLab DevOps Support'),
    ('support','iSupport')

)

PRIORITY_CHOICES =(
    ('','None'),
    ('hign','High - Production System Down'),
    ('medium','Medium - System Impaired'),
    ('low','Low - General Guidance'),
)
CATEGORY_CHOICES =(
    ('','None'),
    ('other','Other'),
)
class TicketForm(forms.Form):
    department          = forms.ChoiceField(choices=DEPARTMENT_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    category            = forms.ChoiceField(choices=CATEGORY_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    pwsLab_url          = forms.URLField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject             = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    description         = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class':'form-control'}))
    contact_name        = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    email               = forms.EmailField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone               = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control'}))
    priority            = forms.ChoiceField(choices=PRIORITY_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))