import boto3
import urllib.request
from datetime import datetime

def lambda_handler(event, context):
    # Obtener la fecha actual
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # URL de la página del tiempo
    weather_url = 'https://www.eltiempo.com/' 
    
    # Descargar la página
    response = urllib.request.urlopen(weather_url)
    weather_page = response.read()
    
    # Configurar el cliente de Amazon S3
    s3 = boto3.client('s3')
    
    # Nombre del bucket y clave del archivo
    bucket_name = 'bigdatalaura'  # Reemplaza con el nombre de tu bucket
    file_key = f'{current_date}.html'
    
    # Subir el archivo a Amazon S3
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=weather_page)
    
    return {
        'statusCode': 200,
        'body': 'Página del tiempo descargada y subida exitosamente a S3.'
    }