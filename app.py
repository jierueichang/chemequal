from flask import Flask, request, render_template
import chemequal

app = Flask(__name__)

def escape(eq):
    return eq.replace('>','&gt;').replace('<','&lt;')

@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        eq1 = escape(request.form['eq1'])
        eq2 = escape(request.form['eq2'])
        res = chemequal.run(eq1,eq2)
        print(res)
        return render_template('index.html',ans = res)
    return render_template('index.html',ans='')

if __name__ == '__main__':
    app.run('0.0.0.0')
