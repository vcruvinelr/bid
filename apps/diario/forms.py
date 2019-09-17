from django.forms import ModelForm
from .models import Diario
from apps.usuarios.models import Usuario

class DiarioForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(DiarioForm, self).__init__(*args, **kwargs)
        self.fields['proprietario'].queryset = Usuario.objects.filter(
            programa=user.usuario.programa) #usuario está no atributo user -> variavel user vem do model usuario e filtra pelo programa envolvido.

    class Meta:
        model = Diario
        fields = ['titulo', 'descritivo', 'data', 'proprietario']
