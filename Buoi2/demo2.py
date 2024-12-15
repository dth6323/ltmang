import requests

data  = {
    'id' :1,
    'title' : 'abcdef',
    'body' :'test put',
    'userID' :1
}
response = requests.get('https://jsonplaceholder.typicode.com/posts', json=data)
print('status code:', response.status_code)
print('body', response.text)
    
    