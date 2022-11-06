# Copyright (c) 2021 Jonathan Vice

from django import forms

from .models import Room


class AddRoomForm(forms.Form):
    room_name = forms.CharField(label="Interviewee Name")

class DelRoomForm(forms.Form):
    room_name = forms.CharField(label="Interviewee Name")


class AddEventForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Room.objects.all(), label="Interviewee")
    event_name = forms.CharField(label="Event Name")

class EditEventForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Room.objects.all())
    event_name = forms.CharField(label="Event Name")
