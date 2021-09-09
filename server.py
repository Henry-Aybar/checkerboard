from flask import Flask, render_template 
from board import make_checkerboard
app = Flask(__name__) 

@app.route('/')
def game_board():
    result = make_checkerboard(8,8)
    return render_template ("index.html", result = result)

@app.route('/<int:x>')    
def game_size_x (x):
    result = make_checkerboard(x,8)
    return render_template ("index.html", result = result)

@app.route('/<int:x>/<int:y>')    
def game_size (x,y):
    result = make_checkerboard(x,y)
    return render_template ("index.html", result = result)



if __name__=="__main__":     
    app.run(debug=True)    