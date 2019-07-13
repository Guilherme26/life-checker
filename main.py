from bot import update_status, life_check
from telegram.ext import Updater, CommandHandler
from credentials import credentials


def main():
    updater = Updater(credentials['token'])

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('status', update_status))
    dispatcher.add_handler(CommandHandler('check', life_check))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
