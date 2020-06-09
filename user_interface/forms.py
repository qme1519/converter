from django import forms

class UnitConversion(forms.Form):
    #source_unit = N one
    #destination_unit = None
    source_unit = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "style": "display: none", "autocomplete": "off"}
            ),
        )
    source_value = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "onchange": "convertNumber('source')",
                "onkeyup": "convertNumber('source')",
                "placeholder": "Number to convert",
                "id": "sourceInput",
                "class": "inputField",
                "autocomplete": "off",
                "min": "0"
            }
        )
    )
    destination_unit = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "style": "display: none", "autocomplete": "off"}
            ),
        )
    destination_value = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "onchange": "convertNumber('destination')",
                "onkeyup": "convertNumber('destination')",
                "placeholder": "Converted number",
                "id": "destinationInput",
                "class": "inputField",
                "autocomplete": "off",
                "min": "0"
            }
        )

    )

class LogInForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "Username"
                }
            ),
        )
    password = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "placeholder": "Password"
                }
            ),
        )

class DateConverter(forms.Form):
    source_unit = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "style": "display: none", "autocomplete": "off"}
            ),
        )
    source_value = forms.DateField(
    widget=forms.TextInput(
        attrs={"class": "form-control", "style": "display: none", "autocomplete": "off"}
        ),)

    destination_unit = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "style": "display: none", "autocomplete": "off"}
            ),
        )
    destination_value = forms.DateField(
    widget=forms.TextInput(
        attrs={"class": "form-control", "style": "display: none", "autocomplete": "off"}
        ),)
