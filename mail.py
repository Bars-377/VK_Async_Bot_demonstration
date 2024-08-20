# import threading

def treatment_p(id, fio, contacts,type_service, service, date, category):

    if category == None:
        category = ''

    from docx import Document
    from docx.shared import Pt
    from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

    # Создайте новый документ
    doc = Document()

    # Функция для добавления текста по центру
    def add_centered_text(doc, text, bold=False, font_size=12):
        paragraph = doc.add_paragraph()
        run = paragraph.add_run(text)
        run.bold = bold
        run.font.size = Pt(font_size)
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Первая строка
    add_centered_text(doc, "ЗАЯВКА № ______", bold=True, font_size=14)

    date = str(date).split('-')

    # # Получение даты
    # date_str = date.strftime("от «%d»_%m_%Y г.")

    # Вторая строка
    add_centered_text(doc, f'от {date[2]}_{date[1]}_{date[0]} г.', font_size=12)

    # Третья строка
    add_centered_text(doc, "на оказание услуги по выездному обслуживанию заявителей", font_size=12)

    # Добавление таблицы
    table = doc.add_table(rows=6, cols=2)
    table.style = 'Table Grid'

    # Первая строка таблицы
    cell = table.cell(0, 0)
    cell.merge(table.cell(0, 1))
    cell_paragraph = cell.paragraphs[0]
    cell_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = cell_paragraph.add_run("Сведения о заказчике")
    run.bold = True

    # Вторая строка таблицы
    table.cell(1, 0).text = "Фамилия Имя Отчество/ Наименование заказчика"

    # Вторая строка таблицы
    table.cell(1, 1).text = fio

    # Третья строка таблицы
    table.cell(2, 0).text = "Контактный телефон/ адрес проживания заказчика адрес электронной почты"

    # Третья строка таблицы
    table.cell(2, 1).text = contacts

    # Четвёртая строка таблицы
    table.cell(3, 0).text = "Наименование категории граждан, для которых организация выезда через МФЦ осуществляется бесплатно*"

    # Четвёртая строка таблицы
    table.cell(3, 1).text = category

    # Пятая строка таблицы
    table.cell(4, 0).text = "Вид услуги"
    if type_service == '1':
        table.cell(4, 1).text = "Выезд к заявителю с целью:\n⩗ приёма документов\n□ доставки документов"
    else:
        table.cell(4, 1).text = "Выезд к заявителю с целью:\n□ приёма документов\n⩗ доставки документов"

    # Шестая строка таблицы
    table.cell(5, 0).text = "Наименование услуги"

    # Шестая строка таблицы
    table.cell(5, 1).text = service

    # После таблицы
    doc.add_paragraph()
    add_centered_text(doc, "Заявку принял: __________(подпись) / __________(ФИО специалиста)", font_size=12)

    # Последняя строка справа
    paragraph = doc.add_paragraph("* - заполняется при выездном обслуживании льготных категорий граждан")
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    # Сохраните документ
    modified_attachment_path = "C:\\Users\\admin\\Desktop\\mail\\zayavka_" + str(id) + ".docx"

    doc.save(modified_attachment_path)

    print("Документ успешно создан и сохранён.")

    import smtplib
    from email.message import EmailMessage
    import time
    import os

    # Заполните эти переменные значениями для своего почтового сервера и учетной записи отправителя
    smtp_server = "smtp.mfc.tomsk.ru"
    # smtp_server = "smtp.yandex.ru"
    smtp_port = 587  # Порт для TLS
    sender_email_address = "neverov@mfc.tomsk.ru"
    sender_password = "85HtnPdj"  # Убедитесь, что это пароль приложения
    # sender_email_address = "m.tosp@yandex.ru"
    # sender_password = "cwlecvijmxlpkvfo"  # Убедитесь, что это пароль приложения

    # Создайте сообщение электронной почты
    message = EmailMessage()
    message["Subject"] = f"Заявка на платную услугу от {fio}"
    message["From"] = sender_email_address
    message["To"] = 'msptosp@mfc.tomsk.ru'  # Адрес получателя

    # Установите текстовое содержимое письма
    message.set_content(f"Заявка на платную у слугу от {fio}")

    # Прикрепите файл Excel к письму
    attachment_path = "C:\\Users\\admin\\Desktop\\mail\\zayavka_" + str(id) + ".docx"
    with open(attachment_path, "rb") as attachment:
        message.add_attachment(attachment.read(), maintype="application", subtype="vnd.openxmlformats-officedocument.wordprocessingml.document", filename=os.path.basename(attachment_path))

    # Функция для отправки письма
    def send_email():
        condition = False
        try:
            # Подключитесь к SMTP-серверу
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Инициализация TLS
                server.login(sender_email_address, sender_password)
                server.send_message(message)  # Отправьте сообщение
            print("Письмо успешно отправлено.")

            # Удалите документ
            os.remove(modified_attachment_path)

            condition = True
        except smtplib.SMTPAuthenticationError as e:
            print(f"Ошибка аутентификации mail: {e}")
        except Exception as e:
            print(f"Произошла ошибка mail: {e}")

        return condition

    # Попробуйте отправить письмо несколько раз с интервалами
    attempts = 3
    for attempt in range(attempts):
        print(f"Попытка {attempt + 1} из {attempts}")

        condition = send_email()
        if condition:
            break
        elif attempt < attempts - 1:
            print("Ожидание перед повторной попыткой...")
            time.sleep(10)  # Ожидание 10 секунд перед следующей попыткой

    return

import mysql.connector

photo_id = ''

def process_mail():
    global photo_id

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
            update_query = "SELECT * FROM application;"
            cursor.execute(update_query)
            data = cursor.fetchall()

            for row in data:
                treatment_p(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                update_query = f"DELETE FROM application WHERE id = {row[0]};"
                cursor.execute(update_query)

            connection.commit()  # Фиксация транзакции

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

# if __name__ == "__main__":

#     # создание и запуск потоков для каждого процесса
#     t1 = threading.Thread(target=process_mail)

#     while True:
#         if not t1.is_alive():
#             t1 = threading.Thread(target=process_mail)
#             t1.start()
