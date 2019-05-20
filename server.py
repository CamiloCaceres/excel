from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
import merge

app = Flask(__name__)

documents = UploadSet('documents', DOCUMENTS)

app.config['UPLOADED_DOCUMENTS_DEST'] = 'static/doc'
configure_uploads(app, documents)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'doc' in request.files:
        docu = request.files['doc']
        filename = documents.save(docu)
        merged = merge.merge(docu)

        return filename
    return render_template('upload.html')


if __name__ == '__main__':
	app.run(debug=True)
