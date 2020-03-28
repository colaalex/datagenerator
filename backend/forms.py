from django import forms


class ProjectCreateForm(forms.Form):
    project_name = forms.CharField(max_length=50)
    project_description = forms.TextInput()
