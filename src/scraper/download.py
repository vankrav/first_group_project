import requests

class Downloader:
    def __init__(self, url, params, method):
        self.url = url
        self.params = params
        self.method = method
        if self.method == "GET":
            self.response = requests.get(url = self.url, params=self.params)
        else:
            self.response = requests.post(url = self.url, params=self.params)

    def get_html(self):
        return self.response.text
    def save(self, file_path):
        with open(file_path, "w") as f:
            f.write(self.response.text)

# URL = "http://www.hmn.ru/index.php"      # тут используйте адрес вашего сайта
# PARAMS = {                               # эти параметры также индивидуальны для страницы, которую вы скрапите
#     "index": 8,
#     "value": 22113,
#     "tz": 3,
#     "start": "2022-11-20",
#     "fin": "2022-11-28",
#     "x": 10,
#     "y": 5,
# }
# FILE_PATH = "weather.html"               # используйте ваше название. Будет более понятно, если будете исполь-
#                                          # зовать расширение html, т.к. в этом файле будет код html-страницы
#
# downloader = Downloader(url=URL, params=PARAMS, method="GET")
# print(downloader.get_html())
# downloader.save(FILE_PATH)