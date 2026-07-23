from flask import Flask, request, jsonify
import telebot
import os

BOT_TOKEN = "8067463049:AAFgPYjPjPU2yfe3c2mp8IcXq0jAPrfYtD0"
CHAT_ID = "103006844"
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.data.decode('utf-8')
        print(f"📥 إشارة مستلمة: {data}")
        
        formatted_message = f"🚨 **إشارة OTC حقيقية من TradingView** 🚨\n\n{data}"
        
        bot.send_message(CHAT_ID, formatted_message, parse_mode="Markdown")
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"❌ خطأ: {e}")
        return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
