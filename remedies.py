import requests
import json

cookies = {
    'ApplicationGatewayAffinityCORS': '1b403a0d9b25d285bdbc14898e4886da',
    'ApplicationGatewayAffinity': '1b403a0d9b25d285bdbc14898e4886da',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'it-IT,it;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5,pt;q=0.4,de;q=0.3',
    'content-type': 'application/json',
    'origin': 'https://vc.vithoulkascompass.com',
    'priority': 'u=1, i',
    'referer': 'https://vc.vithoulkascompass.com/mycompass/summary?username=krish.chat@gmail.com&password=krish123&LoginForm%5BajBrowser%5D=%7B%7D&LoginForm%5Breferer%5D=',
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
    'vc-requestid': '610a76ee-b314-4cd9-8409-b79b67b00cd0',
    'vc-sessionid': '148ad98a-6a6f-4837-94e1-c822ea2b6f61',
    'vc-source': '1',
    'vc-timezone': 'Dateline Standard Time',
    'vc-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImtyaXNoY2hhdCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjQ5ODA0IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvYXV0aGVudGljYXRpb24iOiJkRkJvTm10MmJWQkpVWGt3ZEhNeVNFMW5WbkI0VVQwOUxEbGtSbGxUTm1WRFpWUm9OVk5yVDNOa1YzTmtUakphYUVkcFYyRlNjMGhVTVZobVdtOTBiRVJ1VjBrOSIsIm5iZiI6MTc3MjgzMjU3MywiZXhwIjoxNzcyOTE4OTczLCJpYXQiOjE3NzI4MzI1NzN9.vnBrrAlOaaQOpXLqC0bHIIa-PSSMm5g9SXjODISvEl4',
    'vc-username': 'krishchat',
    'vc-version': '20260109.1',
    # 'cookie': 'ApplicationGatewayAffinityCORS=1b403a0d9b25d285bdbc14898e4886da; ApplicationGatewayAffinity=1b403a0d9b25d285bdbc14898e4886da',
}

json_data = {
    'Url': 'RepertoryRemedies/GetRemediesInfo',
    'verb': 'post',
    'jsonData': '{"empty":0}',
}

response = requests.post('https://vc.vithoulkascompass.com/vcproxy/Proxy/Call', cookies=cookies, headers=headers, json=json_data)

data = response.json()



f = open("data/remedies.json", "w")
f.write(json.dumps(data, indent=2))
f.close()