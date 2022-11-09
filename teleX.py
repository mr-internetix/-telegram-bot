from telegram import *
from telegram.ext import *
bot = Bot("BOT ID HERE")
print(bot.get_me())

updater = Updater("BOT ID HERE",use_context=True)

dispatcher = updater.dispatcher

#custom commands
def test_function(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text="You can contact me here or @mr_internetix"
    )
start_value = CommandHandler('contact',test_function)
dispatcher.add_handler(start_value)



def test_function1(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id= update.effective_chat.id,
        text="Hello how are you ! welcome How can I help you ",
    )

start_value1 = CommandHandler('hello',test_function1)
dispatcher.add_handler(start_value1)

def test_function2(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id= update.effective_chat.id,
        text="https://www.youtube.com/watch?v=6yN-dYwRFuk ",
    )

start_value2 = CommandHandler('youtube',test_function2)
dispatcher.add_handler(start_value2)

#buttons

def test_funtion3(update:Update,context:CallbackContext):
    dict = {"Instagram": "www.intagram.com/mr_internetix", "Facebook": "www.facebook.com/elonmusk", "discord": "www.discord.gg/mr_internetix"}
    buttons = []
    for key, value in dict.items():
        buttons.append([InlineKeyboardButton(text = key, url = value)])
    keyboard = InlineKeyboardMarkup(buttons)
    bot.sendMessage(chat_id=update.effective_chat.id , text= 'These are the social Accounts', reply_markup = keyboard)
start_value3 = CommandHandler('socials',test_funtion3)
dispatcher.add_handler(start_value3)

updater.start_polling() 
