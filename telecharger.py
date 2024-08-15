from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download')
def download_file():
    path = "/home/ec2-user/projectteststylef/Résultat_Test.xlsx"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
