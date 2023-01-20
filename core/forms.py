from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    sender = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, label='message', widget=forms.TextInput(attrs={'placeholder': 'message'}))
    
    
#     <div class="form-group col-md-6">
# <input type="email" name="email" class="form-control" placeholder="Email" required="required">
# </div>
# <div class="form-group col-md-12">
# <input type="text" name="subject" class="form-control" placeholder="Subject" required="required">
# </div>
# <div class="form-group col-md-12">
# <textarea rows="6" name="message" class="form-control" placeholder="Your Message" required="required"></textarea>
# </div>