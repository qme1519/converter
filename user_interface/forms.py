from django import forms

class UnitConversion(forms.Form):
    #source_unit = N one
    #destination_unit = None
    source_value = forms.FloatField(
    widget=forms.NumberInput(
    attrs={
    "onchange": "convertNumber('source')",
    "onkeyup": "convertNumber('source')",
    "placeholder": "Number to convert",
    "id": "sourceInput",
    "class": "numberInput"
    }
    )
    )

    destination_value = forms.FloatField(
        widget=forms.NumberInput(
        attrs={
        "onchange": "convertNumber('destination')",
        "onkeyup": "convertNumber('destination')",
        "placeholder": "Number to convert",
        "id": "destinationInput",
        "class": "numberInput"
        }
        )

    )
