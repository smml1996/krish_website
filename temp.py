import requests

cookies = {
    'ApplicationGatewayAffinityCORS': 'e8c539943b13b17d3b896ea1e8e3261f',
    'ApplicationGatewayAffinity': 'e8c539943b13b17d3b896ea1e8e3261f',
}

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
    'vc-requestid': '6b9c7146-1d3d-41fb-88a6-1758299cb58b',
    'vc-sessionid': '697b9b46-7e63-4c92-8c8a-9a9ad565abbc',
    'vc-source': '1',
    'vc-timezone': 'Dateline Standard Time',
    'vc-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImtyaXNoY2hhdCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjQ5ODA0IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvYXV0aGVudGljYXRpb24iOiJRbGh6VmxRd1pYWjZLMEpZYTFwUk1tTkNkVGsxUVQwOUxETkVTRmxrTjBOWWRrUnlZMWxoTURod1duWlRNbkZxUzJsWlpVdFFjeTl5YTJGNGNHUmpRWGhMWVVVOSIsIm5iZiI6MTc3Mjk5NjM1NiwiZXhwIjoxNzczMDgyNzU2LCJpYXQiOjE3NzI5OTYzNTZ9.Ic-gxdJ0fRaVmNxZXcsP0m2j5INWenq5bdaEvuk2srA',
    'vc-username': 'krishchat',
    'vc-version': '20260109.1',
    # 'cookie': 'ApplicationGatewayAffinityCORS=e8c539943b13b17d3b896ea1e8e3261f; ApplicationGatewayAffinity=e8c539943b13b17d3b896ea1e8e3261f',
}

json_data = {
    'Url': 'RepertoryRemedies/GetSymptomRemediesLimits',
    'verb': 'post',
    'jsonData': '{"symptomid":6017,"trial":false}',
}

response = requests.post('https://vc.vithoulkascompass.com/vcproxy/Proxy/Call', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"Url":"RepertoryRemedies/GetSymptomRemediesLimits","verb":"post","jsonData":"{\\"symptomid\\":6017,\\"trial\\":false}"}'
#response = requests.post('https://vc.vithoulkascompass.com/vcproxy/Proxy/Call', cookies=cookies, headers=headers, data=data)