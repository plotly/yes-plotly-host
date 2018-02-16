import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    if 'text/html' in str(request.accept_mimetypes):
        return render_template('yes.html')
    else:
        return 'YES, plotly.host works for you.'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
