from django import forms
from .models import RakeModel
from django .forms import ModelForm


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'full-width'})


class RakeForm(forms.ModelForm):
    class Meta:
        model = RakeModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RakeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'full-width'
