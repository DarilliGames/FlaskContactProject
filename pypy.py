from flask import Flask, request
from flask import render_template



# /////////////////////////

page = "Welcome to the website!!!"
contact= {
    "Stephen" : { "name" : "Stephen", "phone" : "09875", "email": "thf@hotmail.com"},
    "Sophie" : { "name" : "Sophie", "phone" : "09845", "email": "tef@hotmail.com"},
    }
    
app = Flask(__name__)

# Flip
@app.route("/")

def frontPage():
    return render_template("index.html", data=page)


@app.route("/contact", methods=["GET", "POST"])
def gamePage():
    if request.method == "POST":
        newContactName = request.form.get("newPersonName")
        newContactPhone = request.form.get("newPersonPhone")
        newContactEmail = request.form.get("newPersonEmail")
        contact[newContactName] = { "name" : newContactName, "phone" : newContactPhone, "email" : newContactEmail }
    return render_template("contact.html", game=contact.values())
    
# ALTERNATIVELY YOU CAN USE UPDATE TO ADD

@app.route("/delete", methods=["POST"])
def deleteGame():
    name = request.form.get("contact_to_delete")
    del(contact[name])
    return "You deleted " + name
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)