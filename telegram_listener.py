
---

### **2️⃣ telegram_listener.py**

```python
import logging
from square_post import post_to_square
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import config

logging.basicConfig(level=logging.INFO)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    logging.info(f"📨 New Telegram message: {text}")
    
    # AI rewriting placeholder
    rewritten = f"{text}"  # Replace with AI rewrite logic if needed
    logging.info(f"✏️ AI Rewritten Post:\n {rewritten}")

    # Post to Binance Square
    post_url = post_to_square(rewritten)
    logging.info(f"✅ Posted successfully: {post_url}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    logging.info(f"🤖 Bot started and listening to channel: {config.TELEGRAM_CHANNEL}")
    app.run_polling()
