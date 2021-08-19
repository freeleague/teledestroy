import telebot
import time

print("teledestroy by ratabomb for tg @tg_inc_soft")

token = input("Введите токен: ")
tb = telebot.TeleBot(token=token)

print("Получаем информацию о боте...")
try:
	me = tb.get_me()
except:
	print("Токен недействительный!")
	exit()
print(f"Имя: {me.first_name}")
print(f"Ник: @{me.username}")
print(f"ID бота: {me.id}")
choice = str(input("Запустить спам с бота? (Y/N): "))
if choice == "Y" or choice == "y":
	userid = int(input("Введите user id человека, на которого будет идти спам: "))
	msgt = str(input("Введите сообщение для спама: "))
	times = int(input("Введите число, сколько раз будет отправлено это  сообщение (рекомендуем ставить не больше 200): "))
	print("Начинаем спам...")
	for i in range(times):
		try:
			tb.send_message(userid, msgt)
		except:
			print("Телеграм включил кд на запросы, включаем ожидание на 10 секунд...")
			time.sleep(10)
			tb.send_message(userid, msgt)
	print(f"Отправлено {str(times)} сообщений!")
choice = str(input("Подключить скрипт на отправку сообщения после написания /start? (Y/N): "))
if choice == "N" or choice == "n":
	exit()
msgt = str(input("Введите сообщение, которое будет отправляться: "))
print("Скрипт запущен! Чтобы остановить работу скрипта, нажмите CTRL+C.")

print("Ожидаем людей...")
@tb.message_handler(commands=["start"])
def sendmsg(message):
	tb.send_message(message.chat.id, msgt)
	print(f"@{message.chat.username} написал /start, сообщение отправлено!")

tb.polling(none_stop=True)
