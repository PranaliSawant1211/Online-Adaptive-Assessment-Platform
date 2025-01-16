from flask import Flask, render_template, redirect, url_for, request
import csv
# create the application object
app = Flask(__name__)
y=1

@app.route('/')
def home():
    return "Hello, World!"
home()
@app.route('/test')
def test():
    return render_template('test.html')

@app.route("/read_cell", methods=['POST','GET'])
def read_cell():
    global y
    with open('./static/dataset1-651.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        test = request.form.get("option3") != None
        
        for x in range(1,10):
        
            if(x<len(readCSV)):

                row_you_want = readCSV[x]
                question=row_you_want[0]
                option1=row_you_want[1]
                option2=row_you_want[2]
                option3=row_you_want[3]
                option4=row_you_want[4]
                y+=1
                return render_template('test.html', question=question, option1=option1, option2=option2, option3=option3, option4=option4,test=test,x=x,y=y)
           


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Invalid Username/Password.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)