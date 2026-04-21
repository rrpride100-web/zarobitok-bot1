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
            f"📖 *ОЗНАЙОМЛЕННЯ*\n\n"
            f"💰 Це легальна партнерська програма.\n"
            f"Ми співпрацюємо з офіційними МФО.\n\n"
            f"*Як заробляти:*\n"
            f"1️⃣ Переходь за посиланням\n"
            f"2️⃣ Реєструєшся\n"
            f"3️⃣ Береш мінімальну позику\n"
            f"4️⃣ Отримуєш виплату\n\n"
            f"❓ Підтримка: @cpa_rm\n\n"
            f"👇 Натисни *'НАЗАД'*:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("◀️ НАЗАД", callback_data="back_to_main")
            ]])
        )
    elif query.data == "rules":
        await query.edit_message_text(
            f"📜 *УМОВИ УЧАСТІ*\n\n"
            f"🔞 Вік: 18+\n"
            f"📍 Географія: Україна (ВПН за кордоном)\n"
            f"💳 Картка: українська (для Bank ID)\n"
            f"🚫 Без прострочених кредитів\n"
            f"⚠️ Реєструйся тільки за нашими посиланнями\n\n"
            f"❓ Підтримка: @cpa_rm\n\n"
            f"👇 Натисни *'НАЗАД'*:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("◀️ НАЗАД", callback_data="back_to_main")
            ]])
        )
    elif query.data == "howto":
        await query.edit_message_text(
            f"💰 *ЯК ПРАВИЛЬНО РОБИТИ*\n\n"
            f"1️⃣ Переходь на сайт через кнопку 'ПЕРЕЙТИ ДО МФО'\n"
            f"2️⃣ Реєструєшся, підтверджуєш Bank ID\n"
            f"3️⃣ Береш позику 500-1000 грн на 7-15 днів\n"
            f"4️⃣ Отримуєш гроші на картку (це АПРУВ)\n"
            f"5️⃣ Погашаєш кредит через 1-2 дні (відсотки повернемо)\n\n"
            f"💰 Чим більше апрувів - тим більше грошей!\n\n"
            f"❓ Підтримка: @cpa_rm\n\n"
            f"👇 Натисни *'НАЗАД'*:",
            parse_mode="Markdown",
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
            f"🔥 *ГОЛОВНЕ МЕНЮ*\n\nОбери дію:\n\n❓ Підтримка: @cpa_rm",
            parse_mode="Markdown",
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
