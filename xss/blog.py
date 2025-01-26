from flask import Flask, jsonify, request, render_template

"""
sample blog, in memory list of posts, users can add with no sanitization

"""
app = Flask(__name__)

posts = []

"""
ROUTE - /
METHOD(S) - GET
QUERY PARAMS - none
"""
@app.route('/', methods=['GET'])
def base():
    # display posts
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
            <form action="/post" method="POST">
                <label for="user_input">Enter a post:</label>
                <input type="text" id="user_input" name="user_input" required>
                <button type="submit">Submit</button>
            </form>

            <h1>Blog Posts</h1>
            <ul>
                {posts_html}  <!-- This will render raw user input directly into the HTML -->
            </ul>
        </body>
        </html>
        """

"""
ROUTE - /post
METHOD(S) - POST
QUERY PARAMS - none
"""
@app.route('/post', methods=['POST'])
def post():
    try:
        user_input = request.form.get('user_input')
        posts.append(user_input)
        return base()
    except Exception as e:
        return 400


if __name__ == '__main__':
    app.run()



