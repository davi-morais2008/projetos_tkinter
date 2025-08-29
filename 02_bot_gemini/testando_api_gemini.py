from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyD5l_20H1M3gT7INQxSF75KQi3yH3h-ML0")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Faça um texto sobre como eu, Davi, odeio o Fernando Fernandes Odilon"
)
print(response.text)