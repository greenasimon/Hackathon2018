from django import forms
from multidestination.models import HotelSearch

class HotelSearchForm(forms.ModelForm):
    class Meta:
        model = HotelSearch
        fields = ('city', 'checkin','checkout','type')  
    
    def clean_cityName(self): 
        return self.cleaned_data['city']
        
    def __init__(self, *args, **kwargs):
        super(HotelSearchForm, self).__init__(*args, **kwargs)
        self.fields[ 'checkin' ].input_formats = [ '%d/%m/%Y' ]
        self.fields[ 'checkout' ].input_formats = [ '%d/%m/%Y' ]


