import requests
import uuid
import json

cookies = {
    'ApplicationGatewayAffinityCORS': 'e8c539943b13b17d3b896ea1e8e3261f',
    'ApplicationGatewayAffinity': 'e8c539943b13b17d3b896ea1e8e3261f',
}

def generate_request_id():
    return uuid.uuid4()

def get_symptoms(parent_id, symptom_id):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'it-IT,it;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5,pt;q=0.4,de;q=0.3',
        'content-type': 'application/json',
        'origin': 'https://vc.vithoulkascompass.com',
        'priority': 'u=1, i',
        'referer': 'https://vc.vithoulkascompass.com/repertory/sid/0',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'source': 'api',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'vc-applicationid': '10',
        'vc-isguibillable': '2',
        'vc-languageid': '38',
        'vc-localeid': '26',
        'vc-repertoryid': '6',
        'vc-repertorylangid': '38',
        'vc-requestid': '1df8ea06-3028-4b59-ae13-e1e57cd126a1',
        'vc-sessionid': '7615dffb-0d2a-44b7-addc-6ac8b71b74ca',
        'vc-source': '1',
        'vc-timezone': 'Dateline Standard Time',
        'vc-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImtyaXNoY2hhdCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjQ5ODA0IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvYXV0aGVudGljYXRpb24iOiJabUo1T0V4RlNHaFRjRmRGTjJWSlZIcDVTVVZoVVQwOUxHcGpUWGh4TTNBelJHbHBOM2hTYmtsbWJtbGpTWGd3UmtoMk9FNHhXbTR3ZVcwdmRsQmtiRTloV2pnOSIsIm5iZiI6MTc3Mjg3OTIzMywiZXhwIjoxNzcyOTY1NjMzLCJpYXQiOjE3NzI4NzkyMzN9.8voP6JvRjRSqlzHFBbRHTDYKz7-7AQbvTp4Q_ChzG4c',
        'vc-username': 'krishchat',
        'vc-version': '20260109.1',
        # 'cookie': 'ApplicationGatewayAffinityCORS=e8c539943b13b17d3b896ea1e8e3261f; ApplicationGatewayAffinity=e8c539943b13b17d3b896ea1e8e3261f',
    }

    payload = {
    "Mode": 3,
    "SymptomId": symptom_id,
    "ParentSymptomId": parent_id,
    "MetadataId": parent_id,
    "SymptoIdList": "-"
    }

    json_data = {
        "Url": "RepertoryBrowser/RepertoryBrowser",
        "verb": "post",
        "jsonData": json.dumps(payload)
    }

    response = requests.post('https://vc.vithoulkascompass.com/vcproxy/Proxy/Call', cookies=cookies, headers=headers, json=json_data)
    if response.status_code == 200:
        print("successfull got symptoms")
        return response.json()["Data"]["RbSymptoms"]
    else:
        print("SYMPTOMS: ", response.status_code, response.json())
        return None

def get_remedies(parent_symptom, current_symptom):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'it-IT,it;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5,pt;q=0.4,de;q=0.3',
        'content-type': 'application/json',
        'origin': 'https://vc.vithoulkascompass.com',
        'priority': 'u=1, i',
        'referer': f'https://vc.vithoulkascompass.com/repertory/sid/{parent_symptom}',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'source': 'api',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'vc-applicationid': '10',
        'vc-isguibillable': '2',
        'vc-languageid': '38',
        'vc-localeid': '26',
        'vc-repertoryid': '6',
        'vc-repertorylangid': '38',
        'vc-requestid': '3265be47-771d-4da4-b2d0-3226c2b7c196',
        'vc-sessionid': '7615dffb-0d2a-44b7-addc-6ac8b71b74ca',
        'vc-source': '1',
        'vc-timezone': 'Dateline Standard Time',
        'vc-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImtyaXNoY2hhdCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjQ5ODA0IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvYXV0aGVudGljYXRpb24iOiJabUo1T0V4RlNHaFRjRmRGTjJWSlZIcDVTVVZoVVQwOUxHcGpUWGh4TTNBelJHbHBOM2hTYmtsbWJtbGpTWGd3UmtoMk9FNHhXbTR3ZVcwdmRsQmtiRTloV2pnOSIsIm5iZiI6MTc3Mjg3OTIzMywiZXhwIjoxNzcyOTY1NjMzLCJpYXQiOjE3NzI4NzkyMzN9.8voP6JvRjRSqlzHFBbRHTDYKz7-7AQbvTp4Q_ChzG4c',
        'vc-username': 'krishchat',
        'vc-version': '20260109.1',
    }
    
    payload = {
        "symptomid":current_symptom, 
        "trial": False
    }

    json_data = {
        'Url': 'RepertoryRemedies/GetSymptomRemediesLimits',
        'verb': 'post',
        'jsonData': json.dumps(payload),
    }

    response = requests.post('https://vc.vithoulkascompass.com/vcproxy/Proxy/Call', cookies=cookies, headers=headers, json=json_data)
    if response.status_code == 200:
        print("successfull got symptoms")
        return response.json()["Data"]["SymptomRemedyResponse"]
    else:
        print("REMEDIES: ", response.status_code, response.json())
        return None
