import requests

# The standard API endpoint for calculating a route
url = "https://apis.tollguru.com/toll/v2/origin-destination-waypoints"

# The API requires an authorization header
headers = {
    "x-api-key": "YOUR_API_KEY_HERE", # We are leaving this as a placeholder for now
    "Content-Type": "application/json"
}

# Example route: Driving from North Dallas to DFW Airport
payload = {
    "from": {
        "lat": 33.0198,
        "lng": -96.6989
    },
    "to": {
        "lat": 32.8998,
        "lng": -97.0403
    },
    "vehicle": {
        # 2AxlesAuto is the standard classification for a 2023 Subaru Forester
        "type": "2AxlesAuto" 
    }
}

print("Pinging the toll API...")

try:
    # Send a POST request because we are submitting route data
    response = requests.post(url, json=payload, headers=headers)
    
    # A 200 code means total success
    if response.status_code == 200:
        data = response.json()
        print("Success! Data received.")
        print(data)
        
    # A 403 code means the request worked, but the API key is missing/invalid
    elif response.status_code == 403:
        print("Connection successful! (Received 403 Forbidden: You just need to swap in a real API key to see the live price).")
        
    else:
        print(f"Failed. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")