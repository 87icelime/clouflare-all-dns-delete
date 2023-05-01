import requests

# API Key should have the permission to edit DNS
# Copy Zone ID 1) https://dash.cloudflare.com/ 2) Select The domain from where you want to delete all the DNS 3) Look at the right side to find your zone id
api_key = "YOUR_API_KEY"
zone_id = "YOUR_ZONE_ID"

# Get all DNS records using requests
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)
dns_records = response.json()["result"]

# Delete all DNS records 
for i in dns_records:
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{i['id']}"
    response = requests.delete(url, headers=headers)
    if response.status_code != 204:
        print(f"{i['type']} - {i['name']}  | Deleted Successfully! ")
