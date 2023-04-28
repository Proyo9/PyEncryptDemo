import requests

url = "https://api.py9.dev/encryption.php"

def encrypt(text: str, key: str) -> str:
	data = {
		"type": "encrypt",
		"text": text,
		"key": key
	}
	response = requests.post(url, data=data)
	if response.ok:
		result = response.json()
		if "<html>" in result: # Sometimes (pretty rarely) Cloudflare makes it return an HTML page instead of JSON D:<
			return 400
		return result["result"]
	else:
		print("Error:", response.status_code, response.text)
		return None
	
def encryptJSON(json: dict, key: str) -> str:
	json = str(json)
	encrypted = encrypt(json, key)
	if encrypted != 400:
		return encrypted
	else:
		return 400

def decrypt(text: str, key: str) -> str:
	data = {
		"type": "decrypt",
		"text": text,
		"key": key
	}
	response = requests.post(url, data=data)
	if response.ok:
		result = response.json()
		if "<html>" in result:
			return 400
		return result["result"]
	else:
		print("Error:", response.status_code, response.text)
		return None
	
def decryptJSON(text: str, key: str) -> dict:
	decrypted = decrypt(text, key)
	if decrypted != 400:
		return eval(decrypted)
	else:
		return 400
