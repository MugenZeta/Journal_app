from Functions import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    action_log_in = LogIn()
    action_sign_up = SignUp()
    entry_titles = db.child('Posts').child('entries').get()
    for entry in entry_titles.each():
        title = entry.key()
        body = entry.val()

        print(entry.key())
    return render_template('index.html', action_sign_up = action_sign_up, action_log_in = action_log_in,  post_title=title)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def LogIn():
    if request.method == 'POST':
        email = request.form["USER_EMAIL"]
        password = request.form["USER_PASSWORD"]
        try:
            auth.sign_in_with_email_and_password(email, password)
            print('User Signed In')
            return render_template('index.html')
        except:
            return render_template('index.html')
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        email = request.form["NEW_USER_EMAIL"]
        password = request.form["NEW_USER_PASSWORD"]
        try:
            auth.create_user_with_email_and_password(email, password)
            return render_template('index.html')
        except:
            return 'Email Already in use'
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    post_path = db.child('Posts').child('entries')
    if request.method == 'POST':
        entry_title = request.form['POST_TITLE']
        entry_body = request.form['POST_BODY']
        try:
            post_path.child(entry_title).push(entry_body)
            print("Post Successful")
            return redirect('home')
        except:
            print('Post Failure')
            return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/load_data', methods=['GET', 'POST'])
def load_data():
    entry_titles = db.child('Posts').child('entries').get()
    for entry in entry_titles.each():
        title = entry.key()
        body = entry.val()
        print(entry.key())
        print(entry.val())
        body = db.child('Posts').child('entries').child(title).child('entry_body').get().val()
        return render_template('index.html', post_title=title, post_content=body)
    return render_template('index.html')

@app.route('/edit_entry', methods=['GET','POST'])
def edit_entry(title, body):
    if request.method == 'POST':
        get_entry_Title = request.form['Edit_entry_Title']
        get_entry_Body = request.form['Edit_entry_']
        if len(get_entry_Title) != 0:
            db.child('Posts').child('entries').update(get_entry_Title)
            db.child('Posts').child('entries').update(get_entry_Body)
        return redirect('home')



@app.route('/delete_entry', methods = ['GET', 'POST'])
def delete_entry():
    return redirect('home')








if __name__ == '__main__':
    app.run(debug=true)
