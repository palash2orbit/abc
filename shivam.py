import requests

def get_location(api_key, address):
    base_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(base_url)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location
    else:
        return "Location not found."

# Use the function with your API key and address or coordinates
api_key = "YOUR_API_KEY"
phone_address = "123 Lost Phone Street, City, Country"
phone_location = get_location(api_key, phone_address)
print(phone_location)