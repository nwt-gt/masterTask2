from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def display_form():
    
    return render_template('main.html')


@app.route('/get_input', methods=['POST']) #matches the html form action
def input_reverse():
    str = request.form['input']
    stringlength=len(str) # calculate length of the list
    slicedString=str[stringlength::-1] # slicing 
    #print (slicedString) # print the reversed string
    return slicedString


if __name__ == '__main__':
  #app.run('192.168.139.137')
  app.run()
