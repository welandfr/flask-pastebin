# Pastebin API (Flask for CSC Rahti)

API for pasting strings and returning the last (or specified index) string. 

Maybe files in the future.

### POST:

```
POST https://{{url}}/pastebin?api_key={{api_key}}
Content-Type: application/json

{ "type": "str", "val": "I pasted this" }

```
### GET latest paste (request):
```
GET https://{{url}}/pastebin?api_key={{api_key}}
```

### GET (response):
```
{ "type": "str", "val": "I pasted this", "len": 2 }
```

### GET specific paste (request): 
Latest paste is 0, for example 2:
```
GET https://{{url}}/pastebin/2?api_key={{api_key}}
```

### DELETE all:
Clear all values
```
DELETE https://{{url}}/pastebin?api_key={{api_key}}
```


### DELETE specific:
Latest paste is 0, for example 2:
```
DELETE https://{{url}}/pastebin/2?api_key={{api_key}}
```