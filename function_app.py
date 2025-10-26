# import datetime
# import json
# import azure.functions as func
# import logging
# from elasticsearch import Elasticsearch, helpers

# app = func.function_app()

# @app.blob_trigger(arg_name="myblob", path="raw/oxylabs",
#                                connection="AzureWebJobsStorage__blobServiceUri")

# def blob_index(blob_name):
#     logging.info(f"Indexing blob: {blob_name}")
#     if 'walmart' in blob_name:
#         logging.info(f"Blob {blob_name} is a Walmart blob.")
#         return 'walmart'
#     elif 'amazon_product' in blob_name:
#         logging.info(f"Blob {blob_name} is amazon_product blob.")
#         return 'amazon_product'
#     elif 'amazon_pricing' in blob_name:
#         logging.info(f"Blob {blob_name} is amazon_pricing blob.")
#         return 'amazon_pricing'
#     elif 'google_url' in blob_name:
#         logging.info(f"Blob {blob_name} is google_url blob.")
#         return 'google_url'

# def es_connection():
#     es_host = 'https://pec-elasticsearch-dev-b1f56f.es.eastus.azure.elastic.cloud:443'
#     es_api_key = 'ZUxINTZKa0JlVHUzcjNXbEZYa0s6SEVzU2JETVBCU2w1ZDZCWmZISTFwZw=='
#     return Elasticsearch(es_host, api_key=es_api_key, verify_certs=True, timeout=60)

# def blob2es(myblob: func.InputStream):
#     logging.info(f"Python blob trigger function processed blob"
#                 f"Name: {myblob.name}"
#                 f"Blob Size: {myblob.length} bytes")
    
#     es = es_connection()
#     blob_name=myblob.name
#     blob_name=blob_name.lower()
#     index_name=blob_index(blob_name)
#     blob_data = myblob.read()
#     json_data = json.loads(blob_data.decode('utf-8'))

#     if isinstance(json_data, list):
#         for record in json_data:
#             record["ingested_at"] = datetime.utcnow().isoformat()
#             es.index(index=index_name, document=record)
#     else:
#         json_data["ingested_at"] = datetime.utcnow().isoformat()
#         es.index(index=index_name, document=json_data)

# # This example uses SDK types to directly access the underlying BlobClient object provided by the Blob storage trigger.
# # To use, uncomment the section below and add azurefunctions-extensions-bindings-blob to your requirements.txt file
# # Ref: aka.ms/functions-sdk-blob-python
# #
# # import azurefunctions.extensions.bindings.blob as blob
# # @app.blob_trigger(arg_name="client", path="raw/oxylabs",
# #                   connection="peclaravelstoragedev001_STORAGE")
# # def blob2es(client: blob.BlobClient):
# #     logging.info(
# #         f"Python blob trigger function processed blob \n"
# #         f"Properties: {client.get_blob_properties()}\n"
# #         f"Blob content head: {client.download_blob().read(size=1)}"
# #     )


import azure.functions as func
import logging

function_app2 = func.Blueprint()


@function_app2.route(route="http_trigger", auth_level=func.AuthLevel.FUNCTION)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )