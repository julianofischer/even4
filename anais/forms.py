from django.forms import ModelForm, DateInput
from .models import Anais, Evento
from django.forms.widgets import FileInput
from django.contrib.admin.widgets import AdminDateWidget

class AnaisForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['data_de_publicacao'].widget.attrs.update({'class': 'datepicker form-control', 'pattern':"[0-9]{2}/[0-9]{2}/[0-9]{4}"})

    class Meta:
        model = Anais
        fields = '__all__'
        help_texts = {'data_de_publicacao': 'Formato: dd/mm/aaaa'}

class EventoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if not isinstance(field.widget, FileInput):
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = Evento
        exclude = ['anais']
