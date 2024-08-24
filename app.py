from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from config import config


app = Flask(__name__)


app.config.from_object(config['development']) 

# OAuth Config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    redirect_uri='http://localhost:5000/callback',
    jwks_uri= 'https://www.googleapis.com/oauth2/v3/certs',
    client_kwargs={
        'scope': 'openid email profile',
    }
)

@app.route('/')
def index():
    print()
    email = dict(session).get('email', None)
    return f"Hello, {email}!\n{session.get('picture', None)}"

@app.route('/login')
def login():
    redirect_uri = url_for('callback', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/callback')
def callback():
    token = google.authorize_access_token()
    resp = google.get('https://openidconnect.googleapis.com/v1/userinfo')
    user_info = resp.json()
    print(user_info)
    session['email'] = user_info['email']
    session['picture'] = user_info['picture']
    return redirect('/')

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

if __name__ == "__main__":
    app.run()
    
