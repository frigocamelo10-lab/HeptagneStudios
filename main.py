from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Coloque sua chave do Gemini aqui
API_KEY = "AIzaSyCHwCMBgT3U5HVikcJmQ-XYLWMpPW3ESD4"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

@app.route('/chat', methods=['POST'])
def chat():
    pergunta = request.data.decode('utf-8')
    
    payload = {
        "contents": [{"parts": [{"text": pergunta}]}]
    }
    
    try:
        response = requests.post(GEMINI_URL, json=payload)
        data = response.json()
        # Extrai o texto da resposta da IA
        texto_ia = data['candidates'][0]['content']['parts'][0]['text']
        return texto_ia
    except Exception as e:
        return f"Erro no Servidor: {str(e)}"

if __name__ == "__main__":
    # O Render exige que o app rode na porta definida pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

