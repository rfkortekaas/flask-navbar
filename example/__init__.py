from flask import Flask, render_template
from flask_navbar import Nav
from flask_navbar.elements import *

nav = Nav()

# registers the "top" menubar
nav.register_element('top', Navbar(
    View('Widgits, Inc.', 'index'),
    NavUl(
        View('Our Mission', 'about', icon='fa fa-home'),
        Subgroup(
            'Products',
            View('Wg240-Series', 'products', product='wg240'),
            View('Wg250-Series', 'products', product='wg250'),
            Separator(),
            Text('Discontinued Products'),
            View('Wg10X', 'products', product='wg10x'),
        ),
        Link('Tech Support', 'http://techsupport.invalid/widgits_inc'),
        navbar_right=False
    ),
    Search('/search', navbar_right=False, icon='fa fa-search', btn_text='Go',
           input_placeholder='Search...', input_name='q', input_id='q', ),
    NavUl(View('Login', 'login', icon='fa fa-sign-in'), navbar_right=True),
    navbar_inverse=True,
    # navbar_fixed='top',
    # logo_filename='logo.png'
))


def create_app(configfile=None):
    app = Flask(__name__)
    nav.init_app(app)

    # not good style, but like to keep our examples short
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/products/<product>/')
    def products(product):
        return render_template('index.html', msg='Buy our {}'.format(product))

    @app.route('/about-us/')
    def about():
        return render_template('index.html')

    @app.route('/login/')
    def login():
        return render_template('index.html')

    return app
