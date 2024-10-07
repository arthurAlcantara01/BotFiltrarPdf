import PyPDF2;
from flask import Flask, render_template, request;

app = Flask(__name__)

palavras_chave = ["App", "Desenvolvimento", "Mobile", "Aplicativo", "Sistema", "Automatizado", "Impressora", "Jogo"]

@app.route('/', methods=['GET', 'POST'])

def upload():
    
    result = None;
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Erro';
           
        file = request.files['file']
        if file.filename == '':
            return "Erro nulo";
        
        if file and file.filename.endswith('.pdf'):
            read = PyPDF2.PdfReader(file)
            texto = "";
            
            for pagina in read.pages:
                texto += pagina.extract_text();
            textoLower = texto.lower();
            
            result = {}
            for palavra in palavras_chave:
                result[palavra] = textoLower.count(palavra.lower());
            
    return  render_template('index.html', result=result)
    
if __name__ == '__main__':
    app.run(debug=True)