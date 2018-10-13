from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from . import models
from .models import *
from django.utils.translation import gettext_lazy as _
from .field_helpers import PhoneNumberField,lasyaSizeLimit,prosceniumSizeLimit,battleofbandsSizeLimit,videoFileSupportMessage,audioVideoFileSupportMessage

class SignUpForm(forms.Form):
    full_name = forms.CharField(label='Full Name', min_length=3, max_length=127)
    institution = forms.CharField(label='Institution', min_length=3, max_length=127)
    city = forms.CharField(label='City', min_length=3, max_length=127)
    email = forms.EmailField(label='Email')
    contact = forms.CharField(label='Contact number', min_length=3, max_length=20)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class CampusAmbassadorForm(forms.ModelForm):
    class Meta:
        model = CampusAmbassador
        fields = ('full_name', 'institution','city','email','contactForCalls','contactForWhatsapp',)
        labels = {
            "full_name": "Full Name",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contactForCalls": "Mobile Number",
            "contactForWhatsapp": "Mobile Number (WhatsApp)",
        }

class LasyaForm(forms.ModelForm):
    class Meta:
        model = LasyaRegistration
        fields = ('teamName', 'teamLeader','institution','city','email','contact1','contact2','participantList','videoFile','videoFileLink')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "videoFile": videoFileSupportMessage(lasyaSizeLimit),
            "videoFileLink":"Link to Video (Only if you do not upload the video file)"
        }

class ProsceniumForm(forms.ModelForm):
    class Meta:
        model = ProsceniumRegistration
        fields = ('teamName', 'teamLeader','language','institution','city','email','contact1','contact2','participantList','videoFile','videoFileLink')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "language":"Language",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "videoFile": videoFileSupportMessage(prosceniumSizeLimit),
            "videoFileLink":"Link to Video (Only if you do not upload the video file)"
        }


class BattleOfBandsForm(forms.ModelForm):
    class Meta:
        model = BattleOfBandsRegistration
        fields = ('teamName', 'teamLeader','institution','city','email','contact1','contact2','participantList','audioVideoFile','audioVideoFileLink')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
            "audioVideoFile": audioVideoFileSupportMessage(battleofbandsSizeLimit),
            "audioVideoFileLink": "Link to Audio/Video (Only if you do not upload the file)"
        }

class FootprintsForm(forms.ModelForm):
    class Meta:
        model = FootprintsRegistration
        fields = ('teamName', 'teamLeader','language','institution','city','email','contact1','contact2','participantList')
        labels = {
            "teamName": "Team Name",
            "teamLeader": "Team Leader",
            "language":"Language",
            "institution": "Institution",
            "city": "City",
            "email": "Email",
            "contact1": "Mobile Number",
            "contact2": "Another Mobile Number",
            "participantList": "List of Participants (Enter each participant in a new line or seperated by comma)",
        }

class DecoherenceForm(forms.ModelForm):
    class Meta:
        model = DecoherenceRegistration
        fields = ('teamName', 'institution','city', 'participant1', 'qualification1', 'email1', 'contact1', 'participant2', 'qualification2', 'email2', 'contact2', )
        labels = {
            "teamName": "Team Name",
            "institution": "Institution",
            "participant1": "Full Name",
            "qualification1": "Qualification",
            "email1": 'Email',
            "contact1": "Mobile Number",
            "participant2": "Full Name",
            "qualification2": "Qualification",
            "email2": 'Email',
            "contact2": "Mobile Number",
            "city": "City",
        }
