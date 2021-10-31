# Deloitte Test case

This webapp is built to solve the deloitte test case

## Assignment
<pre>
Build an API that will use a string as input and does a find and replace for certain words and outputs the result. For example: replace Google for Google©. 


Example input: “We really like the new security features of Google Cloud”
Expected output: “We really like the new security features of Google Cloud©”


The words that need to be replaced are listed below:

Oracle -> Oracle©
Google -> Google©
Microsoft -> Microsoft©
Amazon -> Amazon©
Deloitte -> Deloitte©

</pre>

## Solution

Make a POST call to /classify endpoint with the input string

Example:
Please use POSTMAN to make the following POST call 
```
https://python-full-apitest3010.azurewebsites.net/classify?input=We really like the new security features of Microsoft Cloud
```
