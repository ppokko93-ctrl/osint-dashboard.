from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>OSINT Dashboard</h1>
    <form action="/sherlock" method="post">
        Username: <input name="username">
        <button type="submit">Run Sherlock</button>
    </form>
    <form action="/holehe" method="post">
        Email: <input name="email">
        <button type="submit">Run Holehe</button>
    </form>
    <form action="/harvester" method="post">
        Domain: <input name="domain">
        <button type="submit">Run theHarvester</button>
    </form>
    <form action="/spiderfoot" method="post">
        Target: <input name="target">
        <button type="submit">Run SpiderFoot</button>
    </form>
    '''

@app.route('/sherlock', methods=['POST'])
def sherlock():
    username = request.form['username']
    result = subprocess.getoutput(f"python3 -m sherlock {username}")
    return f"<pre>{result}</pre>"

@app.route('/holehe', methods=['POST'])
def holehe():
    email = request.form['email']
    result = subprocess.getoutput(f"python3 -m holehe {email}")
    return f"<pre>{result}</pre>"

@app.route('/harvester', methods=['POST'])
def harvester():
    domain = request.form['domain']
    result = subprocess.getoutput(f"python3 -m theHarvester -d {domain} -b google")
    return f"<pre>{result}</pre>"

@app.route('/spiderfoot', methods=['POST'])
def spiderfoot():
    target = request.form['target']
    result = subprocess.getoutput(f"python3 -m spiderfoot -s {target}")
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
