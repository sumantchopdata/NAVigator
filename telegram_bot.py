# telegram_bot.py
# This module provides a function to send messages to a Telegram chat using a bot.
# It uses the python-telegram-bot library to interact with the Telegram Bot API.

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from scheme_lookup import search_scheme
from mf_data import fetch_nav_history
from analyzer import analyze_fund
from config import TELEGRAM_BOT_TOKEN


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()

    await update.message.reply_text("⏳ Fetching data...")

    results = search_scheme(query)

    query_clean = query.strip().lower()

    exact_match = None

    for scheme in results:
        name = scheme["schemeName"].strip().lower()
        if name == query_clean:
            exact_match = scheme
            break

    if not results:
        await update.message.reply_text(f"❌ No scheme found for: {query}")
        return

    # PRIORITY: exact match
    if exact_match:
        scheme = exact_match

    # Otherwise suggest options
    elif len(results) > 1:
        reply = "🤔 Did you mean:\n\n"

        for i, scheme in enumerate(results, 1):
            reply += f"{i}. {scheme['schemeName']}\n"

        reply += "\nReply with the exact name."
        await update.message.reply_text(reply)
        return

    # fallback
    else:
        scheme = results[0]
    
    # If multiple results, suggest options

    name = scheme["schemeName"]
    code = scheme["schemeCode"]

    try:
        df = fetch_nav_history(code)
        result = analyze_fund(df, name)

        if not result:
            await update.message.reply_text(f"⚠️ Not enough data for {name}")
            return

        data = result

        message = (
            f"📊 {name}\n"
            f"Return: {data['return_pct']}%\n"
            f"Volatility: {data['volatility']}%\n"
            f"Sharpe: {data['sharpe']}\n"
            f"Sortino: {data['sortino']}\n"
            f"Beta: {data['beta']}\n"
            f"Alpha: {data['alpha']}%\n"
            f"Status: {data['status']}"
        )

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"❌ Error fetching data for {name}")


def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()