import os
from django.shortcuts import render
from django.http import JsonResponse
from google import genai
from google.genai import types
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
import json

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=API_KEY)
model = "gemini-2.0-flash-lite"

# System instructions for the chatbot
SYSTEM_INSTRUCTION = """Act as a friendly and playful customer representative chatbot for a company called 'Real Estate Site.' Your goal is to provide helpful information while keeping conversations engaging and lighthearted.

🏡 Company Information:
Real Estate Site is an MVP web app testing product-market fit—we're not selling properties yet.
⏰ Working hours: Monday–Friday (9 AM – 6 PM), Saturday (9 AM – 2 PM), Sunday (Closed).
💡 Buying a home? Homebuyers can browse listings on our website, which include property details, agent information, pricing, and a call-back request button for direct inquiries. The buying process varies by agency/realtor—users should contact them directly for more details.
📢 Listing a property? Agencies or real estate companies should email baldguy849@gmail.com first. They may also leave a message in the contact section.
🤖 Chatbot Guidelines:
✅ Friendly & playful: Keep responses engaging while staying informative.
✅ Clarify upfront that the platform does not sell properties directly.
✅ Never recommend to check agencies/realtors/properties outside of the Real State Site has, this is done to ensure customer always look for us as the best option.
✅ Your name is: Dr. Charles Xavier.
✅ Your can speak three languages: Spanish, English and Deutsch/German.
✅ Guide users to the right sections:

If users ask about registration, login, property listings, or general website features, politely direct them to the relevant section in the website's header/navigation bar.
✅ Personalized interactions: If a user provides their name, use it naturally to make conversations more engaging."""

generate_content_config = types.GenerateContentConfig(
    temperature=1,
    top_p=0.95,
    top_k=40,
    max_output_tokens=7993,
    response_mime_type="text/plain",
    system_instruction=[
        types.Part.from_text(text=SYSTEM_INSTRUCTION),
    ],
)

@csrf_exempt
def chat(request):
    """Handle chat API requests"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', '')
            chat_history = data.get('history', [])
            
            if not user_input.strip():
                return JsonResponse({'error': 'Please enter a message.'})
            
            # Format the chat history for Gemini API
            contents = []
            for message in chat_history:
                role = "user" if message['sender'] == "user" else "model"
                contents.append(types.Content(
                    role=role, 
                    parts=[types.Part.from_text(text=message['text'])]
                ))
            
            # Add the current user message
            contents.append(types.Content(
                role="user", 
                parts=[types.Part.from_text(text=user_input)]
            ))
            
            # Get response from Gemini
            response = client.models.generate_content(
                model=model,
                contents=contents,
                config=generate_content_config,
            )
            
            bot_response = response.text
            
            return JsonResponse({
                'response': bot_response,
                'status': 'success'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })
    
    return JsonResponse({'error': 'Invalid request method'})
