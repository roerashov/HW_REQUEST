import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def get_params(self, file_name):
        return {
            'path':f'/{file_name}',
            'overwrite':'true'
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_list = ['1.txt','2.txt','3.txt']
        headers = { 
            'Content-Type':'application/json',
            'Authorization':'OAuth {}'.format(self.token)
        }
    
        for file in file_list:
            with open(file_path + file, 'rb') as f:
                responce_get = requests.get(self.upload_link, params=self.get_params(file), headers=headers)
                if responce_get.status_code == 200:
                    href = responce_get.json()['href']
                    responce_put = requests.put(href, files={'file':f})
                    if responce_put.status_code < 400:
                        print(f'Файл {file} успешно загружен на Яндекс.Диск')
                    else: print(f"Что-то пошло не так. Error {responce_put.status_code}")
                else: print(f"Что-то пошло не так. Error {responce_get.status_code}")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '/home/roman/Netology/HW_files_1/'
    token = 'здесь был токен'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)