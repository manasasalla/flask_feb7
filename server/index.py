from flask import Flask, render_template, request
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

app = Flask(__name__)

gauth = GoogleAuth()
client_secrets = {
    "web":{"client_id":"285465957506-g39tkiqoaded2ik946vtu486u5icckpr.apps.googleusercontent.com",
           "project_id":"server-450111",
           "auth_uri":"https://accounts.google.com/o/oauth2/auth",
           "token_uri":"https://oauth2.googleapis.com/token",
           "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
           "client_secret":"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",
           "redirect_uris":["http://localhost:8090/","http://127.0.0.1:5000","https://server-eta-smoky.vercel.app/"],
           "javascript_origins":["http://localhost:8090"]}}

SCOPES = ['https://www.googleapis.com/auth/drive.file']

#gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    gfile = drive.CreateFile({'title': file.filename})
    gfile.SetContentString(file.read().decode("latin-1"))  # Adjust encoding if needed
    gfile.Upload()

    return "File uploaded successfully to Google Drive!"


if __name__ == "__main__":
    #app.run(debug=False)
      app.run( debug=True)


