from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/artefatos_scrum')
def artefatos():
    return render_template('artefatos.html')

@app.route('/time_scrum')
def time_scrum():
    return render_template('timescrum.html')

@app.route('/scrum')
def scrum():
    return render_template('scrum.html')

@app.route('/probacklog')
def probacklog():
    return render_template('probacklog.html')

@app.route('/sprintbacklog')
def spbacklog():
    return render_template('sprintbacklog.html')

@app.route('/burndown')
def burndown():
    return render_template('burndown.html')

@app.route('/artefatos_arquivos_para_download')
def artefatos_download():
    return render_template('artefatosdownload.html')

@app.route('/avaliacao')
def avaliacao():
    return render_template('avaliacao.html')

@app.route('/eventos_scrum')
def eventos_scrum():
    return render_template('eventos-scrum.html')

@app.route('/scrumcases')
def scrum_cases():
    return render_template('scrumcases.html')

@app.route('/softskills')
def softskills():
    return render_template('softskills.html')

@app.route('/scrumvideo')
def scrum_video():
    return render_template('scrumvideo.html')

@app.route('/incrementovideo')
def incremento_video():
    return render_template('incrementovideo.html')

@app.route('/eventosvideo')
def eventosvideo():
    return render_template('eventosvideo.html')

if __name__=='__main__':
    app.run(debug=True, use_debugger=True, use_reloader=True)
