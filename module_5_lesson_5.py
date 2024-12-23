from time import sleep


# ___________________________________________________________________________________________________________________
class UrTube:
# ___________________________________________________________________________________________________________________
# Атрибуты:

# users(список объектов User),
    users = []

# videos(список объектов Video),
    videos = []

# current_user(текущий пользователь, User)
    current_user = None

# ___________________________________________________________________________________________________________________
    def __str__(self):
        return 'Urban university Tube'

    # def __contains__(self, item):
    #     return item in UrTube.videos.title

# ___________________________________________________________________________________________________________________
# Метод register, который принимает три аргумента:
# nickname, password, age, и добавляет пользователя в список,
# если пользователя не существует (с таким же nickname).
# Если существует, выводит на экран: "Пользователь {nickname} уже существует".
# После регистрации, вход выполняется автоматически.

    def register(self, nickname:str, password:str, age:int):
        password = hash(password)
        for user in UrTube.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        new_user = User(nickname, password, age)
        UrTube.users.append(new_user)
        UrTube.current_user = new_user

# ___________________________________________________________________________________________________________________
# Метод log_in, который принимает на вход аргументы:
# nickname, password и пытается найти пользователя в users с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    def log_in(self, nickname:str, password:str):
        password = hash(password)
        find = False
        for user in UrTube.users:
            if nickname == user.nickname and password == user.password:
                UrTube.current_user = user
                print(f'Вход в аккаунт выполнен {user.nickname}')
                find = True
        if not find:
            print('Неверное сочетание логина и пароля')

# ___________________________________________________________________________________________________________________
# Метод log_out для сброса текущего пользователя на None.

    def log_out(self):
        if UrTube.current_user is not None:
            UrTube.current_user = None
            print('Вы вышли из аккаунта')

# ___________________________________________________________________________________________________________________
# Метод add, который принимает неограниченное кол-во объектов класса Video
# и все добавляет в videos, если с таким же названием видео ещё не существует.
# В противном случае ничего не происходит.

    def add(self, *videolist:object):
        for video in videolist:
            if not any (video.title == search_vid.title for search_vid in UrTube.videos):
                UrTube.videos.append(video)
            # else:
            #     print('Видео с таким названием уже существует')

# ___________________________________________________________________________________________________________________
# Метод get_videos, который принимает поисковое слово и возвращает
# список названий всех видео, содержащих поисковое слово.
# (не учитывать регистр).

    def get_videos(self, search:str):

        search_result = []

        for element in UrTube.videos:

            if search.lower() in element.title.lower():
                search_result.append(element.title)

        if search_result == []:
            search_result = ['Видео не найдено']

        return search_result

# ___________________________________________________________________________________________________________________
# Метод watch_video, который принимает название фильма,
# если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится,
# если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию
# sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
# В противном случае выводить в консоль надпись:
# "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
# т.к. есть ограничения 18+. Должно выводиться сообщение:
# "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"

    def watch_video(self, watch_video:str, start_time:int = 0):

        if UrTube.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in UrTube.videos:

            if watch_video == video.title:

                if video.adult_mode and UrTube.current_user.age < 18:
                    print('Вам нет 18 лет, видео недоступно к просмотру')
                    return

                # Не стал делать проверку, что время старта меньше чем продолжительность видео
                # Не стал делать проверку, если текущее время старта по умолчанию отличается от 0
                video.time_now = start_time
                print(f'Идёт показ видео: {watch_video}. Просмотр начался с {video.time_now} секунды')
                for watch in range(video.time_now, video.duration):
                    sleep(1)
                    video.time_now += 1
                    print(video.time_now, end=' ')
                print('Конец видео')
                video.time_now = 0
# ___________________________________________________________________________________________________________________


# ___________________________________________________________________________________________________________________
class Video:
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атрибуты: title(заголовок, строка),
# duration(продолжительность, секунды),
# time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
    def __init__(self, title:str, duration:int, time_now:int = 0, adult_mode:bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return  self.title
    #
    # def __contains__(self, item):
    #     return item.title in UrTube.videos.title
# ___________________________________________________________________________________________________________________


# ___________________________________________________________________________________________________________________
class User:
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атрибуты: nickname(имя пользователя, строка),
# password(в хэшированном виде, число),
# age(возраст, число)
    def __init__(self, nickname:str, password:str, age:int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return  self.nickname
# ___________________________________________________________________________________________________________________


# ___________________________________________________________________________________________________________________
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# ___________________________________________________________________________________________________________________
# Дополнительные проверки
print(ur.get_videos('карась'))
ur.log_out()
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Лучший язык программирования 2024 года', 185)

v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 120, adult_mode=True)
ur.add(v1, v2)
ur.add(v1, v2)

ur.log_out()


ur.log_in('vasya_pupkin', 'lol')
ur.log_out()

