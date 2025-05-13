from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return f"User {request.form.get('name')} registered!"
    return '''
        <form method="POST">
            Name: <input name="name">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
