from django import forms

class CandidateFilterForm(forms.Form):
    SORT_CHOICES = (
        ('name', 'Name'),
        ('experience', 'Experience'),
        ('date_applied', 'Date Applied'),
    )

    skill_filter = forms.CharField(max_length=100, required=False)
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False)