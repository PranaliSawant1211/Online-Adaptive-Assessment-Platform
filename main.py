from flask import Flask, render_template,request
#from flask_wtf import Form 
#from wtforms import StringField, PasswordField
#from wtforms.validators import InputRequired
import csv
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'
y=0
r=1
score=0
optiona = []
optionc = []
i=0
el = []
er = []
ea = []
ml = []
mr = []
ma = []
hl = []
hr = []
ha = []

with open('./static/diff_data.csv') as csvfile:
    readCSV = list(csv.reader(csvfile, delimiter=','))
    for i in range(0,650):
        row_you_want = readCSV[i]
        if(row_you_want[8]=='easy' and row_you_want[9]=='logical'):
        	el.append(i)
        if(row_you_want[8]=='easy' and row_you_want[9]=='reasoning'):
        	er.append(i)
        if(row_you_want[8]=='easy' and row_you_want[9]=='aptitude'):
        	ea.append(i)
        if(row_you_want[8]=='medium' and row_you_want[9]=='logical'):
        	ml.append(i)
        if(row_you_want[8]=='medium' and row_you_want[9]=='reasoning'):
        	mr.append(i)
        if(row_you_want[8]=='medium' and row_you_want[9]=='aptitude'):
        	ma.append(i)
        if(row_you_want[8]=='hard' and row_you_want[9]=='logical'):
        	hl.append(i)
        if(row_you_want[8]=='hard' and row_you_want[9]=='reasoning'):
        	hr.append(i)
        if(row_you_want[8]=='hard' and row_you_want[9]=='aptitude'):
        	ha.append(i)
#class LoginForm(Form):
#	username = StringField('username', validators=[InputRequired()])
#	password = PasswordField('password', validators=[InputRequired()])

@app.route('/test2', methods=['GET', 'POST'])
def test2():

	return render_template('test.html', optiona=optiona)

@app.route("/read_cell", methods=['POST','GET'])
# @is_logged_in
def read_cell():
    global y
    global old_index
    with open('./static/diff_data.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        old_index=y


        if(y<len(readCSV)):

            row_you_want = readCSV[hr[y]]
            question=row_you_want[1]
            option1=row_you_want[2]
            option2=row_you_want[3]
            option3=row_you_want[4]
            option4=row_you_want[5]
            y+=1
            return render_template('test1.html', question=question, option1=option1, option2=option2, option3=option3, option4=option4,score=score)
        else:
            x=(len(readCSV)-1)
            row_you_want = readCSV[x]
            question=row_you_want[1]
            option1=row_you_want[2]
            option2=row_you_want[3]
            option3=row_you_want[4]
            option4=row_you_want[5]
            return render_template('test1.html', question=question, option1=option1, option2=option2, option3=option3, option4=option4)
@app.route('/check_answer', methods=['POST','GET'])
# @is_logged_in
def check_answer():
    global score
    global old_index

    with open('./static/diff_data.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        option1a = request.form.get("option1") != None
        option2a = request.form.get("option2") != None
        option3a = request.form.get("option3") != None
        option4a = request.form.get("option4") != None
        # option 1
        if(option1a==True):
            row_you_want = readCSV[hr[old_index]]
            given_answer="Answer: Option A"
            correct_answer=row_you_want[7]
            if(given_answer==correct_answer):
                score += 1
            return test()


        # option 2
        elif(option2a==True):
            row_you_want = readCSV[hr[old_index]]
            given_answer="Answer: Option B"
            correct_answer=row_you_want[7]
            if(given_answer==correct_answer):
                score += 1
            return test()

        # option3
        elif(option3a==True):
            row_you_want = readCSV[hr[old_index]]
            given_answer="Answer: Option C"
            correct_answer=row_you_want[7]
            if(given_answer==correct_answer):
                score += 1
            return test()

        # option4
        elif(option4a==True):
            row_you_want = readCSV[hr[old_index]]
            given_answer="Answer: Option D"
            correct_answer=row_you_want[7]
            if(given_answer==correct_answer):
                score += 1
            return test()

        else:        
            return test()

@app.route('/test', methods=['POST','GET'])
def test():
    global y
    global r
    global old_index
    old_index=y
    with open('./static/cat_data.csv') as csvfile:
    	pred_read = list(csv.reader(csvfile, delimiter=','))
    	with open('./static/diff_data.csv') as csvfile:
	    	readCSV = list(csv.reader(csvfile, delimiter=','))
	    	# Logical
	    	if(i<10):
		        # if(row_you_want[8]=='easy' and row_you_want[9]=='logical'):
        		row_you_want = pred_read[r]
        		if(row_you_want[8]=='easy'):
		            row_you_want1 = readCSV[el[y]]
		            question=row_you_want1[1]
		            option1=row_you_want1[2]
		            option2=row_you_want1[3]
		            option3=row_you_want1[4]
		            option4=row_you_want1[5]
		            y+=1
		            r+=1
		            ID=el[y]
		            return render_template('test1.html', question=question, option1=option1, option2=option2, option3=option3, option4=option4,score=score,pred=row_you_want[8],r=r,ID=ID)
		        if(row_you_want[8]=='medium'):
		        	row_you_want1 = readCSV[ml[y]]
		        	question=row_you_want1[1]
		        	option1=row_you_want1[2]
		        	option2=row_you_want1[3]
		        	option3=row_you_want1[4]
		        	option4=row_you_want1[5]
		        	y+=1
		        	r+=1
		        	ID=ml[y]
		        	return render_template('test1.html', question=question, option1=option1, option2=option2, option3=option3, option4=option4,score=score,pred=row_you_want[8],r=r,ID=ID)		           
		        if(row_you_want[8]=='hard'):
		        	row_you_want1 = readCSV[hl[y]]
		        	question=row_you_want1[1]
		        	option1=row_you_want1[2]
		        	option2=row_you_want1[3]
		        	option3=row_you_want1[4]
		        	option4=row_you_want1[5]
		        	y+=1
		        	r+=1
		        	ID=hl[y]
		        	return render_template('test1.html', question=question, option1=option1, option2=option2, option3=option3, option4=option4,score=score,pred=row_you_want[8],r=r,ID=ID)
		       
	    			


if __name__ == '__main__':
	app.run(debug=True)