import json
import base64
import os
import tempfile
from langchain.document_loaders import PyPDFLoader
from llm_pipeline import llm_pipeline

def lambda_handler(event, context):
    try:
        if event['isBase64Encoded']:
            pdf_data = base64.b64decode(event['body'])
        else:
            pdf_data = event['body'].encode('utf-8')

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(pdf_data)
            tmp_file_path = tmp_file.name

        questions = llm_pipeline(tmp_file_path)

        os.remove(tmp_file_path)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Questions Generated Succesfully!', 'generated_question': questions}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
