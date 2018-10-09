from django import forms
from multidestination.models import TripHotelSearch

class TripHotelSearchForm(forms.ModelForm):
    class Meta:
        model = TripHotelSearch
        fields = ('city_1', 'checkin_1','checkout_1','numberOfPersons_1','city_2', 'checkin_2','checkout_2','numberOfPersons_2',
        'city_3', 'checkin_3','checkout_3','numberOfPersons_3','budget')  
    
    def clean_cityName(self): 
        return self.cleaned_data['city']
        
    def __init__(self, *args, **kwargs):
        super(TripHotelSearchForm, self).__init__(*args, **kwargs)
        self.fields[ 'checkin_1' ].input_formats = [ '%Y-%m-%d' ]
        self.fields[ 'checkout_1' ].input_formats = [ '%Y-%m-%d' ]
        self.fields[ 'checkin_2' ].input_formats = [ '%Y-%m-%d' ]
        self.fields[ 'checkout_2' ].input_formats = [ '%Y-%m-%d' ]
        self.fields[ 'checkin_3' ].input_formats = [ '%Y-%m-%d' ]
        self.fields[ 'checkout_3' ].input_formats = [ '%Y-%m-%d' ]


