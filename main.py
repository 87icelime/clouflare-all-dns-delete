import requests

def get_dns_records(api_key, zone_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("\nFailed to get DNS records!")
        print(f"Error: {response.status_code}\n{response.text}")
        return None
    
    return response.json()["result"]

def delete_dns_record(api_key, zone_id, record_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print(f"Record ID {record_id} deleted successfully!")
    else:
        print(f"Failed to delete record ID {record_id}")
        print(f"Error: {response.status_code}\n{response.text}")

def main():
    api_key = input("Enter your API key: ")
    zone_id = input("Enter your Zone ID: ")

    dns_records = get_dns_records(api_key, zone_id)
    
    if dns_records is not None:
        for record in dns_records:
            delete_dns_record(api_key, zone_id, record['id'])

if __name__ == "__main__":
    main()
