from flask import Flask, request, render_template
import chemequal

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        eq1 = request.form['eq1']
        eq2 = request.form['eq2']
        print(eq1)
        res = chemequal.run(eq1,eq2)
        print(res)
        return render_template('index.html',ans = res)
    return render_template('index.html',ans='')

if __name__ == '__main__':
    app.run('0.0.0.0')
