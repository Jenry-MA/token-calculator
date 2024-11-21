from django.shortcuts import render
from django.http import HttpResponse
import tiktoken

# Create your views here.

def home(request):
    return render(request,'pages/home.html',{})

def calculate_tokens(request):

    prompt = request.POST.get('prompt')
    encode_name = request.POST.get('encode_name')

    encoding = tiktoken.get_encoding(encode_name)
    enconde_prompt = encoding.encode(prompt)
    num_tokens = len(enconde_prompt)

    context = {
        'encode_promt': enconde_prompt,
        'num_tokens': num_tokens,
        'encode_name': encode_name
    }
    return render(request,'pages/home.html',context)

