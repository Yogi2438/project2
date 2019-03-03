from django import forms
from .models import mregister

class fregister(forms.ModelForm):
	class Meta:
		model = mregister
		fields = ['name','roll_no','std','email','phone']