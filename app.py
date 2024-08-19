from flask import Flask, jsonify, request, abort
import pandas as pd
import os

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    # Caminho relativo para o arquivo Excel
    file_path = 'teste.xlsx'
    
    # Verificar se o arquivo existe
    if not os.path.isfile(file_path):
        abort(404, description="Arquivo não encontrado")
    
    try:
        # Ler a planilha a partir da segunda linha
        df = pd.read_excel(file_path, header=0)
        
        # Converter DataFrame para uma lista de dicionários
        data_store = df.to_dict(orient='records')
        
        # Organizar os dados em um dicionário maior
        result = {
            "data": data_store
        }

        print(result)
        return jsonify(result), 200
    except Exception as e:
        # Retornar erro se ocorrer um problema
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
