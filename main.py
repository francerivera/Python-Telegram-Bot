from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6644143306:AAGTHrXLYN09hgck0Yf0Jn4-gBdHUzJ2E_Q'
BOT_USERNAME: Final = '@PransAmbot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Si Idol pala to e!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Anong hanap mo lods?")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Try mo pre!")

#Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "yow wassup lods!"
    if "bai na bai" in processed:
        "bisakol ka no?"
    if "nigga" in processed:
        return "bad yan lods bawal racist dito"
    if "nigger" in processed:
        return "bawal racist dito ang kulet!"
    if "black" in processed:
        return 'black favorite color mo?'
    if "tite" in processed:
        return 'Sabi ko na nga ba yan una mong sasabihin e!'
    if "tanginamo" in processed:
        return 'tanginamo rin!'
    if "pakyu" in processed:
        return 'pakyu ka rin ulol gago ./.'
    return 'ano raw gagi di kita gets HSAHAHA'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause error {context.error}')



if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()


    # Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)





