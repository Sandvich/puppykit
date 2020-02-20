from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('root.html', title="Main", highlight="index")

@app.route("/<string:path>/")
def main_paths(path):
    if path in ['contact', 'personal', 'professional', 'projects', 'writing']:
        return render_template("%s.html" % path, title=path.capitalize(), highlight=path)
    else:
        abort(404)

'''
    Let's spend some time thinking about structure.
    This mainfile should do just the core. What does that entail?
'''

if __name__ == "__main__":
    app.run()
