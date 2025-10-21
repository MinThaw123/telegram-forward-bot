from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

SOURCE_CHAT_ID = -1002552081327  # your source group ID
TARGET_CHAT_ID = -4905986347  # your destination group ID
BOT_TOKEN = "8288899511:AAER7Yfcc_HfiTwjd0WgNBNzs4oNtRTQ4a4"

async def forward_photos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == SOURCE_CHAT_ID and update.message.photo:
        await context.bot.forward_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=SOURCE_CHAT_ID,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, forward_photos))
app.run_polling()
