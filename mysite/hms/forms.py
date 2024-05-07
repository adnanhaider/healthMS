from django import forms

class HealthCheckForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0)
    weight = forms.FloatField(label='Weight (kg)', min_value=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap form-control class to all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
