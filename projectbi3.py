import re
import requests
from urllib.parse import urlparse

def detect_phishing(url):
  
  
  parsed_url = urlparse(url)
  if not parsed_url.scheme or not parsed_url.netloc or not parsed_url.path:
    return True 

  
  if len(url) > 70:
    return True  
  if url.count(".") > 2:
    return True  
  if re.search(r"[-]{2,}", url):
    return True  

 
  domain_name = parsed_url.netloc.lower()
  if any(keyword in domain_name for keyword in ["login", "password", "account", "confirm"]):
    return True

  


  try:
    requests.head(url)  
    return False 
  except requests.exceptions.RequestException:
    return True  

def prevent_interaction(url):
  
  print("Phishing attempt detected. Blocking URL:", url)

def main():
  url = input("Enter the URL to check: ")

  if detect_phishing(url):
    prevent_interaction(url)
  else:
    print("URL is likely legitimate.")

if __name__ == "__main__":
  main()

from projectbi3 import detect_phishing

