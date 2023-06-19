

from flask import Flask, request, jsonify
from flask_cors import CORS

import os

from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

from google.oauth2 import service_account

import json

# # # # # # # # # #

app = Flask(__name__)
CORS(app)

# # # # # # # # # #

json_file = './datalake-2022-fda580d80d72.json'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

# project_id = 'datalake2022'
bucket_name = 'bucketdoalessandro'

# # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#

def upload_cs_file(bucket_name, source_file_name, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    return True

#upload_cs_file(bucket_name,
#               '/home/ego/Projetos/audio_gatherer/moz-todo-svelte/tmp_test/test.txt',
#               'test.txt')

#criando pasta:
#blob2 = storage.Client().bucket('bucketdoalessandro').blob('test/')
#blob2.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')

#

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # #

@app.route('/upload-audio', methods=["GET", "POST"])
def audio_work():    
    audioTeste = request.files
    print ('\n\n')
    print ("========================================================================")
    print ("========================================================================")
    print ("\nINÍCIO...")
    print ("\nSUCESSO! - áudio recebido")
    
    print('TESTE: ' , audioTeste)
    
    print('Marcador: ' , audioTeste["audio"].filename)
    name_mark = audioTeste["audio"].filename
    
    file_storage = audioTeste["audio"]    

    sourceFolder = './tmp/'  ### <<<
    arquivo = sourceFolder + name_mark
    
    if os.path.exists(arquivo):
        os.remove(arquivo)
        print(f"\nArquivo {arquivo} removido com sucesso!\n")    


    os.makedirs(os.path.dirname(sourceFolder), exist_ok=True)
    file_storage.save(arquivo)
        
    # # #
    
    print('Source file name: ' , arquivo)
    print('Destiny file name: ' , name_mark)
    
    upload_cs_file(bucket_name,
               './tmp/{}'.format(name_mark),
               '{}'.format(name_mark))
    
    print ("\nARQUIVO ENVIADO!")

    # # #
    
    print ("\nPROCESSO CONCLUÍDO!\n")
    print ("========================================================================")
    print ("========================================================================")
    # # #

    response = {
            'ok?': 'ok'
        }
    
    return jsonify(response), 200
    

# # # # # # # # # #

@app.route('/upload-info', methods=["GET", "POST"])
def info_work():
    infoTeste = request.get_json(force=True)
    print ('\n\n')
    print ("========================================================================")
    print ("========================================================================")
    print ("\nINÍCIO...")
    print ("\nSUCESSO! - informação recebida")
    
    print('TESTE: ' , infoTeste)
    print('Type: ' , type(infoTeste))
    
    with open("./tmp/{}_info.json".format(infoTeste['data']), "w") as fp:
        json_object = json.dump(infoTeste, fp)   
        print('json_object:')
        print(json_object)
        
    # # #
    
    print('Source file name: ' , "./tmp/{}_info.json".format(infoTeste['data']))
    print('Destiny file name: ' , "{}_info.json".format(infoTeste['data']))
    
    upload_cs_file(bucket_name,
               "./tmp/{}_info.json".format(infoTeste['data']),
               "{}_info.json".format(infoTeste['data']))
    
    print ("\nARQUIVO ENVIADO!")

    # # #
    
    print ("\nPROCESSO CONCLUÍDO!\n")
    print ("========================================================================")
    print ("========================================================================")
    # # #

    response = {
            'ok?': 'ok'
        }
    
    return jsonify(response), 200
    
    

# # # # # # # # # #

if __name__ == '__main__':
    app.run()
