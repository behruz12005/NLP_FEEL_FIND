from django import forms

class Sentences(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Uzingizni hissiyotlarizni yozing !",
                'aria-label': "Uzingizni hissiyotlarizni yozing !",
                'aria-describedby': 'button-addon2'
            }
        )
    )
