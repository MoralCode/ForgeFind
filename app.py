from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static',)

@app.route("/")
def index():
	return render_template('index.html')


@app.route("/search")
def search():
	# print(f"queried for {}")
	query=request.args.get('query')
	print(query)
	return render_template("results.html", results=[1,2,3])