from flask import Flask, render_template, abort
import sqlite3, sys, string

app = Flask(__name__)
order_statement = "ORDER BY system, publisher_id, name"

@app.route("/")
def root():
    # Renders the root page. Nothing special. Uses the latest blog post for part of the content.
    return render_template('root.html', title="Main", highlight="index")

@app.route("/<string:path>/")
def main_paths(path):
    # Renders all the pages directly under the root.
    if path in ['contact', 'personal', 'professional', 'projects', 'fiction', 'blogs']:
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
        cursor.execute(f"SELECT * FROM rpgs {order_statement}")
        rows = cursor.fetchall()
    return render_template('personal/rpg_results.html', data=rows, title="RPGs - All", highlight='personal')

@app.route("/personal/rpgs/run/")
def rpgs_to_run():
    with sqlite3.connect('rpgs.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM rpgs WHERE to_gm=1 {order_statement}")
        rows = cursor.fetchall()
    return render_template('personal/rpg_results.html', data=rows, title="RPGs - To Run", highlight='personal')

@app.route("/personal/rpgs/<string:search_type>/<string:query>/")
def rpg_pages(search_type, query):
    translator = str.maketrans('', '', string.punctuation)
    if search_type not in ['name', 'publisher_id', 'system']:
        abort(404)

    with sqlite3.connect('rpgs.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM rpgs WHERE {search_type} LIKE ? {order_statement}",
                        (f'%{query.translate(translator)}%',))
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

@app.route("/fiction/<string:path>/")
def fiction_paths(path):
    # Everything under fiction
    valid = {
        'accalia': 'The Accalia',
        'finalstraw': 'The Final Straw',
        'landthought': 'A Land of Thought',
        'tippingpoint': 'Tipping Point',
        'uprightdevotion': 'Upright Devotion',
        'birth': 'Birth'    
    }
    if path in valid.keys():
        return render_template(f"fiction/{path}.html", title=f"Fiction - {valid[path]}", highlight='fiction')
    else:
        abort(404)

@app.route("/blogs/<string:post>/")
def blogs(post):
    valid = {
        'site': ['site_setup.html', 'Website'],
        'gbg': ['game_builders_garage.html', 'Game Builders Garage']
    }
    if post in valid.keys():
        return render_template(f"blog/{valid[post][0]}", title=f"Blogs - {valid[post][1]}", highlight='blogs')
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500

if __name__ == "__main__":
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    app.run(debug=True)
