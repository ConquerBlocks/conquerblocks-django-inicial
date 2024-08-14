from django import forms
from django.contrib.auth.password_validation import validate_password


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre")
    email = forms.EmailField(label="Email")
    comentario = forms.CharField(max_length=1000, label="Comentario", widget=forms.Textarea)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre


class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=140, label="Nombre de usuario")
    first_name = forms.CharField(max_length=140, label="Nombre")
    last_name = forms.CharField(max_length=140, label="Apellidos")
    email = forms.EmailField(max_length=140, label="Email")

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2 and password1 != '':
            raise forms.ValidationError('Las contraseñas no coinciden')

        if password2 != '':
            validate_password(password2)

        return password2