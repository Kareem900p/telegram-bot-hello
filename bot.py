import telebot

TOKEN = "7670537680:AAELSBOQ_ujjuyLa4UzjqL9VXBJjTYWAfc0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    username = message.from_user.first_name or "User"
    bot.send_message(message.chat.id, f"Hello {username}")

bot.polling()