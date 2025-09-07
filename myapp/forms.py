from django import forms

class FeedbackForm(forms.Form):
 comment=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your comment'}))
  
 