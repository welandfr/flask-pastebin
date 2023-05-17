# Pastebin API (Flask for CSC Rahti)

API for pasting strings and returning the last (or specified index) string. 

Maybe files in the future.

### POST:

```
POST {{url}}/pastebin?api_key={{api_key}}
Content-Type: application/json

{ "type": "str", "val": "I pasted this" }

```
### GET (request):
```
GET {{url}}/pastebin?api_key={{api_key}}
```

### GET (response):
```
{ "type": "str", "val": "I pasted this" }
```

### Optional GET (request):
add `idx` param to get older pastes (latest paste is 0)

```
GET {{url}}/pastebin?api_key={{api_key}}&idx=2
```