import os
import PyPDF2
from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads' #onde fica os pdfs
os.makedirs(UPLOAD_FOLDER, exist_ok=True) #iniciar o diretório
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #fala onde os arquivos serão salvos

palavras_chave = ["App", "Arthur", "Desenvolvimento", "Mobile", "Aplicativo", "Sistema", "Automatizado", "Impressora", "Jogo"]

@app.route('/', methods=['GET' , 'POST'])
def upload():
    result = None
    if request.method == 'POST':
    
        if 'file' not in request.files:
            return 'Sem arquivo'
        
        file = request.files['file']
        if file.filename == '':
            return 'Sem arquivo'
        
        if file and file.filename.endswith('.pdf'):
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(caminho)
            
            with open(caminho, "rb") as arquivo:
                leitor = PyPDF2.PdfReader(arquivo)
                texto=""
                for pagina in leitor.pages:
                    texto += pagina.extract_text()
            
            result = {}
            texto = texto.lower()
            for palavra in palavras_chave:
                result[palavra] = texto.count(palavra.lower())
                
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)
    
    