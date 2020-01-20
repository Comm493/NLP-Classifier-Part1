import urllib
import urllib.request
import json

url = 'https://ussouthcentral.services.azureml.net/workspaces/bead0e202b29437d9283b3c06d52819a/services/c730aba8ba3945c3a9da2703930989a4/execute?api-version=2.0&details=true'
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

#Some text to classify
comment_text = str(input("What comment do you want to analyze:\n"))

if comment_text != "":
    data =  {
        "Inputs": {
                "input1":
                {
                    "ColumnNames": ["text_column"],
                    "Values": [ [ comment_text ], ]
                },        },
            "GlobalParameters": {
            }
        }

    body = str.encode(json.dumps(data))
    req = urllib.request.Request(url, body, headers)
    response = urllib.request.urlopen(req)
    
    result = response.read()
    print(result)
    comment_text = str(input("What comment do you want to analyze:\n"))
