   # api/hello.py
   def handler(request, event):
       return {
           "statusCode": 200,
           "body": "Hello from Python!"
       }
