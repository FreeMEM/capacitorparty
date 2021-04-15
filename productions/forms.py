from django import forms
from productions.models import Production
from upload_validator import FileTypeValidator


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = (
            "title",
            "description",
            "production_type",
            "filepath",
        )

        labels = {
            "title": "Título",
            "description": "Descripción",
            "production_type": "Tipo",
            "filepath": "File",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "type": "text", "placeholder": "Título"}
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Descripción",
                }
            ),
            "production_type": forms.Select(
                attrs={"class": "form-control", "placeholder": "Tipo"}
            ),
            # 'filepath': forms.TextInput(attrs = {'class':'form-control','type':'file', 'placeholder':'File'}),
            "filepath": forms.FileInput(
                attrs={
                    "accept": "image/jpeg,image/png,application/x-tar,application/x-amiga-disk-format,application/x-adf,application/x-lha",
                    "class": "form-control",
                    "type": "file",
                    "placeholder": "File",
                }
            ),
            # "filepath": forms.FileField(
            # label="",
            # help_text="Formats accepted: JPEG nd PNG",
            # required=True,
            # validators=[
            #     FileTypeValidator(allowed_types=["image/jpeg", "image/png"])
            # ],
            # ),
        }

    def __init__(self, *args, **kwargs):
        super(ProductionForm, self).__init__(*args, **kwargs)
        self.fields["production_type"].choices = [
            ("", "Elige el tipo de producción"),
        ] + list(self.fields["production_type"].choices)[1:]
