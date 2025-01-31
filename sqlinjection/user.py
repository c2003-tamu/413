from flask import Flask, request, jsonify
import sqlite3

"""
basic application, only stores user information
used to show what sql injection looks like and how to avoid
"""

# app object definition
app = Flask(__name__)

#initialize db
with sqlite3.connect("example.db") as con:
  cur = con.cursor()
  users = [
    (0, 'Cade Royal', 1234, 'secret'),
    (1, 'LeBron James', 1234, 'secret2'),
    (2, 'Michael Jordan', 2345, 'catlover42')
  ]
  cur.execute("DROP TABLE user;")
  cur.execute("CREATE TABLE user(id, name, number, password);")
  cur.execute("DELETE FROM user;")
  cur.executemany("INSERT INTO user VALUES (?,?,?,?);", users)
  con.commit()
  cur.close()


"""
ENDPOINT - /user
METHOD(S) - GET
QUERY PARAMS - name
"""
@app.route('/user', methods=['GET'])
def unsafeuser():
  username = request.args.get('name')  
  if username is None:
    return jsonify({"error": "no user name given"}), 400

  # string concat is unsafe: should be paramerized queries
  # this given app sql injection vulnerability
  statement = "SELECT id, name, number FROM user WHERE name = '"+username + "';"
  
  try: 
    with sqlite3.connect("example.db") as db:
      cursor = db.execute(statement)
      rows = cursor.fetchall()
      if len(rows)==0:
        return jsonify({"message": "no results"})
      return jsonify(rows), 200
  except Exception as e:
    return jsonify({"error": "error connecting to db"}), 500


"""
ENDPOINT - /safeuser
METHOD(S) - GET
QUERY PARAMS - name
"""
@app.route('/safeuser', methods=['GET'])
def safeuser():
  username = request.args.get('name')
  
  if username is None:
    return jsonify({"error": "no user name given"}), 400

  statement = "SELECT id, name, number FROM user WHERE name = ?;"
 
  try: 
    with sqlite3.connect("example.db") as db:
      cursor = db.execute(statement, (username,))
      rows = cursor.fetchall()
      if len(rows)==0:
        return jsonify({"message": "no results"})
      return jsonify(rows), 200
  except Exception as e:
    return jsonify({"error": "error connecting to db"}), 500


if __name__ == "__main__":
  app.run()

