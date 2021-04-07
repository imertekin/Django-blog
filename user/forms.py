from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length='50',label='Kullanıcı Adı')
    password=forms.CharField(max_length='12',label='Parola',widget=forms.PasswordInput)
    confirm=forms.CharField(max_length='12',label='Parola Doğrula',widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        confirm=self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('Parolalar eşleşmiyor')
    
        values= {
            "username": username,
            "password": password


        }

        return values

class LoginUserForm(forms.Form):
    username=forms.CharField(max_length='50',label='Kullanıcı Adı')
    password=forms.CharField(max_length='12',label='Parola',widget=forms.PasswordInput)
    
    values= {
            "username": username,
            "password": password}
