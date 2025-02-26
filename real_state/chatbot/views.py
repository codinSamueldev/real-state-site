import base64
import os
from django.shortcuts import render
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
print(API_KEY)

def generate():
    client = genai.Client(
        api_key=API_KEY,
    )

    model = "gemini-2.0-flash-lite"

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=7993,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(
                text="""\"Act as a friendly and playful customer representative chatbot for a company called 'Real Estate Site.'

    Company Information:

    🏡 Real Estate Site is not a real company—just an MVP web app testing product-market fit. At this stage, we are not selling any properties yet.
    ⏰ Working hours: Monday–Friday (9 AM – 6 PM), Saturday (9 AM – 2 PM), Sunday (Closed).
    💡 Buying a home? The purchasing process depends on the agency or realtor. Homebuyers should contact agents or realtors directly to learn more.
    📢 Want to list a property? If an agency or real estate company wants to publish a property, they should email baldguy849@gmail.com first. They may also leave a message in the contact section.
    Chatbot Guidelines:

    Be friendly and playful while staying informative.
    Politely clarify upfront that the platform does not sell properties to prevent misunderstandings.
    Provide working hours and general guidance about real estate processes.
    Encourage agencies/realtors to email first for property listings."""
            ),
        ],
    )

    # Initial prompt to "start" the conversation
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text="Hello!")] 
        )
    ]

    while True:
        # Get the model's response 
        response = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            response += chunk.text
            print(chunk.text, end="")  # Print the response in real-time

        # Get user input
        user_input = input("\nUser: ") 

        if not user_input.strip():
            print("Please enter a message.")
            continue

        # Update the contents for the next turn
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_input)]
            ),
            types.Content(
                role="model",
                parts=[types.Part.from_text(text=response)] # Include the previous response for context
            )
        ]

generate()