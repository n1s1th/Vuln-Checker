import requests
import re

target_url = input("Enter the target URL: ")

# Test for SQL injection
payload = "' OR 1=1--"
r = requests.get(target_url + payload)
if r.status_code == 200:
  print("SQL injection may be possible.")

# Test for XSS
payload = "<script>alert(1)</script>"
r = requests.get(target_url + payload)
if payload in r.text:
  print("XSS vulnerability detected.")

# Test for open redirects
payload = "/redirect?url=http://evil.com" 
r = requests.get(target_url + payload)
if r.status_code == 200:
  print("Unvalidated redirect detected.")

# Test for CRLF injection
payload = "%0d%0aContent-Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0aContent-Length:%2035%0d%0a%0d%0a<html>CRLF Injection Test</html>"
r = requests.get(target_url + payload)
if r.status_code == 200 and "CRLF Injection Test" in r.text:
  print("CRLF injection may be possible.")

print("Scan completed.")