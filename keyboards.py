from vkbottle import Keyboard, KeyboardButtonColor, Text

from base import *

class buttons:
    async def filials(*args):
        try:
            try:
                arg = (args,)[0][0]
            except:
                arg = ''
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Город Томск", {"cmd": "tomsk"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Районы Томской области", {"cmd": "tomsk_obl"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            if not arg == '12345':
                keyboard.add(Text("Томский район", {"cmd": "tomsk_rayon"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            if arg == '12345':
                keyboard.add(Text("Северск", {"cmd": "seversk"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def application_service(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Приём документов", {"cmd": "application_service_1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Доставка документов", {"cmd": "application_service_2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def services_section(department):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            if not department == '12345':
                keyboard.add(Text("Получение готовых документов", {"cmd": "dokum"}),color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            if (
                department != "557"
                and department != "389"
                and department != "449"
                and department != "449"
                and department != "677"
                and department != "371"
                and department != "683"
                and department != "342595"
            ):
                keyboard.add(Text("Социальная сфера", {"cmd": "soc_sphere"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                if not department == '12345':
                    keyboard.add(Text("Водительское удостоверен.", {"cmd": "udost"}), color=KeyboardButtonColor.POSITIVE)
                    keyboard.row()
            keyboard.add(Text("Недвижимость", {"cmd": "nedvij"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Платные услуги", {"cmd": "plant_usl"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            if department == "431" or department == "533":
                keyboard.add(Text("Консультация специалиста", {"cmd": "konsul"}),color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("Другие услуги", {"cmd": "drug_usl"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            if (department == "461"):
                keyboard.add(Text("Консультация юриста по цифровой среде", {"cmd": "digital"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.row()
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()


    async def services_property(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Регистрация и кадастр", {"cmd": "registr"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Сведения из ЕГРН", {"cmd": "sved"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Прекращение, приостановка", {"cmd": "prekr"}),color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Разрешение на сделку", {"cmd": "opeka"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Крупные сделки", {"cmd": "krupn"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.row()
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def services_consultation(department):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            if department != "431":
                keyboard.add(Text("спец. Роспотребнадзора", {"cmd": "kons_rosp"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("спец. Росреестра", {"cmd": "kons_rosres"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("спец. с Нотариусом", {"cmd": "notar"}),color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.row()
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def services_paid(department):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Налоговые декларации", {"cmd": "deklar"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Составление договоров", {"cmd": "dogov"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            if (
                department == "557"
                or department == "389"
                or department == "449"
                or department == "449"
                or department == "677"
                or department == "371"
                or department == "683"
                or department == "342595"
            ):
                keyboard.add(Text("Банкротство ФЛ", {"cmd": "bankr"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.row()
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def services_social(*args):
        try:
            arg = (args,)[0][0]
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Паспорт", {"cmd": "passport"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Прописка", {"cmd": "residency"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("ИНН, СНИЛС, ОМС", {"cmd": "snils"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Субсидии, льготы, пенсии", {"cmd": "lgot"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Справки УМВД и СФР", {"cmd": "sprav"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Распоряжение мат. кап.", {"cmd": "smk"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            if not arg == '12345':
                keyboard.add(Text("Загранпаспорт", {"cmd": "zagran"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            if arg == '12345':
                keyboard.add(Text("Загранпаспорт (5 лет)", {"cmd": "zagran_5"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            if arg == '12345':
                keyboard.add(Text("Детские пособия, путёвки", {'cmd': 'posob'}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            # keyboard.add(Text("Ежемес. выпл. на ребёнка", {'cmd': 'viplata'}), color=KeyboardButtonColor.POSITIVE)
            # keyboard.row()
            keyboard.add(Text("Газификация", {"cmd": "gazif"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.row()
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def services_other(department):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Портал Госуслуги", {"cmd": "gosusl"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            if not department == '12345':
                keyboard.add(Text("Услуги ИП", {"cmd": "predprin"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            if (
                department != "557"
                and department != "389"
                and department != "449"
                and department != "449"
                and department != "677"
                and department != "371"
                and department != "683"
                and department != "342595"
            ):
                keyboard.add(Text("Банкротство ФЛ", {"cmd": "bankr"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_1"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.row()
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def times_buttons(date, time, department, service, fields_s):
        try:
            times = await base().base_get_date_and_time(date, time, department, service, fields_s, True)

            keyboard = Keyboard(one_time=True, inline=False)
            counter = 0
            conditions = [True] * 12

            if isinstance(times, tuple) and not times[1].get('success', True):
                # Обработка ошибки сервера
                print(f"Ошибка: {times[1].get('message', 'Неизвестная ошибка')}")

            print('ВЫВОД ВРЕМЕН В ФУНКЦИИ times_buttons', times[1]["data"])

            if not times[1]["data"]:
                keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
                keyboard = keyboard.get_json()
                return keyboard

            row = False

            for i in times[1]["data"]:
                t = str(i).split(":")
                st = t[0] + t[1]

                for idx in range(12):
                    if (
                        int(st) >= (800 + idx * 100)
                        and int(st) <= (850 + idx * 100)
                        and conditions[idx]
                    ):
                        keyboard.add(
                            Text(
                                f"с {8+idx:02}:00 до {8+idx:02}:50",
                                {"cmd": f"{800+idx*100}"},
                            ),
                            color=KeyboardButtonColor.POSITIVE)
                        counter += 1
                        conditions[idx] = False

                        row = False

                        if counter % 2 == 0:
                            keyboard.row()
                            row = True

            if not row:
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_1"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.row()
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)

            keyboard = keyboard.get_json()
            return keyboard, times
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def tomsk(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Кировский", {"cmd": "frunze"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Ленинский", {"cmd": "derb"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Октябрьский", {"cmd": "pushk"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Советский", {"cmd": "tvers"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Академгородок", {"cmd": "razv"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("ЦОУ для бизнеса", {"cmd": "mfc_business"}),color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_1"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def tomsk_obl(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Асиновский", {"cmd": "asino"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Кедровый", {"cmd": "cedar"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Стрежевой", {"cmd": "strez"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("ЗАТО Северск", {"cmd": "zato"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Зырянский", {"cmd": "ziryansk"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Парабельский", {"cmd": "parabel"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Другой", {"cmd": "tomsk_obl_1"}), color=KeyboardButtonColor.PRIMARY)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_1"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def tomsk_rayon(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("д. Воронино", {"cmd": "voronino"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("д. Кисловска", {"cmd": "kislovka"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("пос. Зональная станция", {"cmd": "zonaln"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("пос. Мирный", {"cmd": "peaceful"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("пос. Рассвет", {"cmd": "dawn"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Богашево", {"cmd": "bogashevo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Вершинино", {"cmd": "vershinino"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Зоркальцево", {"cmd": "zork"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Итатка", {"cmd": "itatka"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Калтай", {"cmd": "kaltay"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Другой", {"cmd": "tomsk_rayon_1"}), color=KeyboardButtonColor.PRIMARY)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_1"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def tomsk_rayon_1(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("с. Корнилово", {"cmd": "kornilovo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Малиновка", {"cmd": "robin"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Межениновка", {"cmd": "mejen"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Новорождественское", {"cmd": "novoroj"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Рыболово", {"cmd": "rybalovo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Моряковский затон", {"cmd": "moryak_zaton"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Турунтаево", {"cmd": "turuntayevo_selo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Октябрьское", {"cmd": "october"}), color=KeyboardButtonColor.POSITIVE,)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_13"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def kojev_rayon(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("с. Вороново", {"cmd": "voronovo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Кожевниково", {"cmd": "kojevn"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Малиновка", {"cmd": "malin"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Новопокровка", {"cmd": "novopokrovka"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Песочнодубровка", {"cmd": "pesochno"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Старая Ювала", {"cmd": "old_yuvala"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Уртам", {"cmd": "urtam"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Чилино", {"cmd": "chilino"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def krivosh_rayon(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("с. Володино", {"cmd": "volodino"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Красный Яр", {"cmd": "red_yar"}), color=KeyboardButtonColor.POSITIVE,)
            keyboard.row()
            keyboard.add(Text("с. Кривошеино", {"cmd": "krivosheino"}), color=KeyboardButtonColor.POSITIVE,)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def kolp_rayon(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("г. Колпашево", {"cmd": "kolpashevo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("п. Большая Саровка", {"cmd": "bolsh_sar"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Новоселово", {"cmd": "novoselovo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Чажемто", {"cmd": "chazhemto"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def molch_rayon(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("с. Могочино", {"cmd": "mogochino"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Молчаново", {"cmd": "molchanovo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Нарга", {"cmd": "narga"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Тунгусово", {"cmd": "tungusovo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def pervom_rayon(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Первомайский", {"cmd": "pervomaiskoye"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Сергеево", {"cmd": "serg"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("п. Орехово", {"cmd": "oreh"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("п. Улу-Юл", {"cmd": "ulu"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Комсомольск", {"cmd": "komsom"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def tomsk_obl_1(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Верхнекетский", {"cmd": "balyar"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Александровский", {"cmd": "alex"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Тегульдетский", {"cmd": "teguld"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Чаинский", {"cmd": "chain"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Другое", {"cmd": "tomsk_obl_2"}), color=KeyboardButtonColor.PRIMARY)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_5"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def tomsk_obl_2(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Первомайский", {"cmd": "pervom_rayon"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Кожевниковский", {"cmd": "kojev_rayon"}),color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Кривошеинский", {"cmd": "krivosh_rayon"}),color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Колпашевский", {"cmd": "kolp_rayon"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Молчановский", {"cmd": "molch_rayon"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Шегарский", {"cmd": "shegar_rayon"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def shegar_rayon(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("с. Анастасьевка", {"cmd": "anast"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Баткат", {"cmd": "butkat"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("с. Мельниково", {"cmd": "meln"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Монастырка", {"cmd": "monastery"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("п. Победа", {"cmd": "victory"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("с. Трубачево", {"cmd": "trubachevo"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def mfc_business(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            # keyboard.add(Text('"Уралсиб банк"', {'cmd': 'frunze_11a'}), color=KeyboardButtonColor.POSITIVE)
            # keyboard.add(Text('"Томскпромстрой"', {"cmd": "frunze_90"}), color=KeyboardButtonColor.POSITIVE)
            # keyboard.add(Text('"Левобережный"', {"cmd": "sovp"}), color=KeyboardButtonColor.POSITIVE)
            # keyboard.add(Text('"ФК Открытие"', {"cmd": "naber"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text('"Дом предпринимателя"', {"cmd": "dom_predpr"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text('"Промсвязьбанк"', {"cmd": "lenin_ave"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text('"Газпромбанк"', {"cmd": "gaspr"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_3"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def params_1(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("1", {"cmd": "1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("2", {"cmd": "2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("3", {"cmd": "3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("4", {"cmd": "4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("5", {"cmd": "5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def reception(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("5 (очень легко)", {"cmd": "5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("4 (легко)", {"cmd": "4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("3 (удовлетворительно)", {"cmd": "3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("2 (сложно)", {"cmd": "2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("1 (очень сложно)", {"cmd": "1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def reception_1(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("5 (очень быстро)", {"cmd": "5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("4 (быстро)", {"cmd": "4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("3 (нормально)", {"cmd": "3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("2 (медленно)", {"cmd": "2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("1 (очень медленно)", {"cmd": "1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def reception_2(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("5 (очень вежливый)", {"cmd": "5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("4 (вежливый)", {"cmd": "4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("3 (не очень вежливый)", {"cmd": "3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("2 (не вежливый)", {"cmd": "2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("1 (возник конфликт)", {"cmd": "1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def waiting_time(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("5 (менее 10 минут)", {"cmd": "5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("4 (10-15 минут)", {"cmd": "4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("3 (16 - 18 минут)", {"cmd": "3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("2 (18 - 25 минут)", {"cmd": "2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("1 (более 26 минут)", {"cmd": "1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def params_2(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("1", {"cmd": "1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("2", {"cmd": "2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("3", {"cmd": "3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("4", {"cmd": "4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("5", {"cmd": "5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("6", {"cmd": "6"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("7", {"cmd": "7"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("8", {"cmd": "8"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("9", {"cmd": "9"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("10", {"cmd": "10"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def yes_no(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Да", {"cmd": "yes"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Нет", {"cmd": "no"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def yes_no_doc(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Ознакомиться с перечнем документов", {"cmd": "yes"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Не интересно", {"cmd": "no"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def agreement_yes_no(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Согласен", {"cmd": "yes"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.add(Text("Не согласен", {"cmd": "no"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def send(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Отправить пожелания!", {"cmd": "yes"}), color=KeyboardButtonColor.POSITIVE)
            # keyboard.add(Text("Календарь событий", {"cmd": "events"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def fio_yes(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Фамилия Имя профиля", {"cmd": "yes_fi"}),color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def delete_coupon(uuid, talon, department, date, tel, fio):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Удалить запись", {"cmd": f"delete_coupons_{uuid}_{talon}_{department}_{date}_{tel}_{fio}"}),color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("Я приду", {"cmd": "accept_entry"}), color=KeyboardButtonColor.POSITIVE)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def menu(*args):
        try:
            keyboard = {
                "one_time": True,
                "buttons": [
                    # [
                    #     {
                    #         "action": {
                    #             "type": "text",
                    #             "label": "*ЮБИЛЕЙ ТОМСКОЙ ОБЛАСТИ*",
                    #             "payload": "{\"cmd\": \"anniversary\"}"
                    #         },
                    #         "color": "negative"
                    #     }
                    # ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Записаться на приём",
                                "payload": "{\"cmd\": \"filials\"}"
                            },
                            "color": "positive"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Уточнить информацию по вашей записи",
                                "payload": "{\"cmd\": \"information_coupons\"}"
                            },
                            "color": "primary"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Проверить статус заявления",
                                "payload": "{\"cmd\": \"status\"}"
                            },
                            "color": "primary"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Адрес и график работы отделов МФЦ",
                                "payload": "{\"cmd\": \"information_mfc\"}"
                            },
                            "color": "primary"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Проконсультировать по услугам МФЦ",
                                "payload": "{\"cmd\": \"consultation\"}"
                            },
                            "color": "primary"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Удалить запись в МФЦ",
                                "payload": "{\"cmd\": \"delete_coupons\"}"
                            },
                            "color": "primary"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Выездное обслуживание",
                                "payload": "{\"cmd\": \"application\"}"
                            },
                            "color": "primary"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "text",
                                "label": "Оценка получения услуги",
                                "payload": "{\"cmd\": \"grade\"}"
                            },
                            "color": "primary"
                        }
                    ],
                    [
                        {
                            "action": {
                                "type": "open_link",
                                "label": "Связаться со специалистом",
                                "link": "https://vk.com/im?media=&sel=-211348794"
                            }
                        }
                    ]
                ]
            }

            import time
            import requests

            # Токен доступа к VK API
            access_token = (args,)[0][1]

            # Данные для отправки сообщения
            peer_id = (args,)[0][0] # ID пользователя, которому отправляем сообщение
            message = 'Добро пожаловать!'

            # Функция для генерации "случайных" чисел без использования модуля random
            def custom_random():
                current_time = time.time()
                seed = int((current_time - int(current_time)) * 10**6)  # Используем миллионные доли секунды в качестве зерна для "случайности"
                next_number = (1103515245 * seed + 12345) % 2**31  # Простой линейный конгруэнтный генератор
                return next_number

            # Отправка сообщения с клавиатурой
            payload = {
                'access_token': access_token,
                'peer_id': peer_id,
                'message': message,
                'keyboard': json.dumps(keyboard),
                'random_id': custom_random(),
                'v': '5.199'  # Добавляем версию API
            }

            requests.post('https://api.vk.com/method/messages.send', params=payload)

            return

        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def events(location):
        try:
            # dates = await base().base_get_events_dates(location)

            dates = await base().base_get_events_dates('tomsk')

            # dates_1 = await base().base_get_events_dates('tomsk')
            # dates_2 = await base().base_get_events_dates('severs')
            # dates_3 = await base().base_get_events_dates('tomsk_obl')

            # dates = [item for sublist in zip(dates_1, dates_2, dates_3) for item in sublist]

            keyboard = Keyboard(one_time=True, inline=False)
            counter = 0

            if not dates == []:
                for date in dates:
                    keyboard.add(Text(f"{date}", {"cmd": f"{date}"}), color=KeyboardButtonColor.POSITIVE)
                    counter += 1
                    row = False

                    if counter % 2 == 0:
                        keyboard.row()
                        row = True

                if not row:
                    keyboard.row()

            keyboard.add(Text("Назад", {"cmd": "back_1"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)

            keyboard = keyboard.get_json()
            return keyboard

        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def consultation(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Услуги МВД / ГИБДД", {"cmd": "cons_mvd"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("СНИЛС, ИНН, ОМС", {"cmd": "cons_snils_inn_oms"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("ЗАГС", {"cmd": "cons_zags"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Удостоверение многодетной семьи", {"cmd": "cons_mnog"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назначение пенсии", {"cmd": "cons_pens"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Сертификат на газификацию", {"cmd": "cons_sert"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Оформление единого пособия", {"cmd": "cons_edin"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Направление ребёнка в детский сад", {"cmd": "cons_detsk"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Далее", {"cmd": "cons_other"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def consultation_mvd(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Паспорт Гражданина РФ", {"cmd": "cons_pasp"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Регистрационный учёт граждан", {"cmd": "cons_reg"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Справка из ИЦ УМВД", {"cmd": "cons_sprav"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Заграничный паспорт", {"cmd": "cons_zagr"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Водительское удостоверение", {"cmd": "cons_vod"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_5"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def consultation_snils_inn_oms(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("СНИЛС", {"cmd": "cons_snils"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("ИНН", {"cmd": "cons_inn"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Полис (ОМС)", {"cmd": "cons_polis"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_5"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def consultation_zags(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Регистрация/расторжение брака", {"cmd": "cons_brak"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Свидетельство о рождении ребёнка", {"cmd": "cons_rojd"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_5"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def cons_zagr(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Срок действия 5 лет", {"cmd": "cons_zagr_5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Срок действия 10 лет", {"cmd": "cons_zagr_10"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def cons_zagr_5_10(condition):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            if condition:
                keyboard.add(Text("С 14 до 18 лет", {"cmd": "cons_zagr_14_18"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                keyboard.add(Text("До 14 лет", {"cmd": "cons_zagr_14"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                keyboard.add(Text("С 18 лет", {"cmd": "cons_zagr_18"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            else:
                keyboard.add(Text("С 14 до 18 лет", {"cmd": "cons_zagr_14_18_10"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                keyboard.add(Text("До 14 лет", {"cmd": "cons_zagr_14_10"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                keyboard.add(Text("С 18 лет", {"cmd": "cons_zagr_18_10"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_5"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def cons_pasp(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Исполнилось 14 лет", {"cmd": "cons_pasp_14"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Исполнилось 20 или 45 лет", {"cmd": "cons_pasp_20"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Изменение внешности", {"cmd": "cons_pasp_vnesh"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Обнаружение неточности/опечатки", {"cmd": "cons_pasp_netoch"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Непригодность или износ", {"cmd": "cons_pasp_povrej"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Внесение изменений в запись акта", {"cmd": "cons_pasp_akt"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Смена ФИО", {"cmd": "cons_pasp_data"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_6"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def consultation_reg_brak(condition):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            if condition:
                keyboard.add(Text("Регистрация гражданина РФ", {"cmd": "cons_grajd_1"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                keyboard.add(Text("Снятие с регистрационного учёта", {"cmd": "cons_snyat_1"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            else:
                keyboard.add(Text("Регистрация брака", {"cmd": "cons_grajd_2"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
                keyboard.add(Text("Расторжение брака", {"cmd": "cons_snyat_2"}), color=KeyboardButtonColor.POSITIVE)
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_7"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def consultation_other(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Выписка из ЕГРН", {"cmd": "cons_vipiska"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Услуги для предпринимателей", {"cmd": "cons_predpr"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Портал Госуслуги.ру", {"cmd": "cons_port"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Лицензия на такси", {"cmd": "cons_lic"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back_5"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def menu_menu(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def menu_menu_file(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Отказаться", {"cmd": "no_no"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def grade(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Отправить без комментария", {"cmd": "1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def application(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Платный выезд", {"cmd": "application_1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Бесплатный выезд", {"cmd": "application_2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def application_approaching(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Подхожу под категорию", {"cmd": "application_3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def application_send(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Отправить заявку", {"cmd": "application_4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def application_1(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Ветеран ВОВ", {"cmd": "1_1"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Инвалид 1 группы", {"cmd": "2_2"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Инвалид 2 группы", {"cmd": "3_3"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Герой РФ", {"cmd": "4_4"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Инвалид боевых действий", {"cmd": "5_5"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Родитель ребёнка-инвалида", {"cmd": "6_6"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Возраст более 80 лет", {"cmd": "7_7"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def button_review(*args):
        try:
            keyboard = Keyboard(one_time=True, inline=False)
            keyboard.add(Text("Оценить качество предоставленной услуги", {"cmd": "button_review"}), color=KeyboardButtonColor.POSITIVE)
            keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
            keyboard = keyboard.get_json()
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def date_1(date, time, department, service, fields_s):
        try:
            dates = await base().base_get_date_and_time(date, time, department, service, fields_s, True)
            keyboard = Keyboard(one_time=True, inline=False)

            if isinstance(dates, tuple) and not dates[0].get('success', True):
                # Обработка ошибки сервера
                print(f"Ошибка: {dates[0].get('message', 'Неизвестная ошибка')}")

            print('ПОСЛЕ ВХОДА В ФУНКЦИЮ date_1:', dates)

            if not dates[0]["data"]:
                keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
                keyboard = keyboard.get_json()
                return keyboard

            counter = 0
            for i in dates[0]["data"]:
                keyboard.add(Text(str(i), {"cmd": str(i)}), color=KeyboardButtonColor.POSITIVE)
                counter += 1
                if counter % 2 == 0:
                    keyboard.row()

                if counter == 5:
                    keyboard.row()
                    keyboard.add(Text("Остальные даты", {"cmd": "date_ost"}), color=KeyboardButtonColor.POSITIVE)
                    keyboard.row()
                    break

            # Преобразуем клавиатуру в JSON
            keyboard_json = keyboard.get_json()

            # Парсим JSON
            keyboard_data = json.loads(keyboard_json)

            # Проверка наличия кнопок и непустой последней строки
            buttons = keyboard_data['buttons']
            has_buttons = any(bool(row) for row in buttons)  # Проверка наличия хотя бы одной строки с кнопками
            last_row = buttons[-1] if buttons else None  # Получаем последнюю строку

            if has_buttons and any(bool(button) for button in last_row) and len(dates[0]["data"]) < 4:
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)

            keyboard = keyboard.get_json()
            print('ПОЛУЧИВШАЯСЯ КЛАВИАТУРА В ФУНКЦИИ date_1', keyboard)
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def date_2(date, time, department, service, fields_s):
        try:
            dates = await base().base_get_date_and_time(date, time, department, service, fields_s, False)
            keyboard = Keyboard(one_time=True, inline=False)

            if isinstance(dates, tuple) and not dates[0].get('success', True):
                # Обработка ошибки сервера
                print(f"Ошибка: {dates[0].get('message', 'Неизвестная ошибка')}")

            print('ПОСЛЕ ВХОДА В ФУНКЦИЮ date_2:', dates)

            if not dates[0]["data"]:
                keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
                keyboard = keyboard.get_json()
                return keyboard

            row = False

            counter = 0
            for i in dates[0]["data"][5:]:
                keyboard.add(Text(str(i), {"cmd": str(i)}), color=KeyboardButtonColor.POSITIVE)
                counter += 1
                row = False
                if counter % 2 == 0:
                    keyboard.row()
                    row = True

            # Преобразуем клавиатуру в JSON
            keyboard_json = keyboard.get_json()

            # Парсим JSON
            keyboard_data = json.loads(keyboard_json)

            # Проверка наличия кнопок и непустой последней строки
            buttons = keyboard_data['buttons']
            has_buttons = any(bool(row) for row in buttons)  # Проверка наличия хотя бы одной строки с кнопками
            last_row = buttons[-1] if buttons else None  # Получаем последнюю строку

            if has_buttons and any(bool(button) for button in last_row) and not row:
                keyboard.row()
            keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)

            keyboard = keyboard.get_json()
            print('ПОЛУЧИВШАЯСЯ КЛАВИАТУРА В ФУНКЦИИ date_2', keyboard)
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def times(times_s, a, b):
        try:

            keyboard = Keyboard(one_time=True, inline=False)

            if isinstance(times_s, tuple) and not times_s[1].get('success', True):
                # Обработка ошибки сервера
                print(f"Ошибка: {times_s[1].get('message', 'Неизвестная ошибка')}")

            print('ПОСЛЕ ВХОДА В ФУНКЦИЮ times:', times_s[1]["data"])

            if not times_s[1]["data"]:
                keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)
                keyboard = keyboard.get_json()
                return keyboard

            row = False
            counter = 0

            for i in times_s[1]["data"]:
                t = str(i).split(":")
                st = t[0] + t[1]
                if a < int(st) < b:
                    keyboard.add(Text(str(i), {"cmd": str(i)}), color=KeyboardButtonColor.POSITIVE)
                    counter += 1
                    row = False

                    if counter % 2 == 0:
                        keyboard.row()
                        row = True

                    if counter == 6:
                        if not row:
                            keyboard.row()
                        # if not button == '':
                        #     keyboard.add(Text("Остальное время", {"cmd": button}), color=KeyboardButtonColor.POSITIVE)
                        # keyboard.row()
                        keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
                        break

            # Преобразуем клавиатуру в JSON
            keyboard_json = keyboard.get_json()

            # Парсим JSON
            keyboard_data = json.loads(keyboard_json)

            # Проверка наличия кнопок и непустой последней строки
            buttons = keyboard_data['buttons']
            has_buttons = any(bool(row) for row in buttons)  # Проверка наличия хотя бы одной строки с кнопками
            last_row = buttons[-1] if buttons else None  # Получаем последнюю строку

            if counter < 6:
                if has_buttons and any(bool(button) for button in last_row) and not row:
                    keyboard.row()
                # if not button == '':
                #     keyboard.add(Text("Остальное время", {"cmd": button}), color=KeyboardButtonColor.POSITIVE)
                # keyboard.row()
                keyboard.add(Text("Назад", {"cmd": "back"}), color=KeyboardButtonColor.NEGATIVE)
            keyboard.add(Text("В главное меню", {"cmd": "menu"}), color=KeyboardButtonColor.PRIMARY)

            keyboard = keyboard.get_json()
            print('ПОЛУЧИВШАЯСЯ КЛАВИАТУРА В ФУНКЦИИ times', keyboard)
            return keyboard
        except Exception as e:
            # Вывод подробной информации об ошибке
            print(f"Поймано исключение: {type(e).__name__}")
            print(f"Сообщение об ошибке: {str(e)}")
            import traceback
            print("Трассировка стека (stack trace):")
            traceback.print_exc()

    async def time_1(times_s):
        a = 750
        b = 900
        # button = 'time_ost_2'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_2(times_s):
        a = 850
        b = 1000
        # button = 'time_ost_3'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_3(times_s):
        a = 950
        b = 1100
        # button = 'time_ost_4'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_4(times_s):
        a = 1050
        b = 1200
        # button = 'time_ost_5'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_5(times_s):
        a = 1150
        b = 1300
        # button = 'time_ost_6'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_6(times_s):
        a = 1250
        b = 1400
        # button = 'time_ost_7'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_7(times_s):
        a = 1350
        b = 1500
        # button = 'time_ost_8'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_8(times_s):
        a = 1450
        b = 1600
        # button = 'time_ost_9'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_9(times_s):
        a = 1550
        b = 1700
        # button = 'time_ost_10'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_10(times_s):
        a = 1650
        b = 1800
        # button = 'time_ost_11'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_11(times_s):
        a = 1750
        b = 1900
        # button = 'time_ost_12'
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)

    async def time_12(times_s):
        a = 1850
        b = 2000
        # button = ''
        # return await buttons.times(times_s, a, b, button)
        return await buttons.times(times_s, a, b)