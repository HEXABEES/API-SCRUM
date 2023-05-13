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

@app.route('/quest-artefatos')
def quest_artefatos():
    return render_template('quest-artefatos.html')

@app.route('/quest-eventos')
def quest_eventos():
    return render_template('quest-eventos.html')

@app.route('/quest-final')
def quest_final():
    return render_template('quest-final.html')    

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

@app.route('/scrumcases_lego')
def scrum_cases_lego():
    return render_template('scrumcases_lego.html')

@app.route('/scrumcases_spotify')
def scrum_cases_spotify():
    return render_template('scrumcases_spotify.html')

@app.route('/scrumcases_microsoft')
def scrum_cases_microsoft():
    return render_template('scrumcases_microsoft.html')

@app.route('/scrumcases_google')
def scrum_cases_google():
    return render_template('scrumcases_google.html')

@app.route('/scrumcases_ibm')
def scrum_cases_ibm():
    return render_template('scrumcases_ibm.html')

@app.route('/scrumcases_amazon')
def scrum_cases_amazon():
    return render_template('scrumcases_amazon.html')

@app.route('/video_scrum_master')
def video_master():
    return render_template('video-master.html')

@app.route('/video_product_owner')
def video_po():
    return render_template('video-po.html')

@app.route('/video_time_scrum')
def video_time_scrum():
    return render_template('video-timescrum.html')

if __name__=='__main__':
    app.run(debug=True, use_debugger=True, use_reloader=True)
