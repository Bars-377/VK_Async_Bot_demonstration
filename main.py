from multiprocessing import Process
from vkbottle import BaseStateGroup
from vkbottle.bot import Bot, Message
from vkbottle import CtxStorage

import aiofiles
import configparser
import logging

from keyboards import *
from base import *

# Чтение конфигурации
config = configparser.ConfigParser()
config.read("config.ini")

from loguru import logger

# Отключаем стандартный логгер vkbottle
logging.getLogger("vkbottle").disabled = True

# Настраиваем loguru, чтобы игнорировать логи
logger.remove()  # Удаляем все существующие обработчики loguru

# # Создаем логгер для модуля vkbottle
# logger = logging.getLogger("vkbottle")
# logger.setLevel(logging.CRITICAL)

# # Создаем логгер для модуля mysql.connector
# logging.getLogger("mysql.connector").setLevel(logging.CRITICAL)

# # Создаем логгер для модуля urllib3
# logging.getLogger("urllib3").setLevel(logging.CRITICAL)  # Игнорируем сообщения уровня DEBUG и INFO

# """ЭТО ИГНОРИРУЕТ 'message_read' is not a valid GroupEventType"""
# # Устанавливаем обработчик для игнорирования сообщений уровня ERROR
# class IgnoreErrors(logging.Filter):
#     def filter(self, record):
#         return record.levelno != logging.ERROR
# # Добавляем фильтр для игнорирования сообщений об ошибке
# logger.addFilter(IgnoreErrors())
# # Пример использования логгера
# logger.error("'message_read' is not a valid GroupEventType")  # Это сообщение будет игнорироваться

# # Устанавливаем обработчик для игнорирования сообщений уровня ERROR
# class IgnoreErrors_1(logging.Filter):
#     def filter(self, record):
#         return record.levelno != logging.DEBUG
# # Добавляем фильтр для игнорирования сообщений об ошибке
# logger.addFilter(IgnoreErrors_1())
# # Пример использования логгера
# logger.error("vkbottle:logging is used as the default logger, but we recommend using loguru. It may also become a required dependency in future releases.")  # Это сообщение будет игнорироваться

def process_1():
    async def debug_print(message, user_id):
        import inspect
        # Получаем информацию о текущем фрейме
        frame = inspect.currentframe()
        # Получаем номер строки, где вызвана функция debug_print
        line_number = frame.f_back.f_lineno
        # Печатаем сообщение с номером строки
        print(f"Line {line_number}: {message}, user_id: {user_id}")

    ctx = CtxStorage()
    bot = Bot(token=config["VKONTAKTE"]["token"])

    filials_id = {
                'frunze': '533',
                'derb': '461',
                'pushk': '641',
                'tvers': '689',
                'alex': '425',
                'zato': '431',
                'ziryansk': '665',
                'kojevn': '377',
                'frunze_11a': '557',
                'frunze_90': '389',
                'sovp': '449',
                'naber': '677',
                'bolsh_sar': '605',
                'zonaln': '443',
                'pervom': '719',
                'anast': '659',
                'zork': '479',
                'malin': '713',
                'mejen': '731',
                'moryak_zaton': '551',
                'novopokrovka': '407',
                'novoroj': '725',
                'pesochno': '467',
                'turunt': '623',
                'strez': '347',
                'asino': '545',
                'balyar': '635',
                'cedar': '455',
                'voronino': '395',
                'kislovka': '491',
                'moscow_tract': '371',
                'kolpashevo': '611',
                'krivosheino': '593',
                'molchanovo': '503',
                'zone_station': '443',
                'peaceful': '401',
                'victory': '629',
                'dawn': '539',
                'parabel': '2894026',
                'pervomaiskoye': '719',
                'butkat': '515',
                'bogashevo': '575',
                'vershinino': '437',
                'volodino': '647',
                'voronovo': '707',
                'zorkaltsevo': '479',
                'itatka': '383',
                'kaltay': '329',
                'kornilovo': '419',
                'red_yar': '563',
                'robin': '599',
                'mogochino': '335',
                'monastery': '617',
                'narga': '497',
                'novopokrovka': '407',
                'novoselovo': '413',
                'october': '527',
                'sand_dubrovka': '467',
                'rybalovo': '521',
                'old_yuvala': '653',
                'trubachevo': '671',
                'tungusovo': '473',
                'turuntayevo_selo': '623',
                'urtam': '569',
                'chazhemto': '485',
                'chilino': '359',
                'сity_strezhevoy': '347',
                'dom_predpr': '371',
                'gaspr': '342595',
                'lenin_ave': '683',
                'per_sovpartshkolny': '449',
                'serg': '432256',
                'teguld': '365',
                'chain': '695',
                'meln': '701',
                'razv': '509',
                'oreh': '432194',
                'ulu': '432212',
                'komsom': '432239'
            }

    services_id = {
                'zagran': '3a276fae-0959-44a5-a6eb-f87a0b5650b4',
                'snils': '976eb69d-83cb-42b9-893a-926e11956393',
                'dokum': '5b0b693c-231e-4f40-8d64-c275c7d9217c',
                'registr': '8f5e514e-dcce-41cf-8b56-38db6af10056',
                'sved': '77a009c9-f183-4ac6-9275-ae9ff7b7d4b9',
                'prekr': '14ea190f-e597-4c68-a77a-a697d826101b',
                'opeka': '99def219-6ee8-47e4-9508-b77b2042a332',
                'passport': '78402a5a-321b-4213-a081-a32a29c0317d',
                'residency': 'd0ec6424-bfdf-492d-888b-76b9060726b4',
                'lgot': 'c155b875-cd2c-4dc9-95a4-bd68ff0d4f1b',
                'sprav': '93e9047a-b55f-4d43-b10d-554f5bd3c080',
                'smk': 'dfa9a351-dc67-42da-b33c-e1fa5da95b90',
                'posob': '97d144a1-14ab-4381-ad05-5575c54e677d',
                'gosusl': 'f94fd42b-611b-460a-8270-059526b40d35',
                'predprin': '97ddcd3f-227b-4450-a62d-c7da82084020',
                'deklar': '0666b35c-0383-441e-a158-cc9bcafffef7',
                'dogov': '36340cfb-7864-4ced-81df-9845bd73cfe2',
                'udost': '9fcfcb68-befb-42e5-ae3c-8b05f3dfe3c2',
                'bankr': 'fb6348b0-6b0c-4aa3-9deb-7385894beb39',
                'kons_rosres': '81914e42-5ce6-477a-a49c-52299d37f8ca',
                'kons_rosp': '52cc58f4-2f75-46b2-8065-abe1c6ed6889',
                'viplata': 'c205f225-d3b0-4183-a424-d215317632ab',
                'gazif': 'ae063235-ef12-4166-922b-78e307060c5d',
                'notar': '4b7b705a-8b12-4f07-b26f-d573e6f096c2',
                'krupn': '9a1e3d5a-9f3d-4bb4-96ea-1096cc5cb703',
                'digital': '79d77421-c234-4f8b-a643-bb31c79d388d'
            }

    services_name = {
                'zagran': 'Загранпаспорт',
                'zagran_5': 'Загранпаспорт (5 лет)',
                'snils': 'СНИЛС',
                'dokum': 'Получение документов',
                'registr': 'Регистрация ПМЖ/ПМП',
                'sved': 'Сведения из ЕГРН',
                'prekr': 'Прекращение права',
                'opeka': 'Опека',
                'passport': 'Паспорт',
                'residency': 'Прописка',
                'lgot': 'Льготы',
                'sprav': 'Справка УМВД',
                'smk': 'МСК',
                'posob': 'Пособия',
                'gosusl': 'Портал Госуслуги',
                'predprin': 'Предприниматель',
                'deklar': 'Декларация',
                'dogov': 'Договор',
                'udost': 'Удоствоверение личности',
                'bankr': 'Банкротство',
                'kons_rosres': 'Консультация Росресстра',
                'kons_rosp': 'Консультация Роспотребнадзора',
                'viplata': 'Выплаты',
                'gazif': 'Газификация',
                'notar': 'Нотариус',
                'krupn': 'Крупные сделки',
                'digital': 'Консультация юриста по цифровой среде'
            }

    privileges = {
                '1_1':'Ветеран Великой Отечественной войны',
                '2_2':'Инвалид 1 группы',
                '3_3':'Инвалид 2 группы (без возможности самостоятельно передвигаться)',
                '4_4':'Герой Российской Федерации/Герой Советского Союза/Герой Социалистического Труда/Герой Труда Российской Федерации, полный кавалер ордена Славы',
                '5_5':'Инвалид боевых действий',
                '6_6':'Родители (законные представители) детей-инвалидов',
                '7_7':'Граждане, достигшие возраста 80 лет'
            }

    numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

    times_list = {'0800', '0900', '1000', '1100', '1200', '1300', '1400', '1500', '1600', '1700', '1800', '1900'}

    bid_locations = {
        '01': 'Отдел ОГКУ "ТО МФЦ" по Советскому району г.Томска',
        '02': 'Отдел ОГКУ "ТО МФЦ" по Октябрьскому району г.Томска',
        '03': 'Отдел ОГКУ "ТО МФЦ" по Кировскому району г. Томска',
        '04': 'Отдел ОГКУ "ТО МФЦ" по Ленинскому району г.Томска',
        '05': 'Отдел ОГКУ "ТО МФЦ"  по Асиновскому району',
        '06': 'Отдел ОГКУ "ТО МФЦ"  по Кожевниковскому району',
        '07': 'Отдел ОГКУ "ТО МФЦ"  по Колпашевскому району',
        '08': 'Отдел ОГКУ "ТО МФЦ" по Чаинскому району',
        '09': 'Отдел ОГКУ "ТО МФЦ" по Молчановскому району',
        '10': 'Отдел ОГКУ "ТО МФЦ" по ЗАТО Северск',
        '11': 'Отдел ОГКУ "ТО МФЦ" по Кривошеинскому району',
        '12': 'Отдел ОГКУ "ТО МФЦ" по Шегарскому району',
        '13': 'Отдел ОГКУ "ТО МФЦ" по городу Кедровому',
        '14': 'Отдел ОГКУ "ТО МФЦ" по Верхнекетскому району',
        '15': 'Отдел ОГКУ "ТО МФЦ" по Александровскому району',
        '16': 'Отдел ОГКУ "ТО МФЦ" по городу Стрежевому',
        '17': 'Отдел ОГКУ "ТО МФЦ"  по Первомайскому району',
        '18': 'ТОСП в с. Тунгусово Молчановского району',
        '20': 'ТОСП в с.Нарга Молчановского района',
        '21': 'ТОСП в с.Могочино Молчановского района',
        '22': 'ТОСП в с.Чажемто Колпашевского района',
        '23': 'ТОСП в с.Новоселово Колпашевского района',
        '24': 'ТОСП в п.Большая Саровка Колпашевского района',
        '25': 'ТОСП в с.Володино Кривошеинского района',
        '26': 'ТОСП в с.Красный Яр Кривошеинского района',
        '27': 'ТОСП в с.Анастасьевка Шегарского района',
        '28': 'ТОСП в с.Баткат Шегарского района',
        '29': 'ТОСП в п.Победа Шегарского района',
        '30': 'ТОСП в с.Трубачево Шегарского района',
        '31': 'ТОСП в с.Монастырка Шегарского района',
        '32': 'ТОСП с.Богашево Томского района',
        '33': 'ТОСП в д.Воронино Томского района',
        '34': 'ТОСП в с.Зоркальцево Томского района',
        '35': 'ТОСП в с.Итатка Томского района',
        '36': 'ТОСП в д.Кисловка Томского района',
        '37': 'ТОСП в п.Зональная станция Томского района',
        '38': 'ТОСП в п.Рассвет Томского района',
        '39': 'ТОСП в с.Корнилово Томского района',
        '39': 'ТОСП в с.Корнилово Томского района',
        '41': 'ТОСП в с.Малиновка Томского района',
        '42': 'ТОСП в с.Межениновка Томского района',
        '43': 'ТОСП в п.Мирный Томского района',
        '44': 'ТОСП в с.Моряковский Томского района',
        '45': 'ТОСП в с.Новорождественское Томском районе',
        '46': 'ТОСП в с.Октябрьское Томского района',
        '47': 'ТОСП в с.Рыбалово Томского района',
        '48': 'ТОСП в с.Вершинино Томского района',
        '49': 'ТОСП в с.Турунтаево Томского района',
        '50': 'ТОСП в с.Вороново Кожевниковского района',
        '51': 'ТОСП с.Малиновка Кожевниковского района',
        '52': 'ТОСП в с.Новопокровка Кожевниковского района',
        '53': 'ТОСП в с.Песочнодубровка Кожевниковского района',
        '54': 'ТОСП в с.Старая Ювала Кожевниковском района',
        '55': 'ТОСП в с.Уртам Кожевниковского района',
        '56': 'ТОСП в с.Чилино Кожевниковского района',
        '58': 'Офис МФЦ для бизнеса в "Доме предпринимателя"',
        '59': 'ЦОУ для бизнеса в АО «Альфа Банк»',
        '60': 'ЦОУ для бизнеса в ПАО Банк «ФК Открытие»',
        '61': 'ЦОУ для бизнеса в ПАО «Промсвязьбанк»',
        '63': 'ТОСП ОЭЗ ТВТ',
        '64': 'ЦОУ для бизнеса в ПАО «Банк Уралсиб»',
        '65': 'ЦОУ для бизнеса в ПАО «Томскпромстройбанк»',
        '66': 'ЦОУ для бизнеса в ПАО Банк «Левобережный»',
        '69': 'Отдел ОГКУ "ТО МФЦ" по работе с субъектами МСП и ТОСП',
        '70': 'Отдел ОГКУ "ТО МФЦ" по Тегульдетскому району',
        '71': 'Отдел ОГКУ "ТО МФЦ" по Зырянскому району',
        '72': 'ТОСП в п. Орехово Первомайского района',
        '73': 'ТОСП в д. Березовка Первомайского района',
        '74': 'ТОСП в п. Улу-Юл Первомайского района',
        '75': 'ТОСП в с. Комсомольск Первомайского района',
        '76': 'ТОСП в с. Сергеево Первомайского района',
        '77': 'ЦОУ для бизнеса в АО «Газпромбанк»',
        '78': 'п. Самусь',
        '79': 'Отдел ОГКУ "ТО МФЦ"  по Парабельскому району'
    }

    class SuperStates(BaseStateGroup):
        FILIALS = 0
        DEPARTMENT = 1
        SERVICE = 2
        FIELDS = 3
        DATE = 4
        TIME = 5
        PHONE = 6
        MENU = 7
        STATUS = 8
        INF_COUPONS = 9
        DEL_COUPONS = 10
        INF_MFC = 11
        PHONE_INPUT = 12
        PHONE_INPUT_NEW = 13
        CONSULTATION = 14
        APPLICATION = 15
        EVENTS = 16
        ANNIVERSARY = 17
        GRADE = 18
        AGREEMENT_INPUT = 19

    locations_1 = ('Томск', 'Северск')

    locations_2 = ('Томск', 'Северск', 'Воронино', 'Кисловка',
                'Зональная станция', 'Мирный', 'Рассвет',
                'Богашово', 'Вершинино', 'Зоркальцево',
                'Итатка', 'Калтай', 'Корнилово', 'Малиновка',
                'Межениновка', 'Моряковский затон', 'Новорождественское',
                'Октябрьское', 'Рыболово', 'Турунтаево')

    async def reset_ctx(user_id):
        await debug_print('ВХОД В ФУНКЦИЮ reset_ctx', user_id)
        # Создаем список ключей для удаления
        keys_to_remove = [key for key in ctx.__dict__['storage'] if str(user_id) in key and \
        'talon_select_vkontakte_reg' not in key and \
        'department_select_vkontakte_reg' not in key and 'phone' not in key]

        # Удаляем ключи из storage
        for key in keys_to_remove:
            ctx.__dict__['storage'].pop(key, None)
            # pass

        # # Проверка текущего состояния storage
        # print('Текущее состояние storage:', ctx.__dict__['storage'])
        await debug_print('ВЫХОД ИЗ ФУНКЦИИ reset_ctx', user_id)
        return

    async def notification_delete_coupon(user_id, message):
        await debug_print('ВХОД В ФУНКЦИЮ notification_delete_coupon', user_id)
        result = await base(user_id = user_id).select_vkontakte_reg()

        if not result == [] and result != ():

            date = result[0][3]
            time_ = result[0][2]
            talon = result[0][1]
            department = result[0][4]
            service = result[0][5]
            uuid = result[0][6]
            tel = result[0][7]
            fio = result[0][8]
            ctx.set(f'{user_id}: talon_select_vkontakte_reg', talon)
            ctx.set(f'{user_id}: department_select_vkontakte_reg', department)

            keyboard = await buttons.delete_coupon(uuid, talon, department, date, tel, fio)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ notification_delete_coupon', user_id)
            return await message.answer(f"Вы хотите подтвердить или удалить талон {talon}, филиал: {department}, услуга: {service}, время: {date} в {time_}?", keyboard=keyboard)

    @bot.on.message(state=SuperStates.GRADE)
    async def grade(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ grade', user_id)
            contexts = {"application_service": None, "contact_application": None, "fio_application": None}
            users_info = await bot.api.users.get(message.from_id)

            back_list = ('back_1', 'back_13', 'back_5', 'back_6', 'back_6')

            async def number_review():
                await debug_print('ВХОД В ФУНКЦИЮ number_review', user_id)
                await message.answer("Спасибо за ваш отзыв и оценку")

                number_statement = ctx.get(f'{user_id}: number_statement')
                number_date = ctx.get(f'{user_id}: number_date')
                number_department = ctx.get(f'{user_id}: number_department')
                number_grade = ctx.get(f'{user_id}: number_grade')
                number_waiting_time = ctx.get(f'{user_id}: number_waiting_time')
                number_time = ctx.get(f'{user_id}: number_time')
                number_employee = ctx.get(f'{user_id}: number_employee')
                number_review = ctx.get(f'{user_id}: number_review')

                import datetime
                date_now = str(datetime.datetime.now().date())

                questions = (number_statement, number_date, number_department, number_grade, number_waiting_time, number_time, number_employee, number_review, date_now)

                await base().base_review(*questions)

                await notification_delete_coupon(user_id, message)

                for context in contexts:
                    ctx.set(f"{user_id}: {context}", "None")

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                await debug_print('ВЫХОД ИЗ ФУНКЦИИ number_review', user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            try:
                payload_data = eval(message.payload)['cmd']

                if payload_data == '1' and ctx.get(f'{user_id}: number_employee') != 'None':
                    ctx.set(f"{user_id}: number_review", '')
                    return await number_review()

                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    for context in contexts:
                        ctx.set(f"{user_id}: {context}", "None")

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif ctx.get(f'{user_id}: number_department') != 'None' and ctx.get(f'{user_id}: number_grade') == 'None':
                    ctx.set(f"{user_id}: number_grade", payload_data)
                    keyboard = await buttons.waiting_time()
                    return await message.answer("Время ожидания в очереди", keyboard=keyboard)

                elif ctx.get(f'{user_id}: number_grade') != 'None' and ctx.get(f'{user_id}: number_waiting_time') == 'None':
                    ctx.set(f"{user_id}: number_waiting_time", payload_data)
                    keyboard = await buttons.reception_1()
                    return await message.answer("Время предоставления государственной услуги", keyboard=keyboard)

                elif ctx.get(f'{user_id}: number_waiting_time') != 'None' and ctx.get(f'{user_id}: number_time') == 'None':
                    ctx.set(f"{user_id}: number_time", payload_data)
                    keyboard = await buttons.reception_2()
                    return await message.answer("Вежливость и компетентность сотрудника МФЦ", keyboard=keyboard)

                elif ctx.get(f'{user_id}: number_time') != 'None':
                    ctx.set(f"{user_id}: number_employee", payload_data)
                    keyboard = await buttons.grade()
                    return await message.answer("Оставьте свой отзыв", keyboard=keyboard)

                elif payload_data in back_list:
                    # keyboard = await buttons.filials()
                    # return await message.answer("Выберите филиал", keyboard=keyboard)
                    keyboard = await buttons.reception()
                    return await message.answer("Оцените по пятибальной шкале, где 'Пять' наивысшая оценка\n\nЗарегистрироваться на приём было просто и удобно", keyboard=keyboard)

                elif payload_data == 'button_review':
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Укажите номер вашего заявления (Например: 12/2024/123456)", keyboard=keyboard)

            except:

                if ctx.get(f'{user_id}: number_employee') != 'None':
                    ctx.set(f"{user_id}: number_review", message.text)
                    return await number_review()

                pattern_number_statement = r'\d{2}/\d{4}/\d{1,10}'
                pattern_date = r'\d{4}-\d{2}-\d{2}'

                if ctx.get(f'{user_id}: number_statement') == 'None' and re.search(pattern_number_statement, message.text):
                    ctx.set(f"{user_id}: number_statement", re.search(pattern_number_statement, message.text).group())

                    ctx.set(f"{user_id}: number_department", bid_locations[re.search(pattern_number_statement, message.text).group()[0:2]])

                    keyboard = await buttons.menu_menu()
                    return await message.answer("Укажите дату посещения в формате год-месяц-дата (Например: 2024-07-25)", keyboard=keyboard)
                elif ctx.get(f'{user_id}: number_date') == 'None' and re.search(pattern_date, message.text):
                    ctx.set(f"{user_id}: number_date", re.search(pattern_date, message.text).group())
                    keyboard = await buttons.reception()
                    return await message.answer("Зарегистрироваться на приём было", keyboard=keyboard)

                else:
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Вы ввели некорректные данные. Попробуйте ввести данные ещё раз.", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ grade', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.APPLICATION)
    async def application(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ application', user_id)
            async def post_application():
                if ctx.get(f'{user_id}: category_application') == 'None':
                    ctx.set(f'{user_id}: category_application', '')

                SSR = (ctx.get(f'{user_id}: fio_application'),
                    ctx.get(f'{user_id}: contact_application'),
                    ctx.get(f'{user_id}: application_service'),
                    ctx.get(f'{user_id}: service_application'),
                    ctx.get(f'{user_id}: category_application'))

                await base.base_post_application(*SSR)

                for context in contexts:
                    ctx.set(f"{user_id}: {context}", "None")

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await message.answer("Заявка отправлена.")
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            contexts = {"application_service": None, "contact_application": None, "fio_application": None}
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']

                commands_1 = {
                    'soc_sphere': buttons.services_social,
                    'nedvij': buttons.services_property,
                    'plant_usl': buttons.services_paid,
                    'konsul': buttons.services_consultation,
                    'drug_usl': buttons.services_other
                }

                if payload_data in commands_1:
                    function_to_call = commands_1[payload_data]
                    keyboard = await function_to_call('12345')
                    return await message.answer("Выберите услугу", keyboard=keyboard)

                if payload_data in services_name:
                    ctx.set(f'{user_id}: service_application', services_name[payload_data])
                    await post_application()

                if payload_data == 'back_1':
                    keyboard = await buttons.services_section('12345')
                    return await message.answer("Выберите услугу", keyboard=keyboard)

                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    for context in contexts:
                        ctx.set(f"{user_id}: {context}", "None")

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
                elif payload_data == 'application_service_1' or payload_data == "application_service_2":
                    ctx.set(f'{user_id}: application_service', payload_data[-1])
                    if payload_data == 'application_service_1':
                        keyboard = await buttons.services_section('12345')
                        return await message.answer("Выберите услугу", keyboard=keyboard)
                    elif payload_data == 'application_service_2':
                        ctx.set(f'{user_id}: service_application', '')
                        await post_application()

            except:

                pattern_telephone = r'(8|\+7)[0-9]{10}'

                if not re.search(pattern_telephone, message.text) and ctx.get(f'{user_id}: contact_application') == 'None':
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Не удалось отправить заявку.\nВведён некорректный номер телефона. Попробуйте ещё раз.\n\nНапишите:\n- свой контактный номер телефона;\n- адрес по которому необходимо осуществить выезд специалиста;\n- адрес электронной почты.\n\nНапример: 89876543210, г. Томск, ул. Строительная, 35-89, tgi658@yandex.ru", keyboard=keyboard)

                elif ctx.get(f'{user_id}: contact_application') == 'None':

                    if ctx.get(f'{user_id}: application_location') == '1':
                        for location in locations_1:
                            if location.lower() in message.text.lower() and not 'область' in message.text.lower():
                                ctx.set(f'{user_id}: contact_application', message.text)
                                keyboard = await buttons.menu_menu()
                                return await message.answer("Напишите:\nФамилию Имя Отчество / Наименование заказчика", keyboard=keyboard)
                        else:
                            keyboard = await buttons.menu_menu()
                            return await message.answer("Не удалось отправить заявку.\nНапоминаю, что выезд осуществляется только в пределах города Томска и Северска.\n\nПожалуйста напишите адрес по которому необходимо осуществить выезд специалиста.\nНапример: г. Томск, ул. Строительная, 35-89", keyboard=keyboard)

                    elif ctx.get(f'{user_id}: application_location') == '2':
                        for location in locations_2:
                            if location.lower() in message.text.lower() and not 'область' in message.text.lower():
                                ctx.set(f'{user_id}: contact_application', message.text)
                                keyboard = await buttons.menu_menu()
                                return await message.answer("Напишите:\nФамилию Имя Отчество / Наименование заказчика", keyboard=keyboard)
                        else:
                            keyboard = await buttons.menu_menu()
                            return await message.answer("Не удалось отправить заявку.\nНапоминаю, что выезд осуществляется только в пределах города Томска, Северска и Томского района.\n\nПожалуйста напишите адрес по которому необходимо осуществить выезд специалиста.\nНапример: г. Томск, ул. Строительная, 35-89", keyboard=keyboard)

                elif ctx.get(f'{user_id}: fio_application') == 'None':
                    ctx.set(f'{user_id}: fio_application', message.text)
                    keyboard = await buttons.application_service()
                    return await message.answer("Выберите, для чего необходимо выездное обслуживание", keyboard=keyboard)

                else:
                    ctx.set(f'{user_id}: contact_application', 'None')
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Вы ввели некорректные данные. Попробуйте ввести данные ещё раз.\n\nНапишите:\n- свой контактный номер телефона;\n- адрес по которому необходимо осуществить выезд специалиста;\n- адрес электронной почты.\n\nНапример, 88003500850, ул. Фрунзе 103д, md.tomsk.ru", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ application', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.ANNIVERSARY)
    async def anniversary(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ anniversary', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                if payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            except:
                await base(user_id=user_id).base_anniversary(message.text)
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await message.answer("Ваше пожеление успешно отправлено. Хорошего дня!")
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ anniversary', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.STATUS)
    async def status(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ status', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            except:
                pattern_number = r'\d{7}'
                if re.match(pattern_number, message.text):
                    answer = await base.readiness_status(message.text)

                    if answer['code'] == 'error' or answer['code'] == 'not_found':
                        keyboard = await buttons.menu_menu()
                        return await message.answer("По данному номеру Заявление не найдено", keyboard=keyboard)
                    if answer['code'] == 'operator':
                        keyboard = await buttons.menu_menu()
                        return await message.answer("К сожалению, но не удалось получить информацию о статусе ваших документов. Возможно, вы ввели неправильный код заявления или эта заявка уже обработана и закрыта. Если вам нужна дополнительная информация, пожалуйста, свяжитесь с оператором по номеру 8 800 350 08 50 или 8 (3822) 602-999", keyboard=keyboard)
                    keyboard = await buttons.menu_menu()
                    return await message.answer(f"Ваше заявление найдено, документы по номеру заявления {answer['caseNumberSpell']}, состоят в статусе - {answer['status_rus']}", keyboard=keyboard)
                else:
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Вы ввели некорректные данные. Попробуйте ввести данные ещё раз.", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ status', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.PHONE_INPUT)
    async def phone_input(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ phone_input', user_id)
            pattern_telephone = r'^(8|\+7)[0-9]{10}$'

            if re.match(pattern_telephone, message.text):

                ctx.set(f'{user_id}: identification', 'yes')

                ctx.set(f'{user_id}: phone', message.text)
                phone = ctx.get(f'{user_id}: phone')

                res = await base(user_id = user_id, tel = phone).phone_input()
                await base(user_id = user_id, tel = phone).agreement_input()

                if not res:
                    return await message.answer("Введённый вами номер уже кем-то используется. Возможно, вы ошиблись при вводе. Попробуйте ещё раз.")

                users_info = await bot.api.users.get(message.from_id)

                photo = "photo-224967611_457239778"

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню', attachment=photo)

            else:
                return await message.answer("Пожалуйста, убедитесь, что введённый вами номер телефона начинается с +7 или 8 и состоит из 11 цифр, без каких-либо знаков препинания. Возможно, вы ошиблись при вводе. Попробуйте ещё раз.")
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ phone_input', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.AGREEMENT_INPUT)
    async def agreement_input(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ agreement_input', user_id)
            users_info = await bot.api.users.get(message.from_id)

            async def agreement_scenario_inside_filials():
                await debug_print('ВХОД В ФУНКЦИЮ agreement_scenario_inside_filials', user_id)
                # answer = await base(user_id = user_id).phone_select()

                # agreement_answer = await base(user_id = user_id).agreement_select()

                ctx.set(f'{user_id}: agreement', '')

                # if not agreement_answer:
                #     async def read_file():
                #         async with aiofiles.open('files\\agreement.txt', mode='r', encoding='utf-8') as file:
                #             contents = await file.read()
                #             return contents

                #     if answer[0]:
                #         ctx.set(f'{user_id}: phone', answer[1][0][0])
                #     await bot.state_dispenser.set(message.peer_id, SuperStates.AGREEMENT_INPUT)
                #     keyboard = await buttons.agreement_yes_no()
                #     return await message.answer(f"{await read_file()}", keyboard=keyboard)

                await base(user_id=user_id).base_count_record()
                keyboard = await buttons.filials()
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await message.answer("Обращаем Ваше внимание, что прием осуществляется только при соответствии информации, указанной в талоне, с данными заявителя.")
                await message.answer("Записаться на приём вы так же можете:\n- в личном кабинете на официальном сайте МФЦ https://md.tomsk.ru;\n- через чат-бот ВКонтакте https://vk.com/im?sel=-224967611;\n- через сектор информирования в отделах МФЦ;\n- через контакт-центр МФЦ по номерам  8-800-350-08-50 (звонок бесплатный), 602-999.")
                await debug_print('ВЫХОД ИЗ ФУНКЦИИ agreement_scenario_inside_filials', user_id)
                return await message.answer("Выберите филиал", keyboard=keyboard)

            async def agreement_scenario_inside_application():
                await debug_print('ВХОД В ФУНКЦИЮ agreement_scenario_inside_application', user_id)
                # answer = await base(user_id = user_id).phone_select()

                # agreement_answer = await base(user_id = user_id).agreement_select()

                ctx.set(f'{user_id}: agreement', '')

                # if not agreement_answer:
                #     async def read_file():
                #         async with aiofiles.open('files\\agreement.txt', mode='r', encoding='utf-8') as file:
                #             contents = await file.read()
                #             return contents

                #     if answer[0]:
                #         ctx.set(f'{user_id}: phone', answer[1][0][0])
                #     await bot.state_dispenser.set(message.peer_id, SuperStates.AGREEMENT_INPUT)
                #     keyboard = await buttons.agreement_yes_no()
                #     return await message.answer(f"{await read_file()}", keyboard=keyboard)

                await base(user_id=user_id).base_count_application()
                keyboard = await buttons.application()
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await debug_print('ВЫХОД ИЗ ФУНКЦИИ agreement_scenario_inside_application', user_id)
                return await message.answer("Услуга по выезду сотрудника МФЦ к заявителю для приёма заявлений и документов, а так же доставки результатов предоставления услуг осуществляется:\n- платно (для всех)\n- бесплатно (для отдельных категорий граждан).", keyboard=keyboard)

            async def agreement_scenario_outside(agreement_input):
                await debug_print('ВХОД В ФУНКЦИЮ agreement_scenario_outside', user_id)
                phone = ctx.get(f'{user_id}: phone')
                await base(user_id = user_id, tel = phone).agreement_input(agreement_input)

                if agreement_input == 0:
                    await message.answer("Обработка персональных данных необходима для продолжения работы с сервисом.\n\nМы понимаем, что ваша конфиденциальность важна для вас. Однако, чтобы вы могли пользоваться всеми преимуществами нашего сервиса, нам необходимо получить ваше согласие на обработку персональных данных.")
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                answer = await base(user_id = user_id).phone_select()
                await debug_print('ВЫХОД ИЗ ФУНКЦИИ agreement_scenario_outside', user_id)
                if answer[0]:

                    agreement = ctx.get(f'{user_id}: agreement')

                    if agreement == 'filials':
                        return await agreement_scenario_inside_filials()

                    elif agreement == 'application':
                        return await agreement_scenario_inside_application()

                    ctx.set(f'{user_id}: phone', answer[1][0][0])

                    photo = "photo-224967611_457239778"

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню', attachment=photo)
                else:
                    await bot.state_dispenser.set(message.peer_id, SuperStates.PHONE_INPUT)
                    return await message.answer("Для полноценного пользования чат-ботом необходимо пройти регистрацию. Пожалуйста, укажите ВАШ постоянный номер телефона, который будет связан с вашим аккаунтом.(например, 88003500850)")

            try:
                payload_data = eval(message.payload)['cmd']

                if payload_data == 'yes':
                    await agreement_scenario_outside(1)
                elif payload_data == 'no':
                    await agreement_scenario_outside(0)

            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные. Попробуйте ввести данные ещё раз.", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ agreement_input', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.PHONE_INPUT_NEW)
    async def phone_input_new(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ phone_input_new', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    SSR = (ctx.get(f'{user_id}: department'),
                        ctx.get(f'{user_id}: service'),
                        ctx.get(f'{user_id}: fields'))

                    await bot.state_dispenser.set(message.peer_id, SuperStates.TIME)
                    keyboard, times = await buttons.times_buttons(ctx.get(f'{user_id}: date'), ctx.get(f'{user_id}: time'), *SSR)
                    ctx.set(f'{user_id}: times', times)
                    await message.answer("Выберите свободное время", keyboard=keyboard)

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            except:
                pattern_telephone = r'^(8|\+7)[0-9]{10}$'
                if re.match(pattern_telephone, message.text):

                    answer = await base(user_id = user_id, tel = message.text).phone_input_new()

                    if answer:
                        ctx.set(f'{user_id}: phone', message.text)

                        await bot.state_dispenser.set(message.peer_id, SuperStates.PHONE)
                        keyboard = await buttons.fio_yes()
                        return await message.answer("Обращаем Ваше внимание, что прием осуществляется только при соответствии информации, указанной в талоне, с данными заявителя.\n\nВведите вашу ФИО или можете использовать Фамилию Имя профиля", keyboard=keyboard)
                    else:
                        await bot.state_dispenser.set(message.peer_id, SuperStates.TIME)
                        keyboard = await buttons.yes_no()
                        return await message.answer(f"Вы не можете использовать новый номер телефона больше одного раза в день.\n\nОбращаем Ваше внимание, что прием осуществляется только при соответствии информации, указанной в талоне, с данными заявителя.\n\nДля записи на приём использовать номер телефона {ctx.get(f'{user_id}: phone')}?", keyboard=keyboard)
                else:
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Вы ввели некорректные данные. Попробуйте ввести данные ещё раз.", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ phone_input_new', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.INF_COUPONS)
    async def information_coupons(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ information_coupons', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            except:
                pattern_telephone = r'^(8|\+7)[0-9]{10}$'
                if re.match(pattern_telephone, message.text):
                    answer = await base.information_about_coupons(message.text, ctx.get(f'{user_id}: fio_cache'))

                    if answer['code'] == 'no':
                        keyboard = await buttons.menu_menu()
                        return await message.answer("По данному номеру Талоны не найдены. Попробуйте ещё раз.", keyboard=keyboard)
                    if answer['code'] == 'error':
                        keyboard = await buttons.menu_menu()
                        return await message.answer("Произошла ошибка поиска. Попробуйте ещё раз.", keyboard=keyboard)
                    keyboard = await buttons.menu_menu()
                    return await message.answer(f"{answer['service_name_time']}", keyboard=keyboard)
                else:
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ information_coupons', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.INF_MFC)
    async def information_mfc(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ information_mfc', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'tomsk':
                    keyboard = await buttons.tomsk()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'frunze':

                    photo = "photo-224967611_457239773"

                    async def read_file():
                        async with aiofiles.open('files_gr\\tomsk\\kirovskiy.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'derb':

                    photo = "photo-224967611_457239777"

                    async def read_file():
                        async with aiofiles.open('files_gr\\tomsk\\leninskiy.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'pushk':

                    photo = "photo-224967611_457239780"

                    async def read_file():
                        async with aiofiles.open('files_gr\\tomsk\\oktyabrskiy.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'tvers':

                    photo = "photo-224967611_457239785"

                    async def read_file():
                        async with aiofiles.open('files_gr\\tomsk\\sovetskiy.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'razv':

                    photo = "photo-224967611_457239788"

                    async def read_file():
                        async with aiofiles.open('files_gr\\tomsk\\akadem.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'mfc_business':
                    async def read_file():
                        async with aiofiles.open('files_gr\\tomsk\\COU_business.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.tomsk()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'tomsk_obl':
                    keyboard = await buttons.tomsk_obl()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'asino':

                    photo = "photo-224967611_457239770"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\asino.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'cedar':

                    photo = "photo-224967611_457239772"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\kedtovij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'strez':

                    photo = "photo-224967611_457239786"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\strezhevoj.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'zato':

                    photo = "photo-224967611_457239783"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\seversk.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'ziryansk':

                    photo = "photo-224967611_457239790"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\ziryanskij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'parabel':

                    photo = "photo-224967611_457239781"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\parabel.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'tomsk_obl_1':
                    keyboard = await buttons.tomsk_obl_1()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'balyar':

                    photo = "photo-224967611_457239789"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\verhneketskij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_1()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'alex':

                    photo = "photo-224967611_457239769"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\aleksandrovskij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_1()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'teguld':

                    photo = "photo-224967611_457239787"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\teguldet.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_1()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'chain':

                    photo = "photo-224967611_457239771"

                    async def read_file():
                        async with aiofiles.open('files_gr\\to\\chainskij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_1()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'tomsk_obl_2':
                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'pervom_rayon':

                    keyboard = await buttons.pervom_rayon()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'pervomaiskoye':

                    photo = "photo-224967611_457239782"

                    async def read_file():
                        async with aiofiles.open('files_gr\\perv\\pervomajskoje.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'serg':

                    async def read_file():
                        async with aiofiles.open('files_gr\\perv\\sergeevo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'oreh':

                    async def read_file():
                        async with aiofiles.open('files_gr\\perv\\orehovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'ulu':

                    async def read_file():
                        async with aiofiles.open('files_gr\\perv\\ulu-iul.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'komsom':

                    async def read_file():
                        async with aiofiles.open('files_gr\\perv\\komsomolsk.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'kojev_rayon':

                    keyboard = await buttons.kojev_rayon()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'voronovo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\voronovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'kojevn':

                    photo = "photo-224967611_457239774"

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\kozhevnikovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'malin':

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\malinovka_kozh.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'novopokrovka':

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\novopokrovka.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'pesochno':

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\pesok.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'old_yuvala':

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\yuvala.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'urtam':

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\urtam.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'chilino':

                    async def read_file():
                        async with aiofiles.open('files_gr\\koj\\chilino.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'krivosh_rayon':

                    keyboard = await buttons.krivosh_rayon()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'volodino':

                    async def read_file():
                        async with aiofiles.open('files_gr\\kriv\\volodino.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'red_yar':

                    async def read_file():
                        async with aiofiles.open('files_gr\\kriv\\red.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'krivosheino':

                    photo = "photo-224967611_457239776"

                    async def read_file():
                        async with aiofiles.open('files_gr\\kriv\\krivosheino.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)

                elif payload_data == 'kolp_rayon':

                    keyboard = await buttons.kolp_rayon()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'kolpashevo':

                    photo = "photo-224967611_457239775"

                    async def read_file():
                        async with aiofiles.open('files_gr\\kolp\\kolpashevo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'bolsh_sar':

                    async def read_file():
                        async with aiofiles.open('files_gr\\kolp\\sarovka.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'novoselovo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\kolp\\novoselovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'chazhemto':

                    async def read_file():
                        async with aiofiles.open('files_gr\\kolp\\chajemto.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'molch_rayon':

                    keyboard = await buttons.molch_rayon()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'mogochino':

                    async def read_file():
                        async with aiofiles.open('files_gr\\molch\\mogochino.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.molch_rayon()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'molchanovo':

                    photo = "photo-224967611_457239779"

                    async def read_file():
                        async with aiofiles.open('files_gr\\molch\\molchanovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.molch_rayon()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'narga':

                    async def read_file():
                        async with aiofiles.open('files_gr\\molch\\narga.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.molch_rayon()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'tungusovo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\molch\\tungusovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.molch_rayon()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'shegar_rayon':
                    keyboard = await buttons.shegar_rayon()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'anast':

                    async def read_file():
                        async with aiofiles.open('files_gr\\shegar\\anast.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'butkat':

                    async def read_file():
                        async with aiofiles.open('files_gr\\shegar\\batkat.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'meln':

                    photo = "photo-224967611_457239784"

                    async def read_file():
                        async with aiofiles.open('files_gr\\shegar\\shegarskij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard, attachment=photo)
                elif payload_data == 'monastery':

                    async def read_file():
                        async with aiofiles.open('files_gr\\shegar\\monas.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'victory':

                    async def read_file():
                        async with aiofiles.open('files_gr\\shegar\\pobeda.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'trubachevo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\shegar\\trub.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)

                elif payload_data == 'tomsk_rayon':

                    keyboard = await buttons.tomsk_rayon()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)

                elif payload_data == 'voronino':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\voronino.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'kislovka':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\kislovka.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'zonaln':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\zonalnij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'peaceful':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\mirnij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'dawn':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\rassvet.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'bogashevo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\bogashevo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'vershinino':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\vershinino.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'zork':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\zorkalcevo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'itatka':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\itatka.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'kaltay':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\kaltaj.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)

                elif payload_data == 'tomsk_rayon_1':

                    keyboard = await buttons.tomsk_rayon_1()
                    return await message.answer("Выберите район для записи", keyboard=keyboard)
                elif payload_data == 'kornilovo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\kornilovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'robin':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\malinovka_chul.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'mejen':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\mezheninovka.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'novoroj':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\novorozhdest.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'rybalovo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\ribalovo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'moryak_zaton':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\moryakovskij.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'turuntayevo_selo':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\turuntaevo.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'october':

                    async def read_file():
                        async with aiofiles.open('files_gr\\tr\\oktyabrskoe.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.tomsk_obl_2()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'back_1':
                    keyboard = await buttons.filials()
                    return await message.answer("Выберите филиал", keyboard=keyboard)
                elif payload_data == 'back_13':
                    keyboard = await buttons.tomsk_rayon()
                    return await message.answer("Выберите филиал", keyboard=keyboard)
                elif payload_data == 'back_5':
                    keyboard = await buttons.tomsk_obl()
                    return await message.answer("Выберите филиал", keyboard=keyboard)
                elif payload_data == 'back_6':
                    keyboard = await buttons.tomsk_obl_1()
                    return await message.answer("Выберите филиал", keyboard=keyboard)
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ information_mfc', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.EVENTS)
    async def events(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ events', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']

                if ctx.get(f'{user_id}: event_location') == 'tomsk':
                    if payload_data == 'yes':
                        await base(user_id=user_id).events('tomsk', ctx.get(f'{user_id}: event_date'), 'VK')
                        await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                        await message.answer("Уведомление о событии вам придёт за день до его начала.")
                        await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                        ctx.set(f'{user_id}: event_location', 'None')
                        # Очистка всех переменных
                        await reset_ctx(user_id)
                        return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
                    elif payload_data == 'no':
                        keyboard = await buttons.events('tomsk')
                        return await message.answer("Выберите событие", keyboard=keyboard)

                pattern_date = r'^\d{4}-\d{2}-\d{2}$'

                if re.match(pattern_date, payload_data):

                    ctx.set(f'{user_id}: event_date', payload_data)

                    """ДОДЕЛАТЬ - ВОЗМОЖНО УДАЛИТЬ ВООБЩЕ"""
                    # contents = await base().base_get_events_event(ctx.get(f'{user_id}: event_location'), ctx.get(f'{user_id}: event_date'))

                    filename = '{}{}'.format(ctx.get(f'{user_id}: event_location'), '\\' + ctx.get(f'{user_id}: event_date')) + '.txt'

                    with open(filename, mode='r', encoding='utf-8') as file:
                        contents = file.read()

                    keyboard = await buttons.yes_no()
                    return await message.answer(f"{contents}\n\nХотите получить уведомление за день до начала события?", keyboard=keyboard)

                if payload_data == 'menu':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'back_1':
                    keyboard = await buttons.filials('12345')
                    return await message.answer("Выберите филиал", keyboard=keyboard)
                elif payload_data == 'back':
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    ctx.set(f'{user_id}: anniversary', 'yes')

                    await base(user_id=user_id).base_count_anniversary()

                    async def read_file():
                        async with aiofiles.open('files_events\\anniversary.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    keyboard = await buttons.send()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)

                elif payload_data == 'back_1':
                    keyboard = await buttons.filials('12345')
                    return await message.answer("Выберите филиал", keyboard=keyboard)
                elif payload_data == 'back_13':
                    keyboard = await buttons.tomsk_rayon()
                    return await message.answer("Выберите филиал", keyboard=keyboard)
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ events', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.CONSULTATION)
    async def consultation_mfc(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ consultation_mfc', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'cons_mvd':

                    keyboard = await buttons.consultation_mvd()
                    return await message.answer("Выберите услугу", keyboard=keyboard)

                elif payload_data == 'cons_snils_inn_oms':

                    keyboard = await buttons.consultation_snils_inn_oms()
                    return await message.answer("Выберите услугу", keyboard=keyboard)

                elif payload_data == 'cons_zags':

                    keyboard = await buttons.consultation_zags()
                    return await message.answer("Выберите услугу", keyboard=keyboard)

                elif payload_data == 'cons_other':

                    keyboard = await buttons.consultation_other()
                    return await message.answer("Выберите услугу", keyboard=keyboard)

                elif payload_data == 'cons_vod':

                    photo = 'photo-224967611_457239840'

                    keyboard = await buttons.consultation()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo)
                elif payload_data == 'cons_port':
                    async def read_file():
                        async with aiofiles.open('files\\gosuslugi.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation_other()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_pasp':

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard)

                elif payload_data == 'cons_pasp_14':

                    photo_1 = 'photo-224967611_457239826'

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_1)

                elif payload_data == 'cons_pasp_20':

                    photo_2 = 'photo-224967611_457239827'

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_2)

                elif payload_data == 'cons_pasp_vnesh':

                    photo_3 = 'photo-224967611_457239828'

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_3)

                elif payload_data == 'cons_pasp_netoch':

                    photo_4 = 'photo-224967611_457239829'

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_4)

                elif payload_data == 'cons_pasp_povrej':

                    photo_5 = 'photo-224967611_457239830'

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_5)

                elif payload_data == 'cons_pasp_akt':

                    photo_6 = 'photo-224967611_457239831'

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_6)

                elif payload_data == 'cons_pasp_data':

                    photo_7 = 'photo-224967611_457239832'

                    keyboard = await buttons.cons_pasp()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_7)

                elif payload_data == 'cons_snils':
                    async def read_file():
                        async with aiofiles.open('files\\snils.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation_snils_inn_oms()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_zagr':

                    keyboard = await buttons.cons_zagr()
                    return await message.answer("ㅤ", keyboard=keyboard)
                elif payload_data == 'cons_zagr_5':

                    condition = True
                    keyboard = await buttons.cons_zagr_5_10(condition)
                    return await message.answer("ㅤ", keyboard=keyboard)
                elif payload_data == 'cons_zagr_10':

                    condition = False
                    keyboard = await buttons.cons_zagr_5_10(condition)
                    return await message.answer("ㅤ", keyboard=keyboard)

                elif payload_data == 'cons_zagr_14_18':

                    photo_1 = 'photo-224967611_457239820'

                    keyboard = await buttons.cons_zagr()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_1)

                elif payload_data == 'cons_zagr_14':

                    photo_2 = 'photo-224967611_457239821'

                    keyboard = await buttons.cons_zagr()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_2)
                elif payload_data == 'cons_zagr_18':

                    photo_3 = 'photo-224967611_457239822'

                    keyboard = await buttons.cons_zagr()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_3)
                elif payload_data == 'cons_zagr_14_18_10':

                    photo_4 = 'photo-224967611_457239843'

                    keyboard = await buttons.cons_zagr()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_4)
                elif payload_data == 'cons_zagr_14_10':

                    photo_5 = 'photo-224967611_457239842'

                    keyboard = await buttons.cons_zagr()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_5)
                elif payload_data == 'cons_zagr_18_10':

                    photo_6 = 'photo-224967611_457239844'

                    keyboard = await buttons.cons_zagr()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_6)
                elif payload_data == 'cons_inn':
                    async def read_file():
                        async with aiofiles.open('files\\app_inn.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation_snils_inn_oms()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_reg':
                    condition = True
                    keyboard = await buttons.consultation_reg_brak(condition)
                    return await message.answer("ㅤ", keyboard=keyboard)
                elif payload_data == 'cons_grajd_1':

                    photo_1 = 'photo-224967611_457239833'
                    photo_2 = 'photo-224967611_457239846'
                    photo_3 = 'photo-224967611_457239835'

                    condition = True
                    keyboard = await buttons.consultation_reg_brak(condition)
                    await message.answer("ㅤ", keyboard=keyboard, attachment=photo_1)
                    await message.answer("ㅤ", keyboard=keyboard, attachment=photo_2)
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_3)
                elif payload_data == 'cons_snyat_1':

                    photo_1 = 'photo-224967611_457239836'
                    photo_2 = 'photo-224967611_457239837'

                    condition = True
                    keyboard = await buttons.consultation_reg_brak(condition)
                    await message.answer("ㅤ", keyboard=keyboard, attachment=photo_1)
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_2)
                elif payload_data == 'cons_brak':
                    condition = False
                    keyboard = await buttons.consultation_reg_brak(condition)
                    return await message.answer("ㅤ", keyboard=keyboard)
                elif payload_data == 'cons_grajd_2':
                    async def read_file():
                        async with aiofiles.open('files\\zakl_brak.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    condition = False
                    keyboard = await buttons.consultation_reg_brak(condition)
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_snyat_2':
                    async def read_file():
                        async with aiofiles.open('files\\rastor.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    condition = False
                    keyboard = await buttons.consultation_reg_brak(condition)
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_drug':
                    keyboard = await buttons.consultation_other()
                    return await message.answer("ㅤ", keyboard=keyboard)
                elif payload_data == 'cons_rojd':
                    async def read_file():
                        async with aiofiles.open('files\\svid_rojd.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation_zags()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_polis':
                    async def read_file():
                        async with aiofiles.open('files\\oms.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation_snils_inn_oms()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_detsk':
                    async def read_file():
                        async with aiofiles.open('files\\det_sad.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_sert':

                    photo_1 = 'photo-224967611_457239818'
                    photo_2 = 'photo-224967611_457239819'

                    keyboard = await buttons.consultation()
                    await message.answer("ㅤ", keyboard=keyboard, attachment=photo_1)
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_2)
                elif payload_data == 'cons_predpr':

                    async def read_file():
                        async with aiofiles.open('files\\ip.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation_other()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_mnog':
                    async def read_file():
                        async with aiofiles.open('files\\mnogod.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_sprav':

                    photo_1 = 'photo-224967611_457239838'
                    photo_2 = 'photo-224967611_457239839'

                    keyboard = await buttons.consultation_mvd()
                    await message.answer("ㅤ", keyboard=keyboard, attachment=photo_1)
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo_2)
                elif payload_data == 'cons_vipiska':

                    photo = 'photo-224967611_457239841'

                    keyboard = await buttons.consultation_other()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo)
                elif payload_data == 'cons_edin':
                    async def read_file():
                        async with aiofiles.open('files\\edin_posob.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_lic':
                    async def read_file():
                        async with aiofiles.open('files\\taxi.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents
                    keyboard = await buttons.consultation_other()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)
                elif payload_data == 'cons_pens':

                    photo = 'photo-224967611_457239845'

                    keyboard = await buttons.consultation()
                    return await message.answer("ㅤ", keyboard=keyboard, attachment=photo)

                elif payload_data == 'back_5':
                    keyboard = await buttons.consultation()
                    return await message.answer("Выберите услугу", keyboard=keyboard)
                elif payload_data == 'back_6':
                    keyboard = await buttons.consultation_mvd()
                    return await message.answer("Выберите услугу", keyboard=keyboard)
                elif payload_data == 'back_7':
                    keyboard = await buttons.consultation_zags()
                    return await message.answer("Выберите услугу", keyboard=keyboard)
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ consultation_mfc', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.DEL_COUPONS)
    async def delete_coupons(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ delete_coupons', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'menu' or payload_data == 'back':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif ctx.get(f'{user_id}: yes_no_cache') == 'yes' and payload_data == 'yes':
                    ctx.set(f'{user_id}: yes_no_cache', 'None')

                    talon_id = list(ctx.get(f'{user_id}: talon_id_cache'))
                    esiaid = list(ctx.get(f'{user_id}: esiaid_cache'))
                    code = list(ctx.get(f'{user_id}: code_cache'))
                    department = list(ctx.get(f'{user_id}: department_cache'))
                    date = list(ctx.get(f'{user_id}: date_cache'))

                    index = ctx.get(f'{user_id}: code_counter')

                    code_cache = code[index]

                    res = await base(user_id = user_id).delete_coupons(talon_id[index], esiaid[index], code[index], department[index], date[index], ctx.get(f'{user_id}: tel_cache'), ctx.get(f'{user_id}: fio'))

                    ctx.set(f'{user_id}: code_counter', index + 1)

                    if index >= len(code):
                        await message.answer(f"По вашем данным талонов больше нет.")
                        await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                        await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                        # Очистка всех переменных
                        await reset_ctx(user_id)
                        return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                    ctx.set(f'{user_id}: tel_cache', 'None')
                    if res:

                        del talon_id[index]
                        del esiaid[index]
                        del code[index]
                        del department[index]
                        del date[index]

                        ctx.set(f'{user_id}: talon_id_cache', talon_id)
                        ctx.set(f'{user_id}: esiaid_cache', esiaid)
                        ctx.set(f'{user_id}: code_cache', code)

                        code = list(ctx.get(f'{user_id}: code_cache'))

                        index = ctx.get(f'{user_id}: code_counter')
                        if len(code) <= index:
                            ctx.set(f'{user_id}: code_counter', 0)
                            index = ctx.get(f'{user_id}: code_counter')

                        if code == []:
                            await message.answer(f"Ваш талон {code_cache} успешно удалён.\n\nПо вашем данным талонов больше нет.")
                            await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                            await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                            # Очистка всех переменных
                            await reset_ctx(user_id)
                            return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                        keyboard = await buttons.yes_no()
                        return await message.answer(f"Ваш талон {code_cache} успешно удалён.\n\nХотите ли удалить талон {code[index]}", keyboard=keyboard)
                    else:
                        keyboard = await buttons.menu_menu()
                        return await message.answer(f"Не удалось удалить талон", keyboard=keyboard)
                elif payload_data == 'no':
                    ctx.set(f'{user_id}: yes_no_cache', 'None')

                    code = list(ctx.get(f'{user_id}: code_cache'))

                    counter = ctx.get(f'{user_id}: code_counter')
                    ctx.set(f'{user_id}: code_counter', counter + 1)
                    counter = ctx.get(f'{user_id}: code_counter')

                    if counter >= len(code):
                        await message.answer(f"По вашем данным талонов больше нет.")
                        await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                        await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                        # Очистка всех переменных
                        await reset_ctx(user_id)
                        return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                    keyboard = await buttons.yes_no()
                    return await message.answer(f"Хотите ли удалить талон {code[counter]}", keyboard=keyboard)
                elif payload_data == 'yes':
                    ctx.set(f'{user_id}: yes_no_cache', 'yes')
                    code = list(ctx.get(f'{user_id}: code_cache'))

                    index = ctx.get(f'{user_id}: code_counter')

                    keyboard = await buttons.yes_no()
                    return await message.answer(f"Вы точно хотите удалить талон {code[index]}", keyboard=keyboard)
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ delete_coupons', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.FILIALS)
    async def filials(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ filials', user_id)

            users_info = await bot.api.users.get(message.from_id)

            """Обнуление переменных пользователя"""
            ctx.set(f'{user_id}: field_1', 'None')
            ctx.set(f'{user_id}: field_2', 'None')
            ctx.set(f'{user_id}: field_3', 'None')
            ctx.set(f'{user_id}: field_4', 'None')
            ctx.set(f'{user_id}: field_5', 'None')
            ctx.set(f'{user_id}: field_6', 'None')
            ctx.set(f'{user_id}: field_7', 'None')
            ctx.set(f'{user_id}: date', 'None')
            ctx.set(f'{user_id}: time', 'None')
            ctx.set(f'{user_id}: tel_cache', 'None')
            ctx.set(f'{user_id}: fio_cache', 'None')
            ctx.set(f'{user_id}: yes_no_cache', 'None')
            ctx.set(f'{user_id}: code_counter', 0)
            ctx.set(f'{user_id}: times', 'None')

            ctx.set(f'{user_id}: application_service', 'None')
            ctx.set(f'{user_id}: contact_application', 'None')
            ctx.set(f'{user_id}: fio_application', 'None')
            ctx.set(f'{user_id}: category_application', 'None')

            ctx.set(f'{user_id}: application_location', 'None')

            try:
                payload_data = eval(message.payload)['cmd']
            except:
                pattern_telephone = r'^(8|\+7)[0-9]{10}$'
                if re.match(pattern_telephone, message.text):
                    await base(user_id=user_id).base_count_cancel_record()
                    ani = await base(user_id = user_id).phone_select()
                    message.text = message.text.replace('+7', '8')

                    condition = False
                    if message.text == ani[1][0][0]:
                        ani = ani[1][0][0]
                        condition = True
                    elif message.text == ani[2][0][0]:
                        ani = ani[2][0][0]
                        condition = True
                    if condition:

                        ctx.set(f'{user_id}: tel_cache', ani)
                        ctx.set(f'{user_id}: fio_cache', '%')
                        answer = await base.information_about_coupons(ctx.get(f'{user_id}: tel_cache'), ctx.get(f'{user_id}: fio_cache'))
                        if answer['code'] == 'no':
                            keyboard = await buttons.menu_menu()
                            return await message.answer("По введённому вами номеру телефона талоны не найдены. Попробуйте ещё раз.", keyboard=keyboard)
                        if answer['code'] == 'error':
                            keyboard = await buttons.menu_menu()
                            return await message.answer("Произошла ошибка поиска. Попробуйте ещё раз.", keyboard=keyboard)

                        await bot.state_dispenser.set(message.peer_id, SuperStates.DEL_COUPONS)

                        ctx.set(f'{user_id}: talon_id_cache', answer['talon_id'])
                        ctx.set(f'{user_id}: esiaid_cache', answer['esiaid'])
                        ctx.set(f'{user_id}: code_cache', answer['code'])
                        ctx.set(f'{user_id}: department_cache', answer['department'])
                        ctx.set(f'{user_id}: date_cache', answer['dates'])

                        code = ctx.get(f'{user_id}: code_cache')

                        index = ctx.get(f'{user_id}: code_counter')
                        if index == -1:
                            ctx.set(f'{user_id}: code_counter', 0)
                            index = ctx.get(f'{user_id}: code_counter')

                        keyboard = await buttons.yes_no()

                        return await message.answer(f"{answer['service_name_time']}.\n\nХотите ли удалить талон {code[index]}", keyboard=keyboard)
                    else:
                        keyboard = await buttons.menu_menu()
                        return await message.answer("Этот номер телефона не использовался при регистрации талонов.\n\nПожалуйста, попробуйте ещё раз", keyboard=keyboard)
                else:
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Вы ввели некорректные данные.\n\nПожалуйста, попробуйте ещё раз", keyboard=keyboard)

            if payload_data == 'events' or payload_data == 'back' or payload_data == 'menu':
                ctx.set(f'{user_id}: anniversary', 'None')

            if payload_data == 'back' or payload_data == 'menu':

                await notification_delete_coupon(user_id, message)

                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
            elif payload_data == 'accept_entry':
                await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            commands_6 = {
                'tomsk_obl_1': buttons.tomsk_obl_1,
                'tomsk_obl_2': buttons.tomsk_obl_2,
                'tomsk_obl': buttons.tomsk_obl,
                'shegar_rayon': buttons.shegar_rayon,
                'pervom_rayon': buttons.pervom_rayon,
                'molch_rayon': buttons.molch_rayon,
                'kolp_rayon': buttons.kolp_rayon,
                'krivosh_rayon': buttons.krivosh_rayon,
                'kojev_rayon': buttons.kojev_rayon,
                'tomsk_rayon': buttons.tomsk_rayon,
                'tomsk_rayon_1': buttons.tomsk_rayon_1,
                'tomsk': buttons.tomsk,
                'mfc_business': buttons.mfc_business,
                'back_2': buttons.tomsk_obl_2,
                'back_5': buttons.tomsk_obl,
                'back_6': buttons.tomsk_obl_2,
                'back_13': buttons.tomsk_rayon,
            }

            # Пример вызова функции по ключу
            if payload_data in commands_6:
                function_to_call = commands_6[payload_data]
                await bot.state_dispenser.set(message.peer_id, SuperStates.DEPARTMENT)
                keyboard = await function_to_call()
                return await message.answer("Выберите район для записи", keyboard=keyboard)

            if payload_data in privileges:
                ctx.set(f'{user_id}: application_location', '2')
                ctx.set(f'{user_id}: category_application', privileges[payload_data])

            await debug_print('ВЫХОД ИЗ ФУНКЦИИ filials', user_id)
            if payload_data == 'filials' or payload_data == 'back_1' or payload_data == 'back':

                answer = await base(user_id = user_id).phone_select()

                agreement_answer = await base(user_id = user_id).agreement_select()

                ctx.set(f'{user_id}: agreement', 'filials')

                if not agreement_answer[0] or agreement_answer[1] == '0':
                    async def read_file():
                        async with aiofiles.open('files\\agreement.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    if answer[0]:
                        ctx.set(f'{user_id}: phone', answer[1][0][0])
                    await bot.state_dispenser.set(message.peer_id, SuperStates.AGREEMENT_INPUT)
                    keyboard = await buttons.agreement_yes_no()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)

                await base(user_id=user_id).base_count_record()
                keyboard = await buttons.filials()
                await message.answer("Обращаем Ваше внимание, что прием осуществляется только при соответствии информации, указанной в талоне, с данными заявителя.")
                await message.answer("Записаться на приём вы так же можете:\n- в личном кабинете на официальном сайте МФЦ https://md.tomsk.ru;\n- через чат-бот ВКонтакте https://vk.com/im?sel=-224967611;\n- через сектор информирования в отделах МФЦ;\n- через контакт-центр МФЦ по номерам  8-800-350-08-50 (звонок бесплатный), 602-999.")
                return await message.answer("Выберите филиал", keyboard=keyboard)

            elif ctx.get(f'{user_id}: anniversary') == 'yes' and payload_data == 'yes':
                ctx.set(f'{user_id}: anniversary', 'None')
                await bot.state_dispenser.set(message.peer_id, SuperStates.ANNIVERSARY)
                keyboard = await buttons.menu_menu()
                return await message.answer('Пожалуйста, напишите свои пожелания ниже и нажмите кнопку "Отправить". Не забудьте указать населенный пункт вашего проживания.👇', keyboard=keyboard)
            elif ctx.get(f'{user_id}: anniversary') == 'yes' and (payload_data == 'back' or payload_data == 'menu'):

                await notification_delete_coupon(user_id, message)

                ctx.set(f'{user_id}: anniversary', 'None')

                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            elif payload_data == 'anniversary':
                ctx.set(f'{user_id}: anniversary', 'yes')

                await base(user_id=user_id).base_count_anniversary()

                async def read_file():
                    async with aiofiles.open('files_events\\anniversary.txt', mode='r', encoding='utf-8') as file:
                        contents = await file.read()
                        return contents

                keyboard = await buttons.send()
                return await message.answer(f"{await read_file()}", keyboard=keyboard)

            elif payload_data == 'events' or payload_data == 'back_1' or payload_data == 'back':
                await base(user_id=user_id).base_count_events()
                await bot.state_dispenser.set(message.peer_id, SuperStates.EVENTS)

                ctx.set(f'{user_id}: event_location', 'tomsk')
                keyboard = await buttons.events('tomsk')
                keyboard_data = json.loads(keyboard)
                payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                payload = eval(str(payload_value))['cmd']
                if payload == 'back_1':
                    return await message.answer("На данный момент нет событий", keyboard=keyboard)
                else:
                    return await message.answer('🎉Программа фестиваля "Праздник топора"🎉\nФестиваль пройдёт с 17 по 24 августа и в этом году будет посвящён 80-летию Томской области.\nВход свободный!\n🪓Место: Парк "Околица" с. Зоркальцево Томского района', keyboard=keyboard)

            elif payload_data == 'application':

                answer = await base(user_id = user_id).phone_select()

                agreement_answer = await base(user_id = user_id).agreement_select()

                ctx.set(f'{user_id}: agreement', 'application')

                if not agreement_answer[0] or agreement_answer[1] == '0':
                    async def read_file():
                        async with aiofiles.open('files\\agreement.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    if answer[0]:
                        ctx.set(f'{user_id}: phone', answer[1][0][0])
                    await bot.state_dispenser.set(message.peer_id, SuperStates.AGREEMENT_INPUT)
                    keyboard = await buttons.agreement_yes_no()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)

                await base(user_id=user_id).base_count_application()
                keyboard = await buttons.application()
                return await message.answer("Услуга по выезду сотрудника МФЦ к заявителю для приёма заявлений и документов, а так же доставки результатов предоставления услуг осуществляется:\n- платно (для всех)\n- бесплатно (для отдельных категорий граждан).", keyboard=keyboard)

            elif payload_data == 'application_4' or ctx.get(f'{user_id}: category_application') != 'None':
                if ctx.get(f'{user_id}: application_location') == 'None':
                    ctx.set(f'{user_id}: application_location', '1')
                await bot.state_dispenser.set(message.peer_id, SuperStates.APPLICATION)
                keyboard = await buttons.menu_menu()
                return await message.answer("Напишите:\n- свой контактный номер телефона;\n- адрес по которому необходимо осуществить выезд специалиста (Обязательно укажите Томск или Северск или Томский район);\n- адрес электронной почты.\n\nНапример: 89876543210, г. Томск, ул. Строительная, 35-89, tgi658@yandex.ru", keyboard=keyboard)

            elif payload_data == 'application_1':

                async def read_file():
                    async with aiofiles.open('files_gr\\application.txt', mode='r', encoding='utf-8') as file:
                        contents = await file.read()
                        return contents

                keyboard = await buttons.application_send()
                return await message.answer(f"{await read_file()}", keyboard=keyboard)

            elif payload_data == 'application_2':

                async def read_file():
                    async with aiofiles.open('files_gr\\application_1.txt', mode='r', encoding='utf-8') as file:
                        contents = await file.read()
                        return contents

                keyboard = await buttons.application_approaching()
                return await message.answer(f"{await read_file()}", keyboard=keyboard)

            elif payload_data == 'application_3':

                keyboard = await buttons.application_1()
                return await message.answer("Выберите категорию, к которой относится заявитель", keyboard=keyboard)

            elif payload_data == 'grade':
                await base(user_id=user_id).base_count_grade()
                await bot.state_dispenser.set(message.peer_id, SuperStates.GRADE)

                ctx.set(f"{user_id}: number_statement", 'None')
                ctx.set(f"{user_id}: number_date", 'None')
                ctx.set(f"{user_id}: number_department", 'None')
                ctx.set(f"{user_id}: number_grade", 'None')
                ctx.set(f"{user_id}: number_waiting_time", 'None')
                ctx.set(f"{user_id}: number_time", 'None')
                ctx.set(f"{user_id}: number_employee", 'None')
                ctx.set(f"{user_id}: number_review", 'None')

                keyboard = await buttons.button_review()
                return await message.answer("Оценить качество предоставления услуг можно следующими способами:\n\n- на сайте МФЦ Томской области; (https://md.tomsk.ru/quiz/usluga)\n- по СМС, которая поступит после получения услуги;\n- по адресу электронной почты (если она указана на приеме);\n- на сайте Вашконтроль.Ру (https://vashkontrol.ru/) (вход через учетную запись Госуслуги.ру (https://www.gosuslugi.ru/);\n- в окне у специалиста МФЦ;", keyboard=keyboard)

            elif payload_data == 'status':
                await base(user_id=user_id).base_count_status()
                await bot.state_dispenser.set(message.peer_id, SuperStates.STATUS)
                keyboard = await buttons.menu_menu()
                return await message.answer("Для получения информации о готовности ваших документов, вам понадобится использовать семизначный код, указанный в верхней части заявления, которое вы получили на приеме в МФЦ.\n\nВведите код вашего заявления.(например, 1234567)", keyboard=keyboard)
            elif payload_data == 'information_coupons':
                await base(user_id=user_id).base_count_inf()
                await bot.state_dispenser.set(message.peer_id, SuperStates.INF_COUPONS)
                keyboard = await buttons.menu_menu()
                return await message.answer("Для получения информации о вашей записи, вам необходимо ввести номер телефона, на который зарегистрирован талон в МФЦ.\n\nВведите ваш номер телефона (например, 88003500850)", keyboard=keyboard)
            elif payload_data == 'information_mfc':
                await base(user_id=user_id).base_count_cons_mfc()
                await bot.state_dispenser.set(message.peer_id, SuperStates.INF_MFC)
                keyboard = await buttons.filials()
                return await message.answer("Выберите филиал", keyboard=keyboard)
            elif payload_data == 'consultation':
                await base(user_id=user_id).base_count_cons_mfc()
                await bot.state_dispenser.set(message.peer_id, SuperStates.CONSULTATION)
                keyboard = await buttons.consultation()
                return await message.answer("Выберите услугу", keyboard=keyboard)
            elif payload_data == 'yes':

                await base(user_id=user_id).base_count_cancel_record()

                ani = await base(user_id = user_id).phone_select()

                ctx.set(f'{user_id}: tel_cache', ani[1][0][0])
                ctx.set(f'{user_id}: fio_cache', '%')
                answer = await base.information_about_coupons(ctx.get(f'{user_id}: tel_cache'), ctx.get(f'{user_id}: fio_cache'))
                if answer['code'] == 'no':
                    keyboard = await buttons.menu_menu()
                    return await message.answer("По введённому вами номеру телефона талоны не найдены. Попробуйте ещё раз.", keyboard=keyboard)
                if answer['code'] == 'error':
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Произошла ошибка поиска. Попробуйте ещё раз.", keyboard=keyboard)

                await bot.state_dispenser.set(message.peer_id, SuperStates.DEL_COUPONS)

                ctx.set(f'{user_id}: talon_id_cache', answer['talon_id'])
                ctx.set(f'{user_id}: esiaid_cache', answer['esiaid'])
                ctx.set(f'{user_id}: code_cache', answer['code'])
                ctx.set(f'{user_id}: department_cache', answer['department'])
                ctx.set(f'{user_id}: date_cache', answer['dates'])

                code = ctx.get(f'{user_id}: code_cache')

                index = ctx.get(f'{user_id}: code_counter')
                if index == -1:
                    ctx.set(f'{user_id}: code_counter', 0)
                    index = ctx.get(f'{user_id}: code_counter')

                keyboard = await buttons.yes_no()
                return await message.answer(f"{answer['service_name_time']}.\n\nХотите ли удалить талон {code[index]}", keyboard=keyboard)

            elif payload_data == 'no':
                keyboard = await buttons.menu_menu()
                return await message.answer("Для удаления ваших талонов, вам понадобится использовать номер телефона, на который вы регистрировали талоны в МФЦ.\n\nВведите ваш номер телефона.(например, 88003500850)", keyboard=keyboard)
            elif payload_data == 'delete_coupons':
                keyboard = await buttons.yes_no()
                return await message.answer(f"Для удаления талонов использовать номер телефона {ctx.get(f'{user_id}: phone')}?", keyboard=keyboard)
            elif payload_data.startswith('delete_coupons_'):
                ctx.set(f'{user_id}: yes_no_cache', 'yes')

                ctx.set(f'{user_id}: talon_id_cache', [payload_data.split('_')[2]])
                ctx.set(f'{user_id}: esiaid_cache', [''])
                ctx.set(f'{user_id}: code_cache', [payload_data.split('_')[3]])
                ctx.set(f'{user_id}: department_cache', [payload_data.split('_')[4]])
                ctx.set(f'{user_id}: date_cache', [payload_data.split('_')[5]])
                ctx.set(f'{user_id}: code_counter', 0)
                ctx.set(f'{user_id}: tel_cache', payload_data.split('_')[6])
                ctx.set(f'{user_id}: fio', payload_data.split('_')[7])

                await bot.state_dispenser.set(message.peer_id, SuperStates.DEL_COUPONS)
                keyboard = await buttons.yes_no()
                return await message.answer(f"Вы точно хотите удалить талон {payload_data.split('_')[3]}?", keyboard=keyboard)
            else:
                await message.answer("Вы ввели некорректные данные.")
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.DEPARTMENT)
    async def department(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ department', user_id)

            users_info = await bot.api.users.get(message.from_id)
            try:
                payload_data = eval(message.payload)['cmd']
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)

            if payload_data == 'back_3':
                await bot.state_dispenser.set(message.peer_id, SuperStates.DEPARTMENT)
                keyboard = await buttons.tomsk()
                return await message.answer("Выберите филиал", keyboard=keyboard)
            elif payload_data == 'back' or payload_data == 'back_1':
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                keyboard = await buttons.filials()
                return await message.answer("Выберите филиал", keyboard=keyboard)
            elif payload_data == 'back_6':
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                keyboard = await buttons.tomsk_obl_1()
                return await message.answer("Выберите филиал", keyboard=keyboard)
            elif payload_data == 'menu':

                await notification_delete_coupon(user_id, message)

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            elif payload_data == 'accept_entry':
                await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            elif payload_data == 'mfc_business':
                await bot.state_dispenser.set(message.peer_id, SuperStates.DEPARTMENT)
                keyboard = await buttons.mfc_business()
                return await message.answer("Выберите банк", keyboard=keyboard)
            elif payload_data in list(services_id.keys()):
                ctx.set(f'{user_id}: service', services_id[payload_data])
                await bot.state_dispenser.set(message.peer_id, SuperStates.FIELDS)
                keyboard = await buttons.params_1()
                await message.answer("Назовите количество дел", keyboard=keyboard)

            commands_1 = {
                'soc_sphere': buttons.services_social,
                'nedvij': buttons.services_property,
                'plant_usl': buttons.services_paid,
                'konsul': buttons.services_consultation,
                'drug_usl': buttons.services_other
            }

            commands_2 = {
                'tomsk_obl_1': buttons.tomsk_obl_1,
                'tomsk_obl_2': buttons.tomsk_obl_2,
                'tomsk_obl': buttons.tomsk_obl,
                'shegar_rayon': buttons.shegar_rayon,
                'pervom_rayon': buttons.pervom_rayon,
                'molch_rayon': buttons.molch_rayon,
                'kolp_rayon': buttons.kolp_rayon,
                'krivosh_rayon': buttons.krivosh_rayon,
                'kojev_rayon': buttons.kojev_rayon,
                'tomsk_rayon': buttons.tomsk_rayon,
                'tomsk_rayon_1': buttons.tomsk_rayon_1,
                'tomsk': buttons.tomsk,
                'mfc_business': buttons.mfc_business,
                'back_2': buttons.tomsk_obl_2,
                'back_5': buttons.tomsk_obl,
                'back_6': buttons.tomsk_obl_2,
                'back_13': buttons.tomsk_rayon
            }

            # Пример вызова функции по ключу
            if payload_data in commands_1:
                function_to_call = commands_1[payload_data]
                await bot.state_dispenser.set(message.peer_id, SuperStates.SERVICE)
                keyboard = await function_to_call(ctx.get(f'{user_id}: department'))
                return await message.answer("Выберите услугу", keyboard=keyboard)
            elif payload_data in commands_2:
                function_to_call = commands_2[payload_data]
                keyboard = await function_to_call()
                return await message.answer("Выберите район для записи", keyboard=keyboard)

            if payload_data in filials_id.keys():
                ctx.set(f'{user_id}: department', filials_id[payload_data])
                keyboard = await buttons.services_section(ctx.get(f'{user_id}: department'))
                return await message.answer("Выберите услугу", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ department', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.SERVICE)
    async def service(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ service', user_id)
            users_info = await bot.api.users.get(message.from_id)
            try:
                payload_data = eval(message.payload)['cmd']
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)

            if payload_data == 'back' or payload_data == 'filials':

                answer = await base(user_id = user_id).phone_select()

                agreement_answer = await base(user_id = user_id).agreement_select()

                ctx.set(f'{user_id}: agreement', 'filials')

                if not agreement_answer[0] or agreement_answer[1] == '0':
                    async def read_file():
                        async with aiofiles.open('files\\agreement.txt', mode='r', encoding='utf-8') as file:
                            contents = await file.read()
                            return contents

                    if answer[0]:
                        ctx.set(f'{user_id}: phone', answer[1][0][0])
                    await bot.state_dispenser.set(message.peer_id, SuperStates.AGREEMENT_INPUT)
                    keyboard = await buttons.agreement_yes_no()
                    return await message.answer(f"{await read_file()}", keyboard=keyboard)

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                keyboard = await buttons.filials()
                await message.answer("Обращаем Ваше внимание, что прием осуществляется только при соответствии информации, указанной в талоне, с данными заявителя.")
                await message.answer("Записаться на приём вы так же можете:\n- в личном кабинете на официальном сайте МФЦ https://md.tomsk.ru;\n- через чат-бот ВКонтакте https://vk.com/im?sel=-224967611;\n- через сектор информирования в отделах МФЦ;\n- через контакт-центр МФЦ по номерам  8-800-350-08-50 (звонок бесплатный), 602-999.")
                return await message.answer("Выберите филиал", keyboard=keyboard)
            elif payload_data == 'back_1':
                keyboard = await buttons.services_section(ctx.get(f'{user_id}: department'))
                return await message.answer("Выберите услугу", keyboard=keyboard)
            elif payload_data == 'menu':

                await notification_delete_coupon(user_id, message)

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            elif payload_data == 'accept_entry':
                await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            commands_3 = {
                'soc_sphere': buttons.services_social,
                'nedvij': buttons.services_property,
                'plant_usl': buttons.services_paid,
                'konsul': buttons.services_consultation,
                'drug_usl': buttons.services_other
            }

            # Пример вызова функции по ключу
            if payload_data in commands_3:
                function_to_call = commands_3[payload_data]
                await bot.state_dispenser.set(message.peer_id, SuperStates.SERVICE)
                keyboard = await function_to_call(ctx.get(f'{user_id}: department'))
                return await message.answer("Выберите услугу", keyboard=keyboard)

            ctx.set(f'{user_id}: service', services_id[payload_data])

            await bot.state_dispenser.set(message.peer_id, SuperStates.FIELDS)
            keyboard = await buttons.params_1()
            await message.answer("Назовите количество дел", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ service', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.FIELDS)
    async def fields(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ fields', user_id)
            users_info = await bot.api.users.get(message.from_id)
            service_id = ctx.get(f'{user_id}: service')

            field_1 = ctx.get(f'{user_id}: field_1')
            field_2 = ctx.get(f'{user_id}: field_2')
            field_3 = ctx.get(f'{user_id}: field_3')
            field_4 = ctx.get(f'{user_id}: field_4')
            field_5 = ctx.get(f'{user_id}: field_5')

            user_id = message.from_id

            contexts = {"field_1", "field_2", "field_3",
                    "field_4", "field_5", "field_6",
                    "field_7", "date", "time",
                    "tel_cache", "fio_cache", "yes_no_cache",
                    "times"}

            async def write_to_file(text):
                await debug_print('ВХОД В ФУНКЦИЮ write_to_file', user_id)
                import os
                # Указываем директорию для сохранения файла
                folder_path = 'C:\\Users\\neverov\\Desktop\\file'  # Укажите путь к папке
                os.makedirs(folder_path, exist_ok=True)  # Создает папку, если она не существует

                file_path = os.path.join(folder_path, f'info_{user_id}.txt')  # Путь к файлу

                # Асинхронно записываем текст в файл
                async with aiofiles.open(file_path, 'a', encoding='utf-8') as file:
                    await file.write(text)
                await debug_print('ВЫХОД ИЗ ФУНКЦИИ write_to_file', user_id)
                return

            date = ctx.get(f'{user_id}: date')
            time = ctx.get(f'{user_id}: time')
            department = ctx.get(f'{user_id}: department')
            service = ctx.get(f'{user_id}: service')

            SSR = (date, time, department, service)

            async def post_file(file_name):
                await debug_print('ВХОД В ФУНКЦИЮ post_file', user_id)
                import os

                file_name_format = str(file_name.title).split('.')[1]
                file_name = f'passport_{user_id}.{file_name_format}'

                # Путь к директории, куда сохранять файлы
                DOWNLOAD_PATH = "C:\\Users\\neverov\\Desktop\\file"

                # Создадим директорию, если она не существует
                if not os.path.exists(DOWNLOAD_PATH):
                    os.makedirs(DOWNLOAD_PATH)
                await debug_print('ВЫХОД ИЗ ФУНКЦИИ ФУНКЦИЮ post_file', user_id)
                # Проверяем, есть ли вложения и является ли первое вложение документом
                if message.attachments and len(message.attachments) > 0 and message.attachments[0].doc:
                    print('POPAL_NEVEROV_ВНУТРИ')
                    document = message.attachments[0].doc

                    # Получаем расширение файла
                    file_extension = document.ext

                    # Проверка, что файл не имеет расширение .rar
                    if file_extension.lower() == 'rar':
                        return False, 'Файлы с расширением .rar не поддерживаются'

                    # Получаем URL для загрузки документа
                    file_url = document.url

                    # import random

                    # random_int = random.randint(1, 10000)

                    # Имя файла (например, example.pdf)
                    # file_name = document.title
                    # file_name_format = str(document.title).split('.')[1]
                    # file_name = f'{str(random_int)}_{str(user_id)}.{file_name_format}'

                    # Полный путь, куда сохранять файл
                    file_path = os.path.join(DOWNLOAD_PATH, file_name)

                    # count = 0
                    # while os.path.isfile(file_path) and count != 5:
                    #     random_int = random.randint(1, 10000)
                    #     file_name = f'{str(random_int)}_{str(user_id)}.{file_name_format}'
                    #     count += 1

                    # Загружаем файл с сервера ВКонтакте и сохраняем его
                    async with aiohttp.ClientSession() as session:
                        async with session.get(file_url) as resp:
                            if resp.status == 200:
                                with open(file_path, 'wb') as f:
                                    f.write(await resp.read())

                    return True, f"Файл '{file_name}' сохранён."
                else:
                    # Если вложений нет или они не являются документами
                    return False, 'В вашем сообщении нет документа. Введите причину отсутствия документа.'

            try:
                payload_data = eval(message.payload)['cmd']

                if payload_data == 'no_no':
                    await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                    print('--------------------------------------------')
                    await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                    print(*SSR)
                    print(ctx.get(f'{user_id}: fields'))
                    print('--------------------------------------------')
                    keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                    keyboard_data = json.loads(keyboard)
                    payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                    payload = eval(str(payload_value))['cmd']
                    if payload == 'menu':
                        return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                    else:
                        return await message.answer("Выберите свободную дату", keyboard=keyboard)

                if payload_data == 'back':

                    """Обнуление переменных пользователя"""
                    ctx.set(f'{user_id}: code_counter', 0)

                    for context in contexts:
                            ctx.set(f"{user_id}: {context}", "None")

                    await bot.state_dispenser.set(message.peer_id, SuperStates.SERVICE)
                    keyboard = await buttons.services_section(ctx.get(f'{user_id}: department'))
                    return await message.answer("Выберите услугу", keyboard=keyboard)
                elif payload_data == 'menu':

                    await notification_delete_coupon(user_id, message)

                    """Обнуление переменных пользователя"""
                    ctx.set(f'{user_id}: code_counter', 0)

                    for context in contexts:
                            ctx.set(f"{user_id}: {context}", "None")

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            except:

                """ОТПРАВЛЯТЬ ФАЙЛЫ"""

                if ctx.get(f'{user_id}: button_cache_file') == 'yes':
                    try:
                        post = await post_file(message.attachments[0].doc)

                        if post[0]:
                            # Отправляем сообщение о том, что файл сохранён
                            await message.answer(post[1])
                            ctx.set(f'{user_id}: button_cache_file_1', 'yes')
                            ctx.set(f'{user_id}: button_cache_file', '')
                            keyboard = await buttons.menu_menu_file()
                            return await message.answer("Загрузите все страницы выписки из ЕГРН.", keyboard=keyboard)
                        else:
                            ctx.set(f'{user_id}: button_cache_file_1', '')
                            ctx.set(f'{user_id}: button_cache_file', '')
                            await write_to_file(f'Нет Паспорта: {message.text}, ')
                            keyboard = await buttons.menu_menu_file()
                            return await message.answer(post[1], keyboard=keyboard)
                    except:
                        ctx.set(f'{user_id}: button_cache_file_1', '')
                        ctx.set(f'{user_id}: button_cache_file', '')
                        await write_to_file(f'Нет Паспорта: {message.text}, ')
                        keyboard = await buttons.menu_menu_file()
                        return await message.answer('В вашем сообщении нет документа. Введите причину отсутствия документа.', keyboard=keyboard)

                elif ctx.get(f'{user_id}: button_cache_file_1') == 'yes':
                    print('ВТОРОЙ ДОКУМЕНТ')
                    try:

                        post = await post_file(message.attachments[0].doc)

                        if post[0]:

                            # Отправляем сообщение о том, что файл сохранён
                            await message.answer(post[1])
                            await message.answer("Спапсибо за обращение.")
                            ctx.set(f'{user_id}: button_cache_file_1', '')

                            await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                            print('--------------------------------------------')
                            await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                            print(*SSR)
                            print(ctx.get(f'{user_id}: fields'))
                            print('--------------------------------------------')
                            keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                            keyboard_data = json.loads(keyboard)
                            payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                            payload = eval(str(payload_value))['cmd']
                            if payload == 'menu':
                                return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                            else:
                                return await message.answer("Выберите свободную дату", keyboard=keyboard)

                        else:
                            ctx.set(f'{user_id}: button_cache_file_1', '')
                            await write_to_file(f'Нет ЕГРН: {message.text}, ')
                            keyboard = await buttons.menu_menu_file()
                            return await message.answer(post[1], keyboard=keyboard)
                    except:
                        ctx.set(f'{user_id}: button_cache_file_1', '')
                        await write_to_file(f'Нет ЕГРН: {message.text}, ')
                        keyboard = await buttons.menu_menu_file()
                        return await message.answer('В вашем сообщении нет документа. Введите причину отсутствия документа.', keyboard=keyboard)

                print('---------------------------------------')
                print(ctx.get(f'{user_id}: button_cache_file_start'))
                print(ctx.get(f'{user_id}: service'))
                print(ctx.get(f'{user_id}: field_1'))
                print(ctx.get(f'{user_id}: field_2'))
                print(ctx.get(f'{user_id}: field_3'))
                print(ctx.get(f'{user_id}: field_4'))
                print(ctx.get(f'{user_id}: field_6'))

                """НАЧАЛО ЗАГРУЗКИ ФАЙЛОВ"""

                # if ctx.get(f'{user_id}: button_cache_file_start') != 'yes' and ctx.get(f'{user_id}: service') == '8f5e514e-dcce-41cf-8b56-38db6af10056' and ctx.get(f'{user_id}: field_1') != 'None' and ctx.get(f'{user_id}: field_2') != 'None' and ctx.get(f'{user_id}: field_3') != 'None' and ctx.get(f'{user_id}: field_4') != 'None' and ctx.get(f'{user_id}: field_6') != 'None':
                #     ctx.set(f'{user_id}: button_cache_file_start', 'yes')

                #     keyboard = await buttons.yes_no_doc()
                #     return await message.answer("Мы заботимся о вашем времени! Для вашего удобства предлагаем возможность отправки необходимых документов онлайн, что позволит сохранить время, затрачиваемое на приёме.", keyboard=keyboard)

                if service_id == '8f5e514e-dcce-41cf-8b56-38db6af10056' and ctx.get(f'{user_id}: field_6') == 'None':
                    ctx.set(f'{user_id}: field_6', message.text)
                    keyboard = await buttons.params_2()
                    return await message.answer("Назовите количество объектов недвижимости", keyboard=keyboard)
                elif service_id == '52cc58f4-2f75-46b2-8065-abe1c6ed6889' and ctx.get(f'{user_id}: field_2') == 'None':
                    ctx.set(f'{user_id}: field_2', message.text)
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Укажите сферу услуг, с которой связан ваш вопрос", keyboard=keyboard)
                elif service_id == '52cc58f4-2f75-46b2-8065-abe1c6ed6889' and ctx.get(f'{user_id}: field_3') == 'None':

                    ctx.set('field_3', message.text)

                    res = {
                        "casecount": int(ctx.get(f'{user_id}: field_1')),
                        "fields":
                        {
                            "48b24708-ad36-4aa7-9772-17940e7741c8": ctx.get(f'{user_id}: field_2'),
                            "cf535155-7337-4310-84d5-3e6e720bf36e": ctx.get(f'{user_id}: field_3')
                        }
                    }
                    fields = json.dumps((res),ensure_ascii=False)

                    ctx.set(f'{user_id}: fields', fields)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                    print('--------------------------------------------')
                    await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                    print(*SSR)
                    print(ctx.get(f'{user_id}: fields'))
                    print('--------------------------------------------')
                    keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                    keyboard_data = json.loads(keyboard)
                    payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                    payload = eval(str(payload_value))['cmd']
                    if payload == 'menu':
                        return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                    else:
                        return await message.answer("Выберите свободную дату", keyboard=keyboard)

                elif service_id == '81914e42-5ce6-477a-a49c-52299d37f8ca' and ctx.get(f'{user_id}: field_2') == 'None':
                    ctx.set(f'{user_id}: field_2', message.text)
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Изложите суть вопроса", keyboard=keyboard)
                elif service_id == '81914e42-5ce6-477a-a49c-52299d37f8ca' and ctx.get(f'{user_id}: field_3') == 'None':
                    ctx.set(f'{user_id}: field_3', message.text)
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Адрес электронной почты", keyboard=keyboard)
                elif service_id == '79d77421-c234-4f8b-a643-bb31c79d388d' and ctx.get(f'{user_id}: field_3') == 'None':
                    ctx.set(f'{user_id}: field_3', message.text)
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Адрес электронной почты", keyboard=keyboard)
                elif service_id == '81914e42-5ce6-477a-a49c-52299d37f8ca' and ctx.get(f'{user_id}: field_4') == 'None':
                    ctx.set(f'{user_id}: field_4', message.text)
                    keyboard = await buttons.yes_no()
                    return await message.answer("Хочу получить консультацию не выходя из дома (ОБЯЗАТЕЛЬНО УКАЗАТЬ АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ!)", keyboard=keyboard)
                elif service_id == '79d77421-c234-4f8b-a643-bb31c79d388d' and ctx.get(f'{user_id}: field_4') == 'None':
                    ctx.set(f'{user_id}: field_4', message.text)
                    keyboard = await buttons.yes_no()
                    return await message.answer("Хочу получить консультацию не выходя из дома (ОБЯЗАТЕЛЬНО УКАЗАТЬ АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ!)", keyboard=keyboard)
                else:
                    keyboard = await buttons.menu_menu()
                    return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)

            if service_id == '8f5e514e-dcce-41cf-8b56-38db6af10056' and ctx.get(f'{user_id}: field_6') == 'None':
                ctx.set(f'{user_id}: field_1', payload_data)
                keyboard = await buttons.menu_menu()
                return await message.answer("Введите адрес объекта", keyboard=keyboard)
            elif service_id == '52cc58f4-2f75-46b2-8065-abe1c6ed6889' and ctx.get(f'{user_id}: field_1') == 'None':
                ctx.set(f'{user_id}: field_1', payload_data)
                keyboard = await buttons.menu_menu()
                return await message.answer("Кратко изложите суть обращения", keyboard=keyboard)
            elif service_id == '79d77421-c234-4f8b-a643-bb31c79d388d' and ctx.get(f'{user_id}: field_1') == 'None':
                ctx.set(f'{user_id}: field_1', payload_data)
                keyboard = await buttons.menu_menu()
                return await message.answer("Кратко изложите суть обращения", keyboard=keyboard)
            elif service_id in ('976eb69d-83cb-42b9-893a-926e11956393', 'f94fd42b-611b-460a-8270-059526b40d35') and ctx.get(f'{user_id}: field_1') == 'None':
                ctx.set(f'{user_id}: field_1', payload_data)
                keyboard = await buttons.yes_no()
                return await message.answer("Обращается иностранный гражданин?", keyboard=keyboard)
            elif service_id == '81914e42-5ce6-477a-a49c-52299d37f8ca' and ctx.get(f'{user_id}: field_1') == 'None':
                ctx.set(f'{user_id}: field_1', payload_data)
                keyboard = await buttons.menu_menu()
                return await message.answer("Укажите тип объекта недвижимости (жилое помещение, квартира; нежилое помещение; земельный участок)", keyboard=keyboard)

            if payload_data in numbers or 'yes' in payload_data or 'no' in payload_data or ctx.get(f'{user_id}: button_cache_file_files') == 'yes':
                if service_id == '8f5e514e-dcce-41cf-8b56-38db6af10056' and field_2 == 'None':
                    ctx.set(f'{user_id}: field_2', payload_data)
                    keyboard = await buttons.params_1()
                    await message.answer("Назовите количество участников сделки", keyboard=keyboard)
                elif service_id == '8f5e514e-dcce-41cf-8b56-38db6af10056' and field_3 == 'None':
                    ctx.set(f'{user_id}: field_3', payload_data)
                    keyboard = await buttons.yes_no()
                    await message.answer("Уточните, планируется ли использовать средства материнского капитала или кредитные средства?", keyboard=keyboard)
                elif service_id == '8f5e514e-dcce-41cf-8b56-38db6af10056' and field_4 == 'None':
                    ctx.set(f'{user_id}: field_4', payload_data)
                    keyboard = await buttons.yes_no()
                    await message.answer("Уточните, необходимо ли составить договор купли-продажи или дарения?", keyboard=keyboard)
                elif ctx.get(f'{user_id}: button_cache_file_start') != 'yes' and service_id == '8f5e514e-dcce-41cf-8b56-38db6af10056' and field_5 == 'None':
                    ctx.set(f'{user_id}: field_5', payload_data)

                    if ctx.get(f'{user_id}: field_4') == 'yes':
                        kolvo_sred = '1'
                    elif ctx.get(f'{user_id}: field_4') == 'no':
                        kolvo_sred = '0'

                    if ctx.get(f'{user_id}: field_5') == 'yes':
                        kolvo_dog = '1'
                    elif ctx.get(f'{user_id}: field_5') == 'no':
                        kolvo_dog = '0'

                    res = {
                        "casecount": int(ctx.get(f'{user_id}: field_1')),
                        "fields":
                        {
                            "aa50aae2-8879-4945-9553-825e911fc9c4": ctx.get(f'{user_id}: field_6'),
                            "6e349207-5486-4efa-90a2-0f5b86765b36": ctx.get(f'{user_id}: field_3'),
                            "cb3e610a-49cc-45c3-a7e4-7867036551ea": ctx.get(f'{user_id}: field_2'),
                            "fec9e657-aa1c-428a-a7d9-c4d977d7cccd": kolvo_sred,
                            "6c8b9903-e522-4d95-af0d-d7d1f688aa62": kolvo_dog,
                        }
                    }
                    fields = json.dumps((res),ensure_ascii=False)

                    ctx.set(f'{user_id}: fields', fields)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                    print('--------------------------------------------')
                    await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                    print(*SSR)
                    print(ctx.get(f'{user_id}: fields'))
                    print('--------------------------------------------')
                    keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                    keyboard_data = json.loads(keyboard)
                    payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                    payload = eval(str(payload_value))['cmd']
                    if payload == 'menu':
                        return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                    else:
                        return await message.answer("Выберите свободную дату", keyboard=keyboard)

                elif ctx.get(f'{user_id}: button_cache_file_start') == 'yes' and service_id == '8f5e514e-dcce-41cf-8b56-38db6af10056' and field_5 == 'None':
                    ctx.set(f'{user_id}: field_5', payload_data)

                    if ctx.get(f'{user_id}: field_4') == 'yes':
                        kolvo_sred = '1'
                    elif ctx.get(f'{user_id}: field_4') == 'no':
                        kolvo_sred = '0'

                    if ctx.get(f'{user_id}: field_5') == 'yes':
                        kolvo_dog = '1'
                    elif ctx.get(f'{user_id}: field_5') == 'no':
                        kolvo_dog = '0'

                    res = {
                        "casecount": int(ctx.get(f'{user_id}: field_1')),
                        "fields":
                        {
                            "aa50aae2-8879-4945-9553-825e911fc9c4": ctx.get(f'{user_id}: field_6'),
                            "6e349207-5486-4efa-90a2-0f5b86765b36": ctx.get(f'{user_id}: field_3'),
                            "cb3e610a-49cc-45c3-a7e4-7867036551ea": ctx.get(f'{user_id}: field_2'),
                            "fec9e657-aa1c-428a-a7d9-c4d977d7cccd": kolvo_sred,
                            "6c8b9903-e522-4d95-af0d-d7d1f688aa62": kolvo_dog,
                        }
                    }
                    fields = json.dumps((res),ensure_ascii=False)

                    ctx.set(f'{user_id}: fields', fields)

                    ctx.set(f'{user_id}: cache_files', 'yes')

                    ctx.set(f'{user_id}: button_cache_file', 'yes')
                    keyboard = await buttons.menu_menu_file()
                    return await message.answer("Загрузите непустые страницы вашего паспорта.", keyboard=keyboard)

                elif service_id == '81914e42-5ce6-477a-a49c-52299d37f8ca' and field_5 == 'None':
                    ctx.set(f'{user_id}: field_5', payload_data)

                    if ctx.get(f'{user_id}: field_5') == 'yes':
                        kolvo_sred = '1'
                    elif ctx.get(f'{user_id}: field_5') == 'no':
                        kolvo_sred = '0'

                    res = {
                        "casecount": int(ctx.get(f'{user_id}: field_1')),
                        "fields":
                        {
                            "b1a8f2ae-3a16-4018-ad69-0a843e61796c": ctx.get(f'{user_id}: field_2'),
                            "667a73c2-e026-483d-8033-1caadcea8f99": ctx.get(f'{user_id}: field_3'),
                            "a3e9a616-5b11-4e59-89f4-be72b3d5bffc": kolvo_sred,
                            "fbc884bf-b18b-4591-8f4d-fd229b9dc11d": ctx.get(f'{user_id}: field_4')
                        }
                    }
                    fields = json.dumps((res),ensure_ascii=False)

                    ctx.set(f'{user_id}: fields', fields)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                    print('--------------------------------------------')
                    await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                    print(*SSR)
                    print(ctx.get(f'{user_id}: fields'))
                    print('--------------------------------------------')
                    keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                    keyboard_data = json.loads(keyboard)
                    payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                    payload = eval(str(payload_value))['cmd']
                    if payload == 'menu':
                        return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                    else:
                        return await message.answer("Выберите свободную дату", keyboard=keyboard)

                elif service_id == '79d77421-c234-4f8b-a643-bb31c79d388d' and field_5 == 'None':
                    ctx.set(f'{user_id}: field_5', payload_data)

                    if ctx.get(f'{user_id}: field_5') == 'yes':
                        kolvo_sred = '1'
                    elif ctx.get(f'{user_id}: field_5') == 'no':
                        kolvo_sred = '0'

                    res = {
                        "casecount": int(ctx.get(f'{user_id}: field_1')),
                        "fields":
                        {
                            "541f0b86-f354-40ae-b2cc-71b091929e31": ctx.get(f'{user_id}: field_3'),
                            "64be467d-5881-416e-be81-fc697334b6e4": ctx.get(f'{user_id}: field_4'),
                            "59b6fc18-2721-4a0f-b273-4fb9c9f7871a": kolvo_sred
                        }
                    }
                    fields = json.dumps((res),ensure_ascii=False)

                    ctx.set(f'{user_id}: fields', fields)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                    print('--------------------------------------------')
                    await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                    print(*SSR)
                    print(ctx.get(f'{user_id}: fields'))
                    print('--------------------------------------------')
                    keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                    keyboard_data = json.loads(keyboard)
                    payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                    payload = eval(str(payload_value))['cmd']
                    if payload == 'menu':
                        return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                    else:
                        return await message.answer("Выберите свободную дату", keyboard=keyboard)

                elif service_id in ('976eb69d-83cb-42b9-893a-926e11956393', 'f94fd42b-611b-460a-8270-059526b40d35') and field_5 == 'None':
                    ctx.set(f'{user_id}: field_5', payload_data)

                    if ctx.get(f'{user_id}: field_5') == 'yes':
                        foreign = '1'
                    elif ctx.get(f'{user_id}: field_5') == 'no':
                        foreign = '0'

                    res = {
                        "casecount": int(ctx.get(f'{user_id}: field_1')),
                        "fields":
                        {
                            "5eddb5e1-aa68-4534-9417-49fc4f7c26dc": foreign,
                            "2703ff9e-319c-4b0a-a152-67b3614839d1": foreign
                        }
                    }
                    fields = json.dumps((res),ensure_ascii=False)

                    ctx.set(f'{user_id}: fields', fields)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                    print('--------------------------------------------')
                    await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                    print(*SSR)
                    print(ctx.get(f'{user_id}: fields'))
                    print('--------------------------------------------')
                    keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                    keyboard_data = json.loads(keyboard)
                    payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                    payload = eval(str(payload_value))['cmd']
                    if payload == 'menu':
                        return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                    else:
                        return await message.answer("Выберите свободную дату", keyboard=keyboard)

                elif service_id != '8f5e514e-dcce-41cf-8b56-38db6af10056' and \
                    service_id != '52cc58f4-2f75-46b2-8065-abe1c6ed6889' and \
                    service_id != '81914e42-5ce6-477a-a49c-52299d37f8ca' and \
                    service_id != '976eb69d-83cb-42b9-893a-926e11956393' and \
                    service_id != 'f94fd42b-611b-460a-8270-059526b40d35' and \
                    service_id != '79d77421-c234-4f8b-a643-bb31c79d388d' and field_1 == 'None':

                    ctx.set(f'{user_id}: field_1', payload_data)

                    res = {
                        "casecount": int(ctx.get(f'{user_id}: field_1')),
                        "fields":{}
                    }
                    fields = json.dumps((res),ensure_ascii=False)

                    ctx.set(f'{user_id}: fields', fields)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                    print('--------------------------------------------')
                    await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                    print(*SSR)
                    print(ctx.get(f'{user_id}: fields'))
                    print('--------------------------------------------')
                    keyboard = await buttons.date_1(*SSR, ctx.get(f'{user_id}: fields'))
                    keyboard_data = json.loads(keyboard)
                    payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                    payload = eval(str(payload_value))['cmd']
                    if payload == 'menu':
                        return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                    else:
                        return await message.answer("Выберите свободную дату", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ fields', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.DATE)
    async def handler_date(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ handler_date', user_id)
            users_info = await bot.api.users.get(message.from_id)
            try:
                payload_data = eval(message.payload)['cmd']
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)

            if payload_data == 'date_ost':
                SSR = (ctx.get(f'{user_id}: date'),
                    ctx.get(f'{user_id}: time'),
                    ctx.get(f'{user_id}: department'),
                    ctx.get(f'{user_id}: service'),
                    ctx.get(f'{user_id}: fields'))
                print('--------------------------------------------')
                await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_2', user_id)
                print(*SSR)
                print('--------------------------------------------')
                keyboard = await buttons.date_2(*SSR)
                return await message.answer("Выберите свободную дату", keyboard=keyboard)

            if payload_data == 'back':
                contexts = {"field_1": None, "field_2": None,
                        "field_3": None, "field_4": None,
                        "field_5": None, "field_6": None,
                        "field_7": None, "date": None,
                        "time": None}

                for context in contexts:
                    ctx.set(f"{user_id}: {context}", "None")

                await bot.state_dispenser.set(message.peer_id, SuperStates.SERVICE)
                keyboard = await buttons.services_section(ctx.get(f'{user_id}: department'))
                return await message.answer("Выберите услугу", keyboard=keyboard)
            elif payload_data == 'menu':

                await notification_delete_coupon(user_id, message)

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            elif payload_data == 'accept_entry':
                await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            ctx.set(f'{user_id}: date', payload_data)

            SSR = (ctx.get(f'{user_id}: department'),
                    ctx.get(f'{user_id}: service'),
                    ctx.get(f'{user_id}: fields'))

            await bot.state_dispenser.set(message.peer_id, SuperStates.TIME)
            keyboard, times = await buttons.times_buttons(ctx.get(f'{user_id}: date'), ctx.get(f'{user_id}: time'), *SSR)
            ctx.set(f'{user_id}: times', times)
            await message.answer("Выберите свободное время", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ handler_date', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message(state=SuperStates.TIME)
    async def handler_time(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ handler_time', user_id)
            users_info = await bot.api.users.get(message.from_id)
            try:
                payload_data = eval(message.payload)['cmd']
            except:
                keyboard = await buttons.menu_menu()
                return await message.answer("Вы ввели некорректные данные", keyboard=keyboard)

            SSR = (ctx.get(f'{user_id}: department'),
                    ctx.get(f'{user_id}: service'),
                    ctx.get(f'{user_id}: fields'))

            if payload_data == 'back':
                ctx.set(f'{user_id}: time', 'None')
                await bot.state_dispenser.set(message.peer_id, SuperStates.TIME)
                keyboard, times = await buttons.times_buttons(ctx.get(f'{user_id}: date'), ctx.get(f'{user_id}: time'), *SSR)
                ctx.set(f'{user_id}: times', times)
                keyboard_data = json.loads(keyboard)
                payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                payload = eval(str(payload_value))['cmd']
                if payload == 'menu' or payload == 'back':
                    return await message.answer("На эту услугу нет свободного времени", keyboard=keyboard)
                else:
                    return await message.answer("Выберите свободную дату", keyboard=keyboard)

            elif payload_data == 'menu':

                await notification_delete_coupon(user_id, message)

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            elif payload_data == 'accept_entry':
                await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

            elif payload_data == 'back_1':
                ctx.set(f'{user_id}: date', 'None')
                ctx.set(f'{user_id}: time', 'None')
                await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                print('--------------------------------------------')
                await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                print(ctx.get(f'{user_id}: date'))
                print(ctx.get(f'{user_id}: time'))
                print(*SSR)
                print('--------------------------------------------')
                keyboard = await buttons.date_1(ctx.get(f'{user_id}: date'), ctx.get(f'{user_id}: time'), *SSR)
                return await message.answer("Выберите свободную дату", keyboard=keyboard)
            elif payload_data == 'yes':
                await bot.state_dispenser.set(message.peer_id, SuperStates.PHONE)
                keyboard = await buttons.fio_yes()
                return await message.answer("Введите вашу ФИО или можете использовать Фамилию Имя профиля", keyboard=keyboard)
            elif payload_data == 'no':
                await bot.state_dispenser.set(message.peer_id, SuperStates.PHONE_INPUT_NEW)
                return await message.answer("Введите ваш номер телефона (например, 88003500850)")

            # commands_5 = {
            #     'time_ost_2': buttons.time_2,
            #     'time_ost_3': buttons.time_3,
            #     'time_ost_4': buttons.time_4,
            #     'time_ost_5': buttons.time_5,
            #     'time_ost_6': buttons.time_6,
            #     'time_ost_7': buttons.time_7,
            #     'time_ost_8': buttons.time_8,
            #     'time_ost_9': buttons.time_9,
            #     'time_ost_10': buttons.time_10,
            #     'time_ost_11': buttons.time_11,
            #     'time_ost_12': buttons.time_12
            # }

            # # Пример вызова функции по ключу
            # if payload_data in commands_5:
            #     function_to_call = commands_5[payload_data]
            #     keyboard = await function_to_call(ctx.get(f'{user_id}: times'))
            #     keyboard_data = json.loads(keyboard)
            #     payload_value = keyboard_data['buttons'][0][0]['action']['payload']
            #     payload = eval(str(payload_value))['cmd']
            #     if payload == 'menu' or payload == 'back':
            #         return await message.answer("На этот промежуток нет свободного времени", keyboard=keyboard)
            #     else:
            #         payload_value = keyboard_data['buttons'][0][0]['action']['payload']
            #         payload = eval(str(payload_value))['cmd']
            #         if payload in commands_5:
            #             return await message.answer("В этом диапазоне время занято. Нажмите кнопку 'Остальное время'", keyboard=keyboard)
            #         else:
            #             return await message.answer("Выберите свободное время", keyboard=keyboard)

            if not payload_data in times_list:
                ctx.set(f'{user_id}: time', payload_data)

            commands_4 = {
                '800': buttons.time_1,
                '900': buttons.time_2,
                '1000': buttons.time_3,
                '1100': buttons.time_4,
                '1200': buttons.time_5,
                '1300': buttons.time_6,
                '1400': buttons.time_7,
                '1500': buttons.time_8,
                '1600': buttons.time_9,
                '1700': buttons.time_10,
                '1800': buttons.time_11,
                '1900': buttons.time_12
            }

            # lists_1 = {'time_ost_2', 'time_ost_3', 'time_ost_4', 'time_ost_5',
            #         'time_ost_6', 'time_ost_7', 'time_ost_8', 'time_ost_9', 'time_ost_10',
            #         'time_ost_11', 'time_ost_12'}
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ handler_time', user_id)
            # Пример вызова функции по ключу
            if payload_data in commands_4:
                function_to_call = commands_4[payload_data]
                print('--------------------------------------------')
                await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ time', user_id)
                print(ctx.get(f'{user_id}: times'))
                print('--------------------------------------------')
                keyboard = await function_to_call(ctx.get(f'{user_id}: times'))
                keyboard_data = json.loads(keyboard)
                payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                payload = eval(str(payload_value))['cmd']
                if payload == 'menu':
                    return await message.answer("На эту услугу нет свободного времени", keyboard=keyboard)
                # elif payload in lists_1:
                #     return await message.answer("На этот промежуток нет свободного времени", keyboard=keyboard)
            else:
                keyboard = await buttons.yes_no()
                return await message.answer(f"Обращаем Ваше внимание, что прием осуществляется только при соответствии информации, указанной в талоне, с данными заявителя.\n\nДля записи на приём использовать номер телефона {ctx.get(f'{user_id}: phone')}?", keyboard=keyboard)
            return await message.answer("Выберите свободное время", keyboard=keyboard)

        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    import re

    @bot.on.message(state=SuperStates.PHONE)
    async def handler_fio(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ handler_fio', user_id)

            users_info = await bot.api.users.get(message.from_id)
            first_name = users_info[0].first_name
            last_name = users_info[0].last_name

            SSR = (ctx.get(f'{user_id}: department'),
                    ctx.get(f'{user_id}: service'),
                    ctx.get(f'{user_id}: fields'))

            user_text = None

            try:
                payload_data = eval(message.payload)['cmd']
                if payload_data == 'back':
                    ctx.set(f'{user_id}: time', 'None')
                    await bot.state_dispenser.set(message.peer_id, SuperStates.TIME)
                    keyboard, times = await buttons.times_buttons(ctx.get(f'{user_id}: date'), ctx.get(f'{user_id}: time'), *SSR)
                    ctx.set(f'{user_id}: times', times)
                    return await message.answer("Выберите свободное время", keyboard=keyboard)
                elif payload_data == 'menu':

                    await notification_delete_coupon(user_id, message)

                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')

                elif payload_data == 'yes_fi' and user_text is None:
                    user_text = f"{last_name} {first_name}"

            except:
                user_text = message.text

            count_space = 0
            for char in message.text :
                if char == ' ':  # Проверяем, что текущий символ является пробелом
                    count_space += 1

            count_text = 0
            for char in message.text :
                if char != ' ':  # Проверяем, что текущий символ не является пробелом
                    count_text += 1

            if count_space > 3:
                keyboard = await buttons.menu_menu()
                return await message.answer("Ваше ФИО содержит много пробелов. Пожалуйста, повторите ввод ещё раз.", keyboard=keyboard)
            elif count_text > 30:
                keyboard = await buttons.menu_menu()
                return await message.answer("Ваше ФИО слишком длинное. Пожалуйста, повторите ввод ещё раз.", keyboard=keyboard)

            ctx.set(f'{user_id}: fio', user_text)

            async def write_to_file(text):
                import os
                # Указываем директорию для сохранения файла
                folder_path = 'C:\\Users\\neverov\\Desktop\\file'  # Укажите путь к папке
                os.makedirs(folder_path, exist_ok=True)  # Создает папку, если она не существует

                file_path = os.path.join(folder_path, f'info_{user_id}.txt')  # Путь к файлу

                # Асинхронно записываем текст в файл
                async with aiofiles.open(file_path, 'a', encoding='utf-8') as file:
                    await file.write(text)

            res = await base(user_id=user_id, tel = ctx.get(f'{user_id}: phone')).base_record(ctx.get(f'{user_id}: fio'), ctx.get(f'{user_id}: department'), ctx.get(f'{user_id}: service'), ctx.get(f'{user_id}: time'), ctx.get(f'{user_id}: date'), ctx.get(f'{user_id}: fields'))
            if res['code'] == 'ok':

                if ctx.get(f'{user_id}: cache_files') == 'yes':
                    answer_1 = f"{ctx.get(f'{user_id}: fio')}, {ctx.get(f'{user_id}: phone')}, Номер талона: " + str(res['number']) + ', дата визита: ' + str(res['dateTime'] + ', время визита: ' + str(res['visitTime']) + ', место визита: ' + str(res["department"]))
                    await write_to_file(answer_1)

                answer = "Вы записаны. Ваш номер талона: " + str(res['number']) + ', дата визита: ' + str(res['dateTime'] + ', время визита: ' + str(res['visitTime']) + ', место визита: ' + str(res["department"]))
                await message.answer(answer)

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
            elif res['code'] == 'err_no_slots':

                ctx.set(f'{user_id}: date', 'None')
                ctx.set(f'{user_id}: time', 'None')

                await bot.state_dispenser.set(message.peer_id, SuperStates.DATE)
                print('--------------------------------------------')
                await debug_print('ПЕРЕД ВХОДОМ В ФУНКЦИЮ date_1', user_id)
                print(ctx.get(f'{user_id}: date'))
                print(ctx.get(f'{user_id}: time'))
                print(*SSR)
                print('--------------------------------------------')
                keyboard = await buttons.date_1(ctx.get(f'{user_id}: date'), ctx.get(f'{user_id}: time'), *SSR)
                keyboard_data = json.loads(keyboard)
                payload_value = keyboard_data['buttons'][0][0]['action']['payload']
                payload = eval(str(payload_value))['cmd']
                if payload == 'menu':
                    return await message.answer("На эту услугу нет свободных дат", keyboard=keyboard)
                else:
                    return await message.answer("Не удалось записаться. Возможно это время уже заняли. Пожалуйста попробуйте ещё раз выбрать свободную дату", keyboard=keyboard)
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ handler_fio', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            await bot.state_dispenser.set(message.peer_id, SuperStates.MENU)
            keyboard = await buttons.menu_menu()
            await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    @bot.on.message()
    @bot.on.message(state=SuperStates.MENU)
    async def handler(message: Message):
        try:
            user_id = message.from_id
            await debug_print('ВХОД В ФУНКЦИЮ handler', user_id)
            users_info = await bot.api.users.get(message.from_id)

            try:
                payload_data = eval(message.payload)['cmd']

                if payload_data.startswith('delete_coupons_'):
                    ctx.set(f'{user_id}: yes_no_cache', 'yes')

                    ctx.set(f'{user_id}: talon_id_cache', [payload_data.split('_')[2]])
                    ctx.set(f'{user_id}: esiaid_cache', [''])
                    ctx.set(f'{user_id}: code_cache', [payload_data.split('_')[3]])
                    ctx.set(f'{user_id}: department_cache', [payload_data.split('_')[4]])
                    ctx.set(f'{user_id}: date_cache', [payload_data.split('_')[5]])
                    ctx.set(f'{user_id}: code_counter', 0)
                    ctx.set(f'{user_id}: tel_cache', payload_data.split('_')[6])
                    ctx.set(f'{user_id}: fio', payload_data.split('_')[7])

                    await bot.state_dispenser.set(message.peer_id, SuperStates.DEL_COUPONS)
                    keyboard = await buttons.yes_no()
                    return await message.answer(f"Вы точно хотите удалить талон {payload_data.split('_')[3]}?", keyboard=keyboard)
                elif payload_data == 'menu':

                    await notification_delete_coupon(user_id, message)

                if payload_data == 'accept_entry':
                    await base(user_id = user_id).delete_vkontakte_reg(ctx.get(f'{user_id}: talon_select_vkontakte_reg'), ctx.get(f'{user_id}: department_select_vkontakte_reg'))
                    await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                    await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                    # Очистка всех переменных
                    await reset_ctx(user_id)
                    return await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню')
            except:
                pass

            answer = await base(user_id = user_id).phone_select()

            agreement_answer = await base(user_id = user_id).agreement_select()

            if not agreement_answer:
                async def read_file():
                    async with aiofiles.open('files\\agreement.txt', mode='r', encoding='utf-8') as file:
                        contents = await file.read()
                        return contents

                if answer[0]:
                    ctx.set(f'{user_id}: phone', answer[1][0][0])
                await bot.state_dispenser.set(message.peer_id, SuperStates.AGREEMENT_INPUT)
                keyboard = await buttons.agreement_yes_no()
                return await message.answer(f"{await read_file()}", keyboard=keyboard)

            if answer[0]:

                ctx.set(f'{user_id}: phone', answer[1][0][0])

                photo = "photo-224967611_457239778"

                await bot.state_dispenser.set(message.peer_id, SuperStates.FILIALS)
                await buttons.menu(user_id, config["VKONTAKTE"]["token"])
                # Очистка всех переменных
                await reset_ctx(user_id)
                await message.answer("{}".format(users_info[0].first_name) + ', Вы в главном меню', attachment=photo)
            else:
                await bot.state_dispenser.set(message.peer_id, SuperStates.PHONE_INPUT)
                return await message.answer("Для полноценного пользования чат-ботом необходимо пройти регистрацию. Пожалуйста, укажите ВАШ постоянный номер телефона, который будет связан с вашим аккаунтом.(например, 88003500850)")
            await debug_print('ВЫХОД ИЗ ФУНКЦИИ handler', user_id)
            return
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()
            keyboard = await buttons.menu_menu()
            return await message.answer("Ошибка соединения с сервером", keyboard=keyboard)

    print('The bot has started!')
    bot.run_forever()

import requests
import random
import time
import mysql.connector
import datetime

def process_5():
    def post_message(ani, talon, time, date, department, service):

        message = f"У вас скоро приём {date} в {time}! Номер вашего талона: {talon}, филиал: {department}, услуга: {service}.\n\nНажмите /start для того, что бы подтвердить или удалить вашу запись."

        def keyboards_dates():
            result = []
            temp = []

            temp.append({"text": f"/start", "callback_data": "/start"})
            result.append(temp)

            return result

        # keyboard = {
        #     "inline_keyboard": keyboards_dates()
        # }

        keyboard = {
            "keyboard": keyboards_dates(),
            "resize_keyboard": True
        }

        data = {
            "chat_id": ani,
            "text": message,
            "reply_markup": json.dumps(keyboard)
        }

        requests.post(f"https://api.telegram.org/bot6910991480:AAHecZctB4SuhT6AWfPbPb7SuxH97mONzN0/sendMessage", data=data)
        # """ОТКЛЮЧИЛ ОСНОВНОЙ ТБ"""
        requests.post(f"https://api.telegram.org/bot6080361959:AAEh7oc1ftSeK7h1vAn2Pu-60nZ656xkcsM/sendMessage", data=data)

    server = "https://equeue.mfc.tomsk.ru"

    while True:
        try:

            now = datetime.datetime.now()
            date_now = now + datetime.timedelta(hours=24)
            date_formatted = date_now.strftime('%Y-%m-%d')
            time_formatted = date_now.strftime('%H:%M')

            if str(time_formatted) == '15:00':

                with mysql.connector.connect(
                    host="172.18.11.103",
                    user="root",
                    password="enigma1418",
                    database="mdtomskbot",
                ) as mydb:
                    mycursor = mydb.cursor()
                    mycursor.execute(
                        f"SELECT * FROM telegram_reg;"
                    )
                    myresult = mycursor.fetchall()

                    for x in myresult:
                        service = x[3]
                        if service == str(date_formatted) and x[9] != 'yes':
                            if not x[6] == None:
                                prms = {
                                    'uuid': x[6]
                                }

                                talon = requests.get(server + "/rest/booking", params=prms, timeout=(5, 8)).json()

                                if not talon['data'] == []:
                                    post_message(x[0], x[1], x[2], x[3], x[4], x[5])
                                    query = "UPDATE telegram_reg SET now = %s WHERE ani = %s AND date = %s;"
                                    mycursor.execute(query, ('yes', x[0], x[3]))
                                    mydb.commit()
                                else:
                                    query = "DELETE FROM telegram_reg WHERE ani = %s AND date = %s AND talon = %s AND department = %s;"
                                    mycursor.execute(query, (x[0], x[3], x[1], x[4]))
                                    mydb.commit()

            continue

        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

def process_2():
    def post_message(user_id, talon, time, date, department, service, uuid, tel, fio):
        # Данные для авторизации
        access_token = config["VKONTAKTE"]["token"]
        api_version = "5.199"
        message = f"У вас скоро приём {date} в {time}! Номер вашего талона {talon}, филиал: {department}, услуга: {service}"

        # Генерация случайного числа для random_id
        random_id = random.getrandbits(31)

        # URL для отправки сообщения
        url = f"https://api.vk.com/method/messages.send"

        # Параметры запроса
        params = {
            "access_token": access_token,
            "v": api_version,
            "user_id": user_id,
            "message": message,
            "random_id": random_id
        }

        # Отправляем POST-запрос
        requests.post(url, params=params)

        keyboard = {
            "one_time": True,
            "buttons": [
                # [
                #     {
                #         "action": {
                #             "type": "text",
                #             "label": "Удалить запись",
                #             "payload": f"{{\"cmd\": \"delete_coupons_{uuid}_{talon}_{department}_{date}_{tel}_{fio}\"}}"
                #         },
                #         "color": "negative"
                #     }
                # ],
                [
                    {
                        "action": {
                            "type": "text",
                            "label": "Продолжить",
                            "payload": "{\"cmd\": \"menu\"}"
                        },
                        "color": "positive"
                    }
                ]
            ]
        }

        import time

        message = 'ㅤ'

        # Функция для генерации "случайных" чисел без использования модуля random
        def custom_random():
            current_time = time.time()
            seed = int((current_time - int(current_time)) * 10**6)  # Используем миллионные доли секунды в качестве зерна для "случайности"
            next_number = (1103515245 * seed + 12345) % 2**31  # Простой линейный конгруэнтный генератор
            return next_number

        # Отправка сообщения с клавиатурой
        payload = {
            'access_token': access_token,
            'peer_id': user_id,
            'message': message,
            'keyboard': json.dumps(keyboard),
            'random_id': custom_random(),
            'v': '5.199'  # Добавляем версию API
        }

        requests.post('https://api.vk.com/method/messages.send', params=payload)

    server = "https://equeue.mfc.tomsk.ru"

    while True:
        try:

            now = datetime.datetime.now()
            date_now = now + datetime.timedelta(hours=24)
            date_formatted = date_now.strftime('%Y-%m-%d')
            time_formatted = date_now.strftime('%H:%M')

            if str(time_formatted) == '15:00':

                with mysql.connector.connect(
                    host="172.18.11.103",
                    user="root",
                    password="enigma1418",
                    database="mdtomskbot",
                    connection_timeout=2
                ) as mydb:
                    mycursor = mydb.cursor()
                    mycursor.execute(
                        f"SELECT * FROM vkontakte_reg;"
                    )
                    myresult = mycursor.fetchall()

                    for x in myresult:
                        service = x[3]
                        if service == str(date_formatted) and x[9] != 'yes':
                            if not x[6] == None:
                                prms = {
                                    'uuid': x[6]
                                }

                                talon = requests.get(server + "/rest/booking", params=prms, timeout=(5, 8)).json()

                                if not talon['data'] == []:
                                    post_message(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])
                                    query = "UPDATE vkontakte_reg SET now = %s WHERE sender = %s AND date = %s;"
                                    mycursor.execute(query, ('yes', x[0], x[3]))
                                    mydb.commit()
                                else:
                                    query = "DELETE FROM vkontakte_reg WHERE sender = %s AND date = %s AND talon = %s AND department = %s;"
                                    mycursor.execute(query, (x[0], x[3], x[1], x[4]))
                                    mydb.commit()

            continue

        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

from mysql.connector import errors

def process_4():
    def post_message(user_id_vk, user_id_tb, event, date, platform, now):

        import re
        pattern_date = r'\d{4}-\d{2}-\d{2}'
        if not re.search(pattern_date, str(date)):
            date = 'error'

        # Создаем правильное имя файла
        filename = f'{event}\\{date}.txt'

        def read_file():
            with open(filename, mode='r', encoding='utf-8') as file:
                contents = file.read()
                return contents

        # Данные для авторизации
        access_token = config["VKONTAKTE"]["token"]
        api_version = "5.199"
        if not now == 'yes':
            message = f"Напоминаю, вы хотели посетить:\n\n{read_file()}"
        else:
            message = f"{read_file()}"

        # Генерация случайного числа для random_id
        random_id = random.getrandbits(31)

        # URL для отправки сообщения
        url = f"https://api.vk.com/method/messages.send"

        # Параметры запроса
        params = {
            "access_token": access_token,
            "v": api_version,
            "user_id": user_id_vk,
            "message": message,
            "random_id": random_id
        }

        if platform == 'VK':
            # Отправляем POST-запрос
            requests.post(url, params=params)

        data = {
            "chat_id": user_id_tb,
            "text": message
        }

        if platform == 'TB':
            requests.post(f"https://api.telegram.org/bot6910991480:AAHecZctB4SuhT6AWfPbPb7SuxH97mONzN0/sendMessage", data=data)
            requests.post(f"https://api.telegram.org/bot6080361959:AAEh7oc1ftSeK7h1vAn2Pu-60nZ656xkcsM/sendMessage", data=data)

    # Создание одиночного соединения
    dbconfig = {
        'host': "172.18.11.103",
        'user': "root",
        'password': "enigma1418",
        'database': "mdtomskbot",
    }

    connection = mysql.connector.connect(**dbconfig)

    # Выполнение запросов и обновление данных
    try:
        cursor = connection.cursor()

        while True:
            # global exit_event
            update_query = "SELECT * FROM events;"

            cursor.execute(update_query)
            myresult = cursor.fetchall()

            now = datetime.datetime.now()
            date_now = now + datetime.timedelta(hours=24)
            date_formatted = date_now.strftime('%Y-%m-%d')

            for x in myresult:
                if x[5] == 'yes':
                    post_message(x[0], x[1], x[2], x[3], x[4], x[5])
                    query = f"DELETE FROM events WHERE id_vk = %s OR id_tb = %s AND date = %s AND now = %s;"
                    cursor.execute(query, (x[0], x[1], x[3], 'yes'))
                    connection.commit()

            connection.commit()

            now = datetime.datetime.now()
            date_now = now + datetime.timedelta(hours=24)
            date_formatted = date_now.strftime('%Y-%m-%d')
            time_formatted = date_now.strftime('%H:%M')

            if str(time_formatted) == '15:00':
                for x in myresult:
                    if x[3] == str(date_formatted) and x[5] != 'yes':
                        post_message(x[0], x[1], x[2], x[3], x[4], x[5])
                        query = f"DELETE FROM events WHERE id_vk = %s OR id_tb = %s AND date = %s;"
                        cursor.execute(query, (x[0], x[1], x[3]))
                        connection.commit()

                connection.commit()

            continue

    except errors.OperationalError as err:
        if err.errno == 2013:
            pass
    except Exception as e:
        # Вывод подробной информации об ошибке
        print(f"Поймано исключение: {type(e).__name__}")
        print(f"Сообщение об ошибке: {str(e)}")
        import traceback
        print("Трассировка стека (stack trace):")
        traceback.print_exc()

    finally:
        if 'cursor' in locals() or 'cursor' in globals():
            cursor.close()  # Важно закрыть курсор
        if 'connection' in locals() or 'connection' in globals():
            connection.close()  # Важно закрыть соединение после его использования

import time

# Функция для генерации "случайных" чисел без использования модуля random
def custom_random():
    current_time = time.time()
    seed = int((current_time - int(current_time)) * 10**6)  # Используем миллионные доли секунды в качестве зерна для "случайности"
    next_number = (1103515245 * seed + 12345) % 2**31  # Простой линейный конгруэнтный генератор
    return next_number

def process_3():
    token='vk1.a.ywUc9P6kVUI_U1_vqtpbK98hPa59vjEUYNcoaBzZQcDIg_txl8e8XNQzNHR6qfTyPoD9rLxey4BDrMXNyb-wbMzcT43ocNpsuJ8VOrY1ds7S6eSphFkIUrG-Nave6DZ8Cz3b3UQXgDiu_29n61S8IyssFQRl0fLF8h_UFL_U3x5Br5bKoG8krvE6LEl7wOz_pJYkGPABKEKW3mMO_7muXA'
    bot = Bot(token=token)

    @bot.on.message()
    async def handler(message: Message):
        try:
            user_id = message.from_id

            keyboard = {
                "one_time": True,
                "buttons": [
                    [
                        {
                            "action": {
                                "type": "open_link",
                                "label": "Вернуться к боту",
                                "link": "https://vk.com/im?sel=-224967611"
                            }
                        }
                    ]
                ]
            }

            import json

            # Данные для отправки сообщения
            peer_id = user_id # ID пользователя, которому отправляем сообщение
            message = 'ㅤ'

            # Отправка сообщения с клавиатурой
            payload = {
                'access_token': token,
                'peer_id': peer_id,
                'message': message,
                'keyboard': json.dumps(keyboard),
                'random_id': custom_random(),
                'v': '5.199'  # Добавляем версию API
            }

            requests.post('https://api.vk.com/method/messages.send', params=payload)

        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    bot.run_forever()

def process_6():
    import calendars
    calendars.process_calendar()

def process_7():
    import mail
    mail.process_mail()

def process_8():
    import mail
    mail.process_file()

if __name__ == "__main__":

    process1 = Process(target=process_1)
    # process2 = Process(target=process_2)
    """НЕ НУЖНО"""
    # process3 = Process(target=process_3)
    # process4 = Process(target=process_4)
    # process5 = Process(target=process_5)
    # process6 = Process(target=process_6)
    # process7 = Process(target=process_7)
    process8 = Process(target=process_8)

    # process1.start()
    # process2.start()
    # process3.start()
    # process4.start()
    # process5.start()
    # process6.start()
    # process7.start()
    # process8.start()

    # process1.join()
    # process2.join()
    # process3.join()
    # process4.join()
    # process5.join()
    # process6.join()
    # process7.join()
    # process8.join()

    while True:
        if not process1.is_alive():
            process1 = Process(target=process_1)
            process1.start()
            # process1.join()
        # elif not process2.is_alive():
        #     process2 = Process(target=process_2)
        #     process2.start()
        #     # process2.join()
        # elif not process3.is_alive():
        #     process3 = Process(target=process_3)
        #     process3.start()
        #     # process3.join()
        # elif not process4.is_alive():
        #     process4 = Process(target=process_4)
        #     process4.start()
        #     # process4.join()
        # elif not process5.is_alive():
        #     process5 = Process(target=process_5)
        #     process5.start()
        #     # process5.join()
        # elif not process6.is_alive():
        #     process6 = Process(target=process_6)
        #     process6.start()
        #     # process6.join()
        # elif not process7.is_alive():
        #     process7 = Process(target=process_7)
        #     process7.start()
        #     # process7.join()
        elif not process8.is_alive():
            process8 = Process(target=process_8)
            process8.start()
            # process7.join()