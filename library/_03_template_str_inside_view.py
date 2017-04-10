from flask import Flask
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    library_name = "Poe"
    html = """
        <html>
            <h1> Welcome to {{library_name}} library!</h1>
            <ul>
                {% for author in authors %}
                    <li>{{ author }} </li>
                {% endfor %}
            </ul>
        </html>
    """
    authors = ["Rabindranath Tagore", "Satyajit Roy", "Arthur Conan Doyle"]
    rendered_html = render_template_string(html, library_name=library_name, authors = authors)
    return rendered_html
