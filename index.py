from distutils.debug import DEBUG
from flask import Flask,render_template, request, redirect, url_for, flash
import sqlite3



app=Flask(__name__)
app.secret_key='abc'

@app.route('/', methods=('GET','POST'))
def index():
    conn=sqlite3.connect('urlbase.db')

    if request.method=='POST':
        cur=conn.execute('select short_url from urls;')

        url=request.form['lurl']
        short_term=request.form['sterm']

        if (short_term,) not in cur:
            conn.execute(f'insert into urls (original_url,short_url) values(?,?)',(url,short_term))
            conn.commit()
            conn.close()
            short_url=request.host_url+short_term
            return render_template('index.html',short_url=short_url)
            
        else:
            return render_template('index.html',eroor=1,url=url)
            

    
    return render_template('index.html')
    
@app.route('/<id>')
def redir(id):
    conn=sqlite3.connect('urlbase.db')
    cur=conn.execute('select * from urls;')
    c=0
    for i in cur:
        if i[2]==id:
            c=1
            original_url=i[1]
            conn.execute('update urls set clicks=clicks+1 where short_url=?',(id,))
            conn.commit()
            conn.close()
            if "http://" in original_url or "https://" in original_url:
                print(1)
                return redirect(original_url)
            else:
                print(2)
                return redirect("https://"+original_url)
            
    if c==0:
        flash('Invalid URL')
        return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('untitled-1.html')

@app.route('/contact')
def contact():
    return render_template('untitled.html')

if __name__=="__main__":
    app.run(debug=False)
    
