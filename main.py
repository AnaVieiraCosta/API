from flask import Flask, jsonify, render_template 

app = Flask(__name__)

@app.route('/')
def inicio():
  return render_template('index.html')

@app.route('/<pais>/<comida_tipicas>')
def qual_pais(pais):
  lista_capital = ['Buenos Aires', 'La Paz', 'Brasilia', 'Santiago', 'Bogota', 'Quito', 'Georgetown', 'Assunçao', 'Lima', 'Paramaribo', 'Montevideu', 'Caracas', 'Caiena']
  pais = int(pais)
      
  return jsonify({f'pais {pais}':lista_capital[pais-1]})


app.run(host='0.0.0.0')



