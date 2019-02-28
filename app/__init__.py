from flask import Flask, render_template, url_for, redirect
from flask_mail import Mail, Message
from app.forms import ContactForm
import json
import os




app = Flask(__name__)

app.config['SECRET_KEY'] = 'ovojetajnaionaceostatiskrivena'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail()
mail.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
    

@app.route('/')
@app.route('/home')
def index():
    filename = os.path.join(app.static_folder, 'recepies.json')
    with open(filename) as recepies:
        data = json.load(recepies)

    y = json.dumps(data)
    print(y)

    return render_template('index.html', title="Početna", recepies=data)



@app.route('/recepti')
def recepies():
    filename = os.path.join(app.static_folder, 'recepies.json')
    with open(filename) as recepies:
        data = json.load(recepies)

    y = json.dumps(data)
    print(y)

    return render_template('recepti.html', title="Recepti", recepies=data)



@app.route('/vjezbe')
def workout():

    return render_template('workout.html', title='Vježbe')



@app.route('/householdHacks')
def hacks():

    return render_template('tips.html', title='Savjeti')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        message = Message(form.subject.data, sender='softythetechguy@gmail.com', recipients=['andelavanesaa@gmail.com'])
        message.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(message)
        return redirect(url_for('index'))
    return render_template('contact.html', title='Kontakt', form=form)
