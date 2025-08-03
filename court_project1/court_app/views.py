from django.shortcuts import render
from .forms import CaseQueryForm
from .models import CaseQuery
from .scraper import fetch_case_details  # importing the scraper function

def index(request):
    result=None
    if request.method=='POST':
        form=CaseQueryForm(request.POST)
        if form.is_valid():
            case_type=form.cleaned_data['case_type']
            case_number=form.cleaned_data['case_number']
            filing_year=form.cleaned_data['filing_year']

            # Using the scraper function instead of dummy string
            result=fetch_case_details(case_type,case_number,filing_year)

            # Save to DB
            CaseQuery.objects.create(
                case_type=case_type,
                case_number=case_number,
                filing_year=filing_year,
                raw_response=result
            )
    else:
        form=CaseQueryForm()

    queries=CaseQuery.objects.order_by('-created_at')[:5]

    return render(request,'court_app/index.html',{
        'form':form,
        'result':result,
        'queries':queries
    })
