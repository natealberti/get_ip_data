import requests

# api configuration
ip = '{IP ADDRESS}'
token = '{TOKEN}'
url = f'https://ipinfo.io/{ip}?token={token}'
url_formatted = url.format(ip=ip, token=token)
req = requests.get(url)

# data sorting
content = str(req.content)
split_content = content.split('\\n')

# cleaning the slices up
data = split_content
for i in range (len(split_content)):
    data[i] = split_content[i].replace("\"", "").replace("  ", "").replace(",", "")


# formatting and printing output
del data[0]
[print(data[i]) for i in range(len(data)-1)]