import requests

# Make a request to the Scryfall API to retrieve a card
response = requests.get("https://api.scryfall.com/cards/named", params={"exact": "Demonic Tutor"})

# Parse the JSON data in the response
card_data = response.json()

# Print the name of the card
print(card_data["name"])
