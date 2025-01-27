from flask import Flask, jsonify, request
import html

"""
sample search engine, simply takes in an query argument, runs search in backend without sanitization
"""
app = Flask(__name__)

"""
ROUTE - /
METHOD(S) - GET
QUERY PARAMS - q: query term
"""
@app.route('/', methods=['GET'])
def base():
	query = request.args.get('q')
	query_html = ''
	if query:
		query_html = '<h2>Showing results for: '+ query + '<p> no results </p>'
	
	return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blog Posts</title>
        </head>
        <body>
            <h1>Search</h1>
            <form action="/" method="GET">
                <label for="q">Search:</label>
                <input type="text" id="q" name="q" required>
                <button type="submit">Submit</button>
            </form>
	    {query_html}
        </body>
        </html>
        """

"""
ROUTE - /safesearch
METHOD(S) - GET
QUERY PARAMS - q: query term
"""
@app.route('/safesearch', methods=['GET'])
def safesearch():
	query = request.args.get('q')
	query_html = ''
	if query:
		query_html = '<h2>Showing results for: '+ html.escape(query) + '<p> no results </p>'
	
	return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blog Posts</title>
        </head>
        <body>
            <h1>Search</h1>
            <form action="/safesearch" method="GET">
                <label for="q">Search:</label>
                <input type="text" id="q" name="q" required>
                <button type="submit">Submit</button>
            </form>
	    {query_html}
        </body>
        </html>
        """
	


if __name__ == '__main__':
	app.run()


