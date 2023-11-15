import json
import os
import subprocess


def readFile(path):
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


def writeFile(path, data):
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def reformatJson(data):
    collectionItems = data['item']
    for collectionItem in collectionItems:
        try:
            requestCollectionItems = collectionItem['item']
        except Exception as e:
            continue
        for requestCollectionItem in requestCollectionItems:
            try:
                requestItems = requestCollectionItem['item']
            except Exception as e:
                continue
            for requestItem in requestItems:
                requestCollectionItems.append(requestItem)
            requestItems.clear()
    return data


def generateHtmlDocs(path, envPath):
    postmaneratorCommand = [
        "postmanerator",
        "--output=" + generateOutputFile(path), "--collection=" + path,
        "-ignored-request-headers=Host,Accept",
        "-ignored-response-headers=Host,Date,Connection,X-Powered-By,X-Xdebug-Profile-Filename,Cache-Control,Content-Type,X-RateLimit-Limit,X-RateLimit-Remaining"
    ]
    if envPath:
        postmaneratorCommand.append("--environment=" + envPath)
    subprocess.run(postmaneratorCommand)


def generateOutputFile(path):
    return os.path.splitext(path)[0] + '.html'


file = input("Enter a postman collection file path: ")
envFile = input("Enter a postman environment file path: ")

jsonData = readFile(file)
writeFile(file, reformatJson(jsonData))
generateHtmlDocs(file, envFile)
