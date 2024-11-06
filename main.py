import telebot as tele


Stud_Inside_bot = tele.TeleBot("7578462045:AAGkCRCnryHNER7hZq-d_PnQ-V8SwMk9GOM")

@Stud_Inside_bot.message_handler(func=lambda message: True ,content_types=['text', 'audio', 'video', 'voice', 'photo'])
def start(message):
    if message.text == '/start':
        Stud_Inside_bot.send_message(message.from_user.id, "Привет! Здесь ты можешь поделиться цитатами, фотками, видео, кружочками, сенсациями, мемами и новостями. А самое интересное, мы выложим в канал! 🫢")
    else:
        Stud_Inside_bot.send_message(message.from_user.id, "Твоё сообщение уже дошло до админов! Спасибо, что поделился!")
Stud_Inside_bot.polling(none_stop=True, interval=0)