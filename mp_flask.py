from flask import render_template, Flask
import mp_requests
import mp_db

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/index')
def index():
    return "index page"


@app.route('/list/<table_name>')
def list_table(table_name):

    result = mp_db.engine.execute("select * from "+table_name)
    cat_table = result.fetchall()

    return render_template('catalog.html', table=table_name, posts=cat_table)


@app.route('/getCategories')
def get_categories():
    mp_requests.add_categories(10)
    return list_table('Category')


@app.route('/getCatalog')
def get_catalog():
    mp_requests.add_catalog(10)
    return list_table('Catalog')


@app.route("/test")
def tested():
    print("вызов теста")
    return "Tested!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


