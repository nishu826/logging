from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store 
        fields = ['part_number','purchase_order','mat_code','description','quantity','qty_consumed','location','gate_pass','Date','image']
        lables = {
            'part_number':'part number',
            'purchase_order' :'purchase order',
            ' mat_code' : 'mat code',
            'description' : 'description',
            'quantity':'quantity',
            'qty_consumed' : 'qty_consumed',
            'location' : 'location',
            'gate_pass' : 'gate_pass',
            'Date' : 'date',
            
           

        }
        widgets = {
        'part_number' : forms.NumberInput(attrs={'class':'form-control'}),
        'purchase_order' :forms.NumberInput(attrs={'class':'form-control'}),
        'mat_code' :forms.NumberInput(attrs={'class':'form-control'}),
        'description' : forms.TextInput(attrs={'class':'form-control'}),
        'quantity' :forms.NumberInput(attrs={'class':'form-control'}),
        'qty_consumed' :forms.NumberInput(attrs={'class':'form-control'}),
        'location' : forms.TextInput(attrs={'class':'form-control'}),
        'gate_pass':forms.NumberInput(attrs={'class':'form-control'}),
        'Date' : forms.TextInput(attrs={'class': 'form-control'}),
        
        }