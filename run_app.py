import os


#from app import app
#from library._02_html_inside_view import app
#from library._03_template_str_inside_view import app
#from library._04_template_outside_view import app
#from library._05_basic_routing import app
#from library._06_raising_custom_error import app
#from library._07_request_info import  app
from library._08_redirects import app


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP','192.168.0.109')
    port = int(os.environ.get('PORT',8080))
    app.run(host=host, port = port)