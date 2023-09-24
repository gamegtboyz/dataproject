import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhN2VjY2YzZWExNTJlMzc0NGM4ZmQ3MTU2YWU3MDNiNCIsInN1YiI6IjY1MGZmMmUxNmY1M2UxMGFhNjc0ODdiMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.p7zibYT5sgFvY2UatKbG84dxs0fVUhSjv1PbeiL40NQ"
}

response = requests.get(url, headers=headers)

print(response.text)

