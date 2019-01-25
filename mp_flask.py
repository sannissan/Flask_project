from flask import Flask
from flask import render_template

import mp_db

app = Flask(__name__)
app.debug = True


@app.route('/<table_name>')
def index(table_name):

    result = mp_db.engine.execute("select * from "+table_name)
    cat_table = result.fetchall()

    return render_template('catalog.html', table=table_name, posts=cat_table)


@app.route("/test")
def tested():
    print("вызов теста")
    return "Tested!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    return '<form method="post"><p><input type=text name=username><p><input type=submit value=Login></form>'


if __name__ == '__main__':
    app.run()
