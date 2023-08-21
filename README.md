# Vuln-Checker
Here is a basic Python script that can check a website for some common vulnerabilities,
This sends some basic payloads to test for common bugs like SQLi, XSS, open redirects, and CRLF injection. It doesn't cover everything, but can give you an idea where to start looking. You would need to expand on this base script adding more checks for other vulnerabilities.

Some key points:

    Use the requests module to send payloads and analyse responses
    Print output for detected issues
    Iterate through different payloads for each vulnerability type
    Add checks for other bugs like command injection, directory traversal etc.
    Use regex to match patterns in responses
    Handle edge cases and validate potential findings

Enjoy!
