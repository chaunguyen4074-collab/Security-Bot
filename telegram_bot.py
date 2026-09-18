import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from vietcap_api import get_stock_data

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Xin chào! Đây là FinTech Bot."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 HƯỚNG DẪN FINTECH BOT\n\n"
        "/start - Khởi động bot\n"
        "/help - Xem hướng dẫn\n"
        "/price symbol - Xem giá gần nhất\n"
        "/signal symbol - Xem tín hiệu kỹ thuật"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
async def signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Vui lòng nhập mã cổ phiếu.\nVí dụ: /signal FPT"
        )
        return

    symbol = context.args[0].upper()

    try:
        df = get_stock_data(symbol)
        latest = df.iloc[-1]

        message = (
            f"📊 Mã: {symbol}\n"
            f"💰 Giá đóng cửa: {latest['Close']:.2f}\n"
            f"📈 EMA20: {latest['EMA20']:.2f}\n"
            f"📉 EMA50: {latest['EMA50']:.2f}\n"
            f"RSI14: {latest['RSI14']:.2f}\n"
            f"🔔 Tín hiệu: {latest['Signal']}"
        )

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(
            f"Không lấy được dữ liệu cho mã {symbol}."
        )

async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Vui lòng nhập mã cổ phiếu.\nVí dụ: /price FPT"
        )
        return

    symbol = context.args[0].upper()

    try:
        df = get_stock_data(symbol)
        latest = df.iloc[-1]

        await update.message.reply_text(
            f"📊 Mã: {symbol}\n"
            f"💰 Giá gần nhất: {latest['Close']:.2f}"
        )

    except Exception:
        await update.message.reply_text(
            f"Không lấy được dữ liệu cho mã {symbol}."
        )

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("signal", signal_command))
app.add_handler(CommandHandler("price", price_command))

print("Bot đang chạy...")

app.run_polling()