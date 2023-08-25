from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai

@csrf_exempt
def chat_with_gpt(request, question:str):
    if request.method == 'POST':

        openai.api_key = 'your-api-key'

        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=question,
            temperature=1.2,
            max_tokens=100
        )

        chatbot_response = response

        return JsonResponse({'response': chatbot_response})
    else:
        return JsonResponse({'message': 'Invalid request method'})