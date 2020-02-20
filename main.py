from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html', title="Main", highlight="index")

'''
    Let's spend some time thinking about structure.
    This mainfile should do just the core. What does that entail?
'''

if __name__ == "__main__":
    app.run()
