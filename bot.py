from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
from web import keep_alive  # We'll fix this too

import threading
import socketserver

# --- Dummy TCP server for Koyeb ---
class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b"OK")

def start_tcp_server():
    import os
    port = int(os.environ.get("PORT", 8080))  # Koyeb uses 8080
    server = socketserver.TCPServer(("0.0.0.0", port), TCPHandler)
    server.serve_forever()

# --- Pyrogram bots ---
bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

if __name__ == "__main__":
    # Start dummy TCP server in background
    threading.Thread(target=start_tcp_server).start()

    # Start the bot(s)
    if STRING:
        apps = [Client2, bot]
        for app in apps:
            app.start()
        idle()
        for app in apps:
            app.stop()
    else:
        bot.run()