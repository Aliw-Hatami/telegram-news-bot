import os
import time
import feedparser
import telegram

# توکن ربات و آیدی کانال
BOT_TOKEN = os.getenv("7686858863:AAGE7W5cYPFU7JNe4Yuyprj9MTX8JbS-zbc")
CHANNEL_ID = os.getenv("@Daijoplus")  # مثلاً "@Daijoplus"

# لینک RSS سایت زومیت
RSS_URL = "https://www.zoomit.ir/feed/"

# ساخت ربات
bot = telegram.Bot(token=BOT_TOKEN)

# ذخیره عنوان‌های قبلی برای جلوگیری از تکرار
sent_titles = set()

def get_feed():
    feed = feedparser.parse(RSS_URL)
    if not feed.entries:
        return None
    return feed.entries[0]  # جدیدترین خبر

def main():
    while True:
        entry = get_feed()
        if entry and entry.title not in sent_titles:
            sent_titles.add(entry.title)

            caption = f"📰 {entry.title}\n\n📡 منبع: Zoomit\n🔗 https://t.me/Daijoplus"
            image_url = entry.media_content[0]['url'] if 'media_content' in entry else None

            try:
                if image_url:
                    bot.send_photo(chat_id=CHANNEL_ID, photo=image_url, caption=caption)
                else:
                    bot.send_message(chat_id=CHANNEL_ID, text=caption)
            except Exception as e:
                print("خطا در ارسال پیام:", e)

        time.sleep(1800)  # هر ۳۰ دقیقه

if __name__ == "__main__":
    main()

