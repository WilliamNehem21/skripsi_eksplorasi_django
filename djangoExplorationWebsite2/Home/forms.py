from django import forms

class HomeForm(forms.Form):
    email = forms.CharField(
        label="email", 
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'masukkan email'
            }
        ))
    saran = forms.CharField(
        label="saran", 
        widget=forms.Textarea(
            attrs= {
                'class': 'form-control',
                'placeholder': 'masukkan saran'
            }
        ))
