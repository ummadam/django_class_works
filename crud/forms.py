from django import forms

class MyForm(forms.Form):
    color = forms.CharField()
    speed = forms.IntegerField(min_value=0, max_value=200)
    model = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Car Model'}))
    tags = forms.CharField()
    # agreement = forms.BooleanField()
    # models = forms.ChoiceField(choices=(
    #     ('BMW', 'BMW'), ('Toyota', 'Toyota')
    # ))
    # test = forms.MultipleChoiceField(choices=(
    #     ('BMW', 'BMW'), ('Toyota', 'Toyota'),
    #     ('BMW', 'BMW'), ('Toyota', 'Toyota'),
    #     ('BMW', 'BMW'), ('Toyota', 'Toyota'),
    # ))