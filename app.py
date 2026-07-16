from flask inport Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
    return render_template ('index.html')

iff __name__=='__main__'
    app.run()