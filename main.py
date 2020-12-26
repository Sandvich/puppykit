from flask import Flask, render_template, abort
import sqlite3, sys, string

app = Flask(__name__)

@app.route("/")
def root():
    # Renders the root page. Nothing special.
    return render_template('root.html', title="Main", highlight="index")

@app.route("/<string:path>/")
def main_paths(path):
    # Renders all the pages directly under the root.
    if path in ['contact', 'personal', 'professional', 'projects', 'writing']:
        return render_template(f"{path}.html", title=path.capitalize(), highlight=path)
    else:
        abort(404)

@app.route("/personal/<string:path>/")
def personal_paths(path):
    # Everything under personal
    if path == 'rpgs':
        return render_template(f"personal/rpg_main.html", title=f"Personal - {path.capitalize()}", highlight='personal')
    else:
        abort(404)

@app.route("/personal/rpgs/all/")
def all_rpgs():
    with sqlite3.connect('rpgs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM rpgs")
        rows = cursor.fetchall()
    return render_template('personal/rpg_results.html', data=rows, title="RPGs - All", highlight='personal')

@app.route("/personal/rpgs/run/")
def rpgs_to_run():
    with sqlite3.connect('rpgs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM rpgs WHERE to_gm=1")
        rows = cursor.fetchall()
    return render_template('personal/rpg_results.html', data=rows, title="RPGs - To Run", highlight='personal')

@app.route("/personal/rpgs/<string:search_type>/<string:query>/")
def rpg_pages(search_type, query):
    translator = str.maketrans('', '', string.punctuation)
    if search_type not in ['name', 'publisher_id', 'system']:
        abort(404)

    with sqlite3.connect('rpgs.db') as connection:
        cursor = connection.cursor()
        print(f'search term is {query}', file=sys.stderr)
        cursor.execute(f"SELECT * FROM rpgs WHERE {search_type} LIKE ?", (f'%{query.translate(translator)}%',))
        rows = cursor.fetchall()
    
    if len(rows) == 0:
        return render_template('personal/rpg_error.html', title="RPGs - 404", highlight='personal'), 404
    else:
        return render_template('personal/rpg_results.html', data=rows, title="RPGs - Search Results", highlight='personal')

@app.route("/projects/<string:path>/")
def project_paths(path):
    # Everything under projects
    if path in ['window', 'elcm', 'empyrean', 'packmates']:
        return render_template(f"projects/{path}.html", title=f"Projects - {path.capitalize()}", highlight='projects')
    elif path == "marked_for_death":
        return render_template("projects/marked_for_death.html", title="Projects - Marked for Death", highlight='projects')
    else:
        abort(404)

@app.route("/writing/<string:path>/")
def writing_paths(path):
    # Everything under writing
    valid = {
        'accalia': 'The Accalia',
        'finalstraw': 'The Final Straw',
        'landthought': 'A Land of Thought',
        'tippingpoint': 'Tipping Point',
        'uprightdevotion': 'Upright Devotion',
        'birth': 'Birth'    
    }
    if path in valid.keys():
        return render_template(f"writing/{path}.html", title=f"Writing - {valid[path]}", highlight='writing')
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
