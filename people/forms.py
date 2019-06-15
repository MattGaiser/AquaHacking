from django.db import models
from django.forms import ModelForm, Textarea, IntegerField, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Person, Skill, Emergency, Task

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'gender', 'age', 'occupation', 'skills', 'phone_number','email', 'address',
                  'address_city', 'address_province', 'address_country']
        age = IntegerField()
        skill_list = Skill.objects.all()
        skills = ModelMultipleChoiceField(widget=CheckboxSelectMultiple(),required=True, queryset=skill_list)

class EmergencyForm(ModelForm):
    class Meta:
        model = Emergency
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'skill_needed', 'emergency']
