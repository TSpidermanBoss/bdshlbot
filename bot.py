from pyrogram import Client, Filters
k = -1001212143796
bot = "929464432:AAGcs59lrU1OKnSI7g02irSFQ4nB6b8XkKg"
app = Client (session_name="rr",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = bot)                                   
bullet = -1001483246865                                              
ferrari = -1001152188215                                             
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 client.send_message(k,message.text.markdown)
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 client.send_message(k,message.text.markdown)
app.run()
