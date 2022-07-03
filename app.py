from flask import Flask, render_template, request
from forges import all_forges

app = Flask(__name__, static_folder='static',)

@app.route("/")
def index():
	return render_template('index.html')


@app.route("/search")
def search():
	# print(f"queried for {}")
	query=request.args.get('query')
	print("handling query: " + query)
	results = []
	for forge in all_forges:
		results.extend(forge.searchfor(query))
	return render_template("results.html", results=results)