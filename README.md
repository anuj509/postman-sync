# Scenario
>I am was working on freelance project and I realised that I need to import postman collection and later other party reshared postman collection again and again I was fed up with re-import and hence created this simple script to reimport postman collection.

# Configuration
1. Obtain postman api key from [here](https://learning.postman.com/docs/developer/intro-api/#generating-a-postman-api-key)
2. Using postman get collections list https://api.getpostman.com/collections .Requires API Key as X-Api-Key request header or apikey URL query parameter.
3. Edit postman-sync.py replace line 7 url with your url shared from your colleague and line 10 replace with uuid from the response from collection list. 
