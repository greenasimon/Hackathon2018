from django import forms
from multidestination.models import TripHotelSearch

class TripHotelSearchForm(forms.ModelForm):
    class Meta:
        model = TripHotelSearch
        fields = ('city', 'checkin','checkout','numberOfPersons','budget')  
    
    def clean_cityName(self): 
        return self.cleaned_data['city']
        
    def __init__(self, *args, **kwargs):
        super(TripHotelSearchForm, self).__init__(*args, **kwargs)
        self.fields[ 'checkin' ].input_formats = [ '%Y-%m-%d' ]
        self.fields[ 'checkout' ].input_formats = [ '%Y-%m-%d' ]


