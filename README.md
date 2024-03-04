# Куда пойти - Москва глазами туриста
Сайт о самых интересных местах Москвы.
![where_to_go](https://i.ibb.co/FV0ZMGV/stranica.png)
## Как установить:
Python3.11 должен быть уже установлен. 
Затем используйте `pip`  для установки зависимостей:
```shell
pip install -r requirements.txt
```
Создайте файл **.env** в корне репозитория, добавьте в него **переменные окружения**:
- SECRET_KEY — секретный ключ приложения. Используется для криптографической подписи, должен быть установлен в уникальное значение.
- ALLOWED_HOSTS — список допустимых доменных имен, которые могут обслуживаться приложением. Это важная мера безопасности, которая помогает предотвратить атаки на заголовок HTTP Host.
- DEBUG — значение, включающее режим отладки. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. По умолчанию - `False`.
Создайте базу данных:
```shell
python manage.py makemigrations
python manage.py migrate
```
Создайте администратора:
```sh
python manage.py createsuperuser
```

### Запуск:
Запустите сервер:
```shell
python manage.py runserver
```
### Заполнение базы данных:
Заполнить базу данных возможно в ручную через администраторскую панель, а так же через команду **load_place**:
```shell
python manage.py load_place https://адрес/json/файла.json
```
структура json-файла: [пример](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%92%D0%BE%D0%B4%D0%BE%D0%BF%D0%B0%D0%B4%20%D0%A0%D0%B0%D0%B4%D1%83%D0%B6%D0%BD%D1%8B%D0%B9.json).
![визуальный пример](https://i.ibb.co/dgZt0z2/image.png)
