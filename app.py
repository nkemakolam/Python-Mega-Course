from flask import Flask,jsonify ,request

app = Flask(__name__)
Books = [{
'id': 0,
'name':'Green Eggs',
'price':'5.98787',
'isbn':'4566787'
},
{
'id': 1,
'name':'Green Eggs',
'price':'5.98787',
'isbn':'4567'
}
 ]
@app.route('/books')
def get_book():
    return jsonify({'books':Books})
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = []
    for book in Books:
        if book["isbn"] == isbn:
            return_value={
            'name':book["name"],
            'price': book["price"]
            }
    #print(jsonify(return_value))
    return jsonify(return_value)


@app.route('/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()

app.debug = True
app.run(port=5000)
