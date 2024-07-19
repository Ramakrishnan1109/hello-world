
# from flask import Flask

# #constructor
# app = Flask(__name__)

# #Routing, #Methods
# @app.route('/')
# def hello_world():
#     return "Hello World!!!"

# #routing2,#method2
# @app.route('/hello')
# def hello():
#     return "Hello Welcome to the Training!!!"

# #routing3,#method3 with value
# @app.route('/login/<username>')
# def login(username):
#     return f'The Username is {username}'

# #routing4, method4 with value ID
# @app.route('/login/<int:id>')
# def login_id(id):
#     return f'The is of the User is {id}'

# #Run
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)