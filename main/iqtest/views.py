from django.shortcuts import render
from .models import Score


# Create your views here.
def fiqtest(request):

    if request.method == "POST":
        username = request.POST.get('username')
        options1 = request.POST.get('options1')
        options2 = request.POST.get('options2')
        options3 = request.POST.get('options3')
        options4 = request.POST.get('options4')
        options5 = request.POST.get('options5')
        options6 = request.POST.get('options6')
        options7 = request.POST.get('options7')
        options8 = request.POST.get('options8')
        options9 = request.POST.get('options9')
        options10 = request.POST.get('options10')

        score = 0
        if options1 == '36':
            score += 1
        if options2 == 'მარიამი':
            score += 1
        if options3 == '6':
            score += 1
        if options4 == 'მარსი':
            score += 1
        if options5 == 'ლურჯი ვეშაპი':
            score += 1
        if options6 == 'option6-4':
            score += 1
        if options7 == 'option7-2':
            score += 1
        if options8 == 'html':
            score += 1
        if options9 == '8':
            score += 1
        if options10 == 'ოზონი':
            score += 1

        print(username)
        print(score)

        user_score = Score(user = username, score = score)
        user_score.save()

        data = {
            'key': score,
        }

        return render(request, 'iqtest/score.html', data)

    return render(request, 'iqtest/iqtest.html')


def oldscore(request):
    user_scores = Score.objects.all()

    data = {}

    for user_score in user_scores:
        print(f"User: {user_score.user}")
        print(f"Score: {user_score.score}")

    return render(request, 'iqtest/oldscore.html', {'user_scores':user_scores})