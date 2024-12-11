from time import sleep
import hashlib

class User:
# используется hashlib для хеширования строк и сохранения числа через конвертацию хеша в целое число.

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = self.hash_password(password)                # Хешируем пароль при создании объекта
        self.age = int(age)

# используем декоратор @staticmethod для определения методов которые не требуют доступа к экземпляру класса, т.е.
# не зависят от состояния экземпляра класса
    @staticmethod
    def hash_password(password):
        hashed = hashlib.sha256(password.encode()).hexdigest()         # Хешируем строку
        return int(hashed, 16)                                         # Преобразуем хэш в число для соответствия ТЗ

    def check_password(self, password):
        return self.password == self.hash_password(password)           # Проверяет введенный пароль с хранящимся хэшем

    def __str__(self):
        return self.nickname

class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = bool(adult_mode)

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and user.check_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверный логин или пароль.")

    def register(self,nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован.")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    def get_videos(self, search_word):
        list_film = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                list_film.append(video.title)
        return list_film

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    break
                else:
                    print(f"Смотрим видео: '{title}' ")
                for time_now in range(1, video.duration + 1):
                    sleep(1)
                    print(f"{time_now}s", end=' ', flush=True)  # используется метод flush() чтобы сбросить время
                                                                # просмотра видео после воспроизведения.
                print('Конец видео')
                return
        print(f"Видео '{title}' не найдено.")



# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Вывод в консоль:
#
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist

