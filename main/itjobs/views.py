from django.shortcuts import render
from .jobs_ge import f_jobs_ge


# Create your views here.
def itjobs(request):
    jobs = f_jobs_ge()

    data = {
        'key': jobs
    }

    for i in jobs:
        print(i)
    # print(jobs)
    print(type(jobs))

    return render(request, 'itjobs/itjobs.html', data)