# Deloitte Test case

This webapp is built to solve the deloitte test case

## Assignment

Build an API that will use a string as input and does a find and replace for certain words and outputs the result. For example: replace Google for Google©. 


Example input: “We really like the new security features of Google Cloud”
Expected output: “We really like the new security features of Google Cloud©”


The words that need to be replaced are listed below:

Oracle -> Oracle©
Google -> Google©
Microsoft -> Microsoft©
Amazon -> Amazon©
Deloitte -> Deloitte©

## Solution
Post the input to /classify endpoint

Make a POST call to /classify endpoint with the input string

Example:
```
curl --location --request POST 'http://127.0.0.1:5000/classify?input=We%20really%20like%20the%20new%20security%20features%20of%20Google%20Cloud'
```
