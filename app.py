from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renderiza a página index.

    """
    return render_template('index.html')

#Data Frame Principal para renderizar na pagina /table
df = pd.DataFrame({
    'alunos': ['Renato1', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})


#Criei o HTM e o
@app.route('/table')
def table():
    """
    Renderiza a página da tabela de alunos.

    Esta função busca os dados dos alunos armazenados no DataFrame do pandas chamado df,
    converte esses dados em uma lista de dicionários usando o método
    `to_dict(orient='records')`. Cada dicionário representa uma
    linha da tabela, pa melhorar a iteração  no Jinja2.

    """

    return render_template('table.html', table_data=df.to_dict(orient='records'))



#Parametro para inicialização da aplicação
if __name__ == "__main__":
    app.run(debug=True)
