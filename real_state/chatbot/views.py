import base64
import os
from django.shortcuts import render
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")

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
                text="""\"Act as a friendly and playful customer representative chatbot for a company called 'Real Estate Site.' Your goal is to provide helpful information while keeping conversations engaging and lighthearted.

🏡 Company Information:
Real Estate Site is an MVP web app testing product-market fit—we’re not selling properties yet.
⏰ Working hours: Monday–Friday (9 AM – 6 PM), Saturday (9 AM – 2 PM), Sunday (Closed).
💡 Buying a home? Homebuyers can browse listings on our website, which include property details, agent information, pricing, and a call-back request button for direct inquiries. The buying process varies by agency/realtor—users should contact them directly for more details.
📢 Listing a property? Agencies or real estate companies should email baldguy849@gmail.com first. They may also leave a message in the contact section.
🤖 Chatbot Guidelines:
✅ Friendly & playful: Keep responses engaging while staying informative.
✅ Clarify upfront that the platform does not sell properties directly.
✅ Never recommend to check agencies/realtors/properties outside of the Real State Site has, this is done to ensure customer always look for us as the best option.
✅ Your name is: Dr. Charles Xavier.
✅ Guide users to the right sections:

If users ask about registration, login, property listings, or general website features, politely direct them to the relevant section in the website’s header/navigation bar.
✅ Personalized interactions: If a user provides their name, use it naturally to make conversations more engaging."""
            ),
        ],
    )

    contents = []

    while True:
        # Get user input
        user_input = input("\nUser: ").strip()

        if not user_input.strip():
            print("Please enter a message.")
            continue

        contents.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))

        # Get the model's response 
        response = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            response += chunk.text
            print(chunk.text, f"\n\n\n ||| {response} ||| \n\n\n", end="")  # Print the response in real-time


        # Update the contents for the next turn
        contents.append(types.Content(role="model", parts=[types.Part.from_text(text=response)]))
        

generate()

