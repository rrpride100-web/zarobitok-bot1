import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8697397505:AAFw-SsPCT29mryhYUN52XdAp2yzDUeJSBs"
MFO_URL = "https://kiepa.stick.ws"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("📖 ОЗНАЙОМЛЕННЯ", callback_data="info")],
        [InlineKeyboardButton("📜 УМОВИ", callback_data="rules")],
        [InlineKeyboardButton("💰 ЯК ПРАВИЛЬНО РОБИТИ", callback_data="howto")],
        [InlineKeyboardButton("🎯 ПЕРЕЙТИ ДО МФО", url=MFO_URL)]
    ]
    await update.message.reply_text(
        f"🔥 Вітаю, {user.first_name}! 🔥\n\nОбери дію:\n\n❓ Підтримка: @cpa_rm",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text(
            "📖 ОЗНАЙОМЛЕННЯ\n\n"
            "💰 Це легальна партнерська програма.\n"
            "Ми співпрацюємо з офіційними МФО.\n\n"
            "Як заробляти:\n"
            "1️⃣ Переходь за посиланням\n"
            "2️⃣ Реєструєшся\n"
            "3️⃣ Береш мінімальну позику\n"
            "4️⃣ Отримуєш виплату\n\n"
            "❓ Підтримка: @cpa_rm\n\n"
            "👇 Натисни НАЗАД",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("◀️ НАЗАД", callback_data="back_to_main")
            ]])
        )
    elif query.data == "rules":
        await query.edit_message_text(
            "📜 УМОВИ УЧАСТІ\n\n"
            "🔞 Вік: 18+\n"
            "📍 Географія: Україна (ВПН за кордоном)\n"
            "💳 Картка: українська (для Bank ID)\n"
            "🚫 Без прострочених кредитів\n"
            "⚠️ Реєструйся тільки за нашими посиланнями\n\n"
            "❓ Підтримка: @cpa_rm\n\n"
            "👇 Натисни НАЗАД",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("◀️ НАЗАД", callback_data="back_to_main")
            ]])
        )
    elif query.data == "howto":
        await query.edit_message_text(
            "💰 ЯК ПРАВИЛЬНО РОБИТИ\n\n"
            "1️⃣ Переходь на сайт через кнопку 'ПЕРЕЙТИ ДО МФО'\n"
            "2️⃣ Реєструєшся, підтверджуєш Bank ID\n"
            "3️⃣ Береш позику 500-1000 грн на 7-15 днів\n"
            "4️⃣ Отримуєш гроші на картку (це УСПІШНО)\n"
            "5️⃣ Погашаєш кредит через 1-2 дні (відсотки повернемо)\n\n"
            "💰 Чим більше успішних операцій - тим більше грошей!\n\n"
            "❓ Підтримка: @cpa_rm\n\n"
            "👇 Натисни НАЗАД",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("◀️ НАЗАД", callback_data="back_to_main")
            ]])
        )
    elif query.data == "back_to_main":
        keyboard = [
            [InlineKeyboardButton("📖 ОЗНАЙОМЛЕННЯ", callback_data="info")],
            [InlineKeyboardButton("📜 УМОВИ", callback_data="rules")],
            [InlineKeyboardButton("💰 ЯК ПРАВИЛЬНО РОБИТИ", callback_data="howto")],
            [InlineKeyboardButton("🎯 ПЕРЕЙТИ ДО МФО", url=MFO_URL)]
        ]
        await query.edit_message_text(
            "🔥 ГОЛОВНЕ МЕНЮ\n\nОбери дію:\n\n❓ Підтримка: @cpa_rm",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
