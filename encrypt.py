import telebot #Import the library

TOKEN = '454542876:AAEs9MY9NbZ9XQxoz0nLU4PVBdlFxWO84U0' #This is our token
started, encryptState, decryptState = False

my_bot = telebot.TeleBot(TOKEN) #Create the bot

def encrypt(self, message):
    return "Encrypt"

def decrypt(self, message):
    return "Decrypt"

def start(self, message):
    chat_id = message.chat.id #Take the id of the chat
    if message is "/start":
        my_bot.send_message(chat_id, "OK, you can choose /encrypt or /decrypt")
        started = True
        encryptState = False
        decryptState = False
    else:
        my_bot.send_message(chat_id, "You have to start sending me /start")
        started = False

def options(self, message, started):
    chat_id = message.chat.id  # Take the id of the chat
    if started is False:
        my_bot.send_message(chat_id, "You have not started yet")
    else:
        if message is "/encrypt":
            my_bot.send_message(chat_id, "OK, you can send me the message to encrypt")
            started = True
            encryptState = True
            decryptState = False
        elif message is "/decrypt":
            my_bot.send_message(chat_id, "OK, you can send me the message to decrypt")
            started = True
            encryptState = False
            decryptState = True
        elif message is "/end":
            my_bot.send_message(chat_id, "OK, I send me /start to start again")

def encryptDecryptOption(self, message):
    chat_id = message.chat.id  # Take the id of the chat
    if started is True and encryptState is True:
        encryptedMessage = encrypt(message)
        my_bot.send_message(chat_id, "OK,this is your encrypted text \n" + encryptedMessage)
    elif started is True and decryptState is True:
        decryptedMessage = decrypt(message)
        my_bot.send_message(chat_id, "OK,this is the decrypted text \n" + decryptedMessage)

my_bot.set_update_listener(start)
my_bot.polling()