from django.shortcuts import render
from .models import Candidate
from .forms import CandidateFilterForm

def candidate_list(request):
    candidates = Candidate.objects.all()
    form = CandidateFilterForm(request.GET)

    if form.is_valid():
        skill_filter = form.cleaned_data.get('skill_filter')
        sort_by = form.cleaned_data.get('sort_by')

        if skill_filter:
            candidates = candidates.filter(skills__icontains=skill_filter)

        if sort_by:
            candidates = candidates.order_by(sort_by)

    context = {
        'candidates': candidates,
        'form': form,
    }

    return render(request, 'candidate_list.html', context)

