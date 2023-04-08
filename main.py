import requests
import os

url = "https://api.py9.dev/encryption.php"

def encrypt(text, key):
	data = {
		"type": "encrypt",
		"text": text,
		"key": key
	}
	response = requests.post(url, data=data)
	if response.ok:
		result = response.json()
		return result["result"]
	else:
		print("Error:", response.status_code, response.text)
		return None

def decrypt(text, key):
	data = {
		"type": "decrypt",
		"text": text,
		"key": key
	}
	response = requests.post(url, data=data)
	if response.ok:
		result = response.json()
		return result["result"]
	else:
		print("Error:", response.status_code, response.text)
		return None

os.system("title PyEncrypt")
os.system("color 0b")

def main():
	while True:
		os.system("cls" if os.name == "nt" else "clear")
		print("Welcome to PyEncrypt!\n")
		text = input("Text: ").strip()
		key = input("Key: ").strip()
		mode = input("Encrypt(1), Decrypt(2): ").strip()
		
		if mode == "1":
			print("\nEncrypting...\n")
			try:
				result = encrypt(text, key)
				if "<html>" in result:
					print("Something went wrong. The API may have timed out.\n")
				else:
					print(f"{result}\n")
			except Exception as e:
				print(f"Someting went wrong. Are you connected to the internet?\n")
		elif mode == "2":
			print("\nDecrypting...\n")
			try:
				result = decrypt(text, key)
				if "<html>" in result:
					print("Something went wrong. The API may have timed out.\n")
				else:
					print(f"{result}\n")
			except Exception as e:
				print(f"Someting went wrong. Did you enter the correct key?\n")
		else:
			print("Invalid mode! Try again.\n")

		input("Press enter to continue...")
main()
