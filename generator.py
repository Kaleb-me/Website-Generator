from google import genai

#Insert Gemini API key here
client = genai.Client(api_key="")


prompt = input("website idea: ")
        
ai_input = (f"""
            
    you are a full stack web developer. Your sole purpose is to generate a detailed
    website with the following prompt: {prompt}. 
    You must include html, css, and javascript elements, and include it in one file.
    your response must not include anything but the contents of website code which will then
    be taken and put into a file for immediate use. Use maximum tokens to generate a detailed website.

    To ensure that images are displayed correctly, pull them from picsum.photos or another source that can provide relevant images.
    make the page as interactive as possible.

    remember to include html, css, and javascript elements in the same file, and use as much code as you
    need to make it detailed.
    """)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=ai_input
)

print(response.text)
output = response.text
html = output.replace("```html","").replace("```","")

with open(f"Website/index.html", "w") as file:
    file.write(html)
