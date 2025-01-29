from flask import Flask, jsonify, request, render_template
import html

"""
sample blog, in memory list of posts, users can add with no sanitization

"""
app = Flask(__name__)

posts = []

"""
ROUTE - /
METHOD(S) - GET
QUERY PARAMS - post
"""
@app.route('/', methods=['GET'])
def base():
    # display posts
    post = request.args.get('post')
    if post:
        posts.append(post)

    posts_html = "".join(f"<li>{item}</li>" for item in posts)
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blog Posts</title>
        </head>
        <body>
            <h1>Submit a Blog Post</h1>
            <form action="/" method="GET">
                <label for="post">Enter a post:</label>
                <input type="text" id="post" name="post" required>
                <button type="submit">Submit</button>
            </form>

            <h1>Blog Posts</h1>
            <ul>
                {posts_html}  <!-- This will render raw user input directly into the HTML -->
            </ul>
        </body>
        </html>
        """
	
def is_escaped(s):
    return '&' in s 
 
"""
ROUTE - /safeview
METHOD(S) - GET
QUERY PARAMS - post
"""
@app.route('/safeview', methods=['GET'])
def safeview():
    post = request.args.get('post')
    if post:
        posts.append(html.escape(post))

    # backend logic to make display nice, we don't want to double escape or else it is displayed as escaped text
    posts_html = ""
    for item in posts:
        if is_escaped(item):
            posts_html = posts_html + f"<li>{item}</li>"
        else:
            posts_html = posts_html + f"<li>{html.escape(item)}</li>"

    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blog Posts</title>
        </head>
        <body>
            <h1>Submit a Blog Post</h1>
            <form action="/safeview" method="GET">
                <label for="post">Enter a post (no xss):</label>
                <input type="text" id="post" name="post" required>
                <button type="submit">Submit</button>
            </form>

            <h1>Blog Posts</h1>
            <ul>
                {posts_html}  <!-- This will render raw user input directly into the HTML -->
            </ul>
        </body>
        </html>
        """


if __name__ == '__main__':
    app.run()



