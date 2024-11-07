from django import forms

class FollowForm(forms.Form):
    profile_pk = forms.IntegerField(label="Idendtificador del usuario", widget=forms.HiddenInput())
