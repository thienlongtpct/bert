from django.shortcuts import render
from summarizer import Summarizer


def index(request):
    if request.method == 'POST':
        model = Summarizer()
        input_text = request.POST.get('input')
        output_text = "".join(model(input_text, min_length=20))
        return render(request, 'index.html', {"input": input_text, "output": output_text})
    response = render(request, 'index.html', {"input": "", "output": ""})
    return response

