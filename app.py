from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def enter():
    return render_template('layer.html')

@app.get('/function_1')
def function_1():
      return render_template('Function_1/layer.html')

@app.get('/function_1/layer_1-1')
def function_1_layer_1():
      return render_template('Function_1/layer_1-1.html')

@app.get('/function_1/layer_1-2')
def function_1_layer_2():
      return render_template('Function_1/layer_1-2.html')

@app.get('/function_1/layer_1-1/page_1-1-1')
def function_1_layer_1_page_1():
      return render_template('Function_1/page_1-1-1.html')

@app.get('/function_1/layer_1-1/page_1-1-2')
def function_1_layer_1_page_2():
      return render_template('Function_1/page_1-1-2.html')

@app.get('/function_1/layer_1-2/page_2-1-1')
def function_1_layer_2_page_1():
      return render_template('Function_1/page_1-2-1.html')

@app.get('/function_2')
def function_2():
      return render_template('Function_2/layer.html')

@app.get('/function_2/layer_2-1')
def function_2_layer_1():
      return render_template('Function_2/layer_2-1.html')

@app.get('/function_2/layer_2-1/layer_2-1-1')
def function_2_layer_1_layer_1():
      return render_template('Function_2/layer_2-1-1.html')

@app.get('/function_2/layer_2-1/layer_2-1-1/page_2-1-1-1')
def function_2_layer_1_layer_1_page_1():
      return render_template('Function_2/page_2-1-1-1.html')

@app.get('/function_3/page_3-1')
def function_3_page_1():
      return render_template('Function_3/page_3-1.html')

if __name__ == '__main__':
	# Flask class 中的 run()會執行應用程式的啟動
	app.run()