from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def root():
    # Renders the root page. Nothing special.
    return render_template('root.html', title="Main", highlight="index")

@app.route("/<string:path>/")
def main_paths(path):
    # Renders all the pages directly under the root.
    if path in ['contact', 'personal', 'professional', 'projects', 'writing']:
        return render_template("%s.html" % path, title=path.capitalize(), highlight=path)
    else:
        abort(404)

@app.route("/personal/<string:path>/")
def personal_paths(path):
    # Everything under personal
    if path in ['rpgs']:
        return render_template("personal/%s.html" % path, title="Personal - %s" % path.capitalize(), highlight='personal')
    else:
        abort(404)

@app.route("/projects/<string:path>/")
def project_paths(path):
    # Everything under projects
    if path in ['window', 'elcm', 'empyrean', 'packmates']:
        return render_template("projects/%s.html" % path, title="Projects - %s" % path.capitalize(), highlight='projects')
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
        return render_template("writing/%s.html" % path, title="Writing - %s" % valid[path], highlight='writing')
    else:
        abort(404)

if __name__ == "__main__":
    app.run()
