import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from Login import save_accounts_to_json

TOKEN = "TOKEN"
def bytes_to_gigabytes(bytes_value):
    return bytes_value / (1024 * 1024 * 1024)
# فایل JSON که داده‌ها در آن قرار دارد
json_file = 'data.json'

# تابعی برای جستجوی کاربر بر اساس ایمیل
def get_user_info(email):
    with open(json_file, 'r') as f:
        data = json.load(f)

    for panel, users in data.items():
        for user in users:
            for client in user['clientStats']:
                if client['email'] == email:
                    up_gb = bytes_to_gigabytes(client['up'])
                    down_gb = bytes_to_gigabytes(client['down'])
                    return f"{panel} \n User found: {email}\n" \
                           f"Up: {up_gb:.2f}\n" \
                           f"Down: {down_gb:.2f}\n" \
                           f"Enable: {client['enable']}\n" \
                           f"Expiry Time: {client['expiryTime']}\n" \
                           f"Total: {client['total']}"
    return "User not found"

# هندلر دستور start
async def start(update: Update, context) -> None:
    await update.message.reply_text('Welcome! Send me an email to get the user info.')

# هندلر پیام‌های کاربر
async def handle_message(update: Update, context) -> None:
    email = update.message.text

    # فراخوانی save_accounts_to_json برای به‌روزرسانی اطلاعات پنل‌ها
    save_accounts_to_json()

    # جستجوی کاربر بر اساس ایمیل
    user_info = get_user_info(email)

    # نمایش نتیجه به کاربر
    await update.message.reply_text(user_info)

# تنظیمات اصلی ربات
def main():
    # توکن ربات خود را در اینجا وارد کنید


    # ساخت اپلیکیشن ربات با استفاده از Application.builder()
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلرها
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # اجرای ربات
    application.run_polling()

if __name__ == '__main__':
    main()
