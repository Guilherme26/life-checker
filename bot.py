import email_functions as ef
from credentials import credentials


def update_status(bot, update):
    status = get_status()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=status)

def get_status():
    response = 'Se pá morreu em ...'
    if ef.is_alive():
        response = 'Morreu ainda não!'

    return response

def life_check(bot, update):
    ef.send_email()

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='Vamo ver se o Gustaveixon tá vivo! Para acompanhar o status ative o comando \'status\'')
