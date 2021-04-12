#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify, send_file, make_response
from werkzeug.exceptions import RequestURITooLarge
from werkzeug.wrappers import Response
import youtube_dl
import os
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/slashing', methods=['GET'])
def slashing_api():
    url = request.args.get('url')
    mp3_file_name = get_mp3(url)
    
    # extract vocal from source.mp3 file
    os.system('echo spleeter_starts')
    os.system('python -m spleeter separate -i source.mp3 -p spleeter:4stems -o output')
    
    # delete source.mp3 file
    os.system('del source.mp3')
    
    # for debug
    print('spleeter finished')
    
    # send vocals.wav to deepspeech server
    url = 'http://3.94.121.170/receive.php'
    files = {'uploadFile': open('./output/source/vocals.wav', 'rb')}
    res = requests.post(url, files = files)
    
    # resp = make_response(
    #     send_file("./output/source/vocals.wav", mimetype="audio/wav", as_attachment=True, attachment_filename="vocals.wav")
    # )
    # send vocal.wav (extracted from source.mp3) to check
    
    return str(res.text)

def get_mp3(url):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url, download=False
    )
    file_name = "source.mp3"
    options = {
        'format' : 'bestaudio/best',
        'keepvideo' : False,
        'outtmpl' : file_name,
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }]
    }
    
    with youtube_dl.YoutubeDL(options) as download:
        download.download([url])
        
    return file_name

if __name__ == '__main__':
    app.run(host = '0.0.0.0')


# In[ ]:




