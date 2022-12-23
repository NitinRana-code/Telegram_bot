from telegram.ext.updater import Updater
from telegram.ext import ConversationHandler,CommandHandler,RegexHandler 
import telegram.ext
import os
import openai
import telepot
from Cred import tokens 
key = tokens.TOKEN_OPENAI
openai.api_key = os.getenv(key)

token = tokens.TOKEN_TELGERAM

updater = Updater(token, use_context=True  )
dispatcher = updater.dispatcher

def start(update,context):
    update.message.reply_text("""Welcome!!!🌟✨✨
Your bot 🤖 is ready to use :)
Try these commands👇
/say --> ask me anything!🤔
/help --> if you want any help🙋‍♂️
/img --> to generate image🐈""")
    
    
    
    
query = []
res = ""
pr =""

def say(update, context):
    global pr
    global res
    inp_msg = update.message.text
    inp_args = inp_msg.split("/say ")     

    if len(inp_args)>1:  #if no message typed by user
        query.append(inp_args[1])
        pr+=f"Human: {query[len(query)-1]}. \nAi:"
        
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=pr,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        
        msg = response["choices"][0]["text"]
        res = msg
        update.message.reply_text(msg)
        pr+=f" {res}\n"
        
    else:
        update.message.reply_text("/say ask me something")

bot = telepot.Bot(token)  
def img(update, context):
    chat_id = update.message.chat_id
    inp_msg = update.message.text
    inp_args = inp_msg.split("/img")

    if inp_args[1]!="":
        response = openai.Image.create(
            prompt=inp_args[1],
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        bot.sendPhoto(chat_id, image_url)

    else:
        update.message.reply_text("/img type your prompt to generate an image")


def help(update, context):
    update.message.reply_text("""Try these following command to start with us ⬇️
/start --> Start with us!🚀
/say type any thing you want🤔
/img type prompt to generate image🐈""")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("say", say))
dispatcher.add_handler(CommandHandler("img", img))
dispatcher.add_handler(CommandHandler("help", help))
updater.start_polling()
updater.idle()

