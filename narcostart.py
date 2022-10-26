# -*- coding: utf-8 -*-
import telebot
from telebot import types
import sqlite3
import keyboards
import time
import config

 

bot = telebot.TeleBot(config.bot_token)
shop_name = config.shop_name
supp = config.support
#feedback = config.feedback
admin = config.admin

#Начало работы (приветствие)
@bot.message_handler(commands=['start'])
def start_message(message):
	global ref_stavka
	global lose_money
	global ref_user
	global ref_donate
	global ref_earn
	global ref_count
	userid = str(message.chat.id)
	ref_user = message.text
	ref_count = 0
	amount = 0
	ref_donate = 0
	userid = str(message.chat.id)
	username = str(message.from_user.username)
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	q = q.execute('SELECT * FROM users WHERE (id IS ? AND name IS ?)', (userid, username))
	row = q.fetchone()
	if row is None:
		q.execute("INSERT INTO users (id,name,amount,ref_user, ref_count, ref_donate) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"%(userid,username,amount,ref_user[7:],ref_count,ref_donate))
		connection.commit()
		if ref_user[7:] != '':
			q.execute("update users set ref_count = ref_count + 1" + " where id =" + str(ref_user[7:]))
			connection.commit()
			q.close()
			connection.close()
		else:
			connection = sqlite3.connect('database.sqlite')
			userid = str(message.chat.id)
			username = str(message.from_user.username)
			q = connection.cursor()
			q.execute("update users set ref_user = 05959 where id =" + str(userid))
			connection.commit()
			q.close()
			connection.close()
	bot.send_message(message.chat.id, '✌️ Добро пожаловать в автоматический магазин <b>'+str(shop_name)+'</b>\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nВ нашем шопе ты можешь преобрести лучший товар по самым сладким ценам.\n\nОт успешного соврешения заказа тебя отделяет лишь несколько шагов.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>Для начала выбери интересующий тебя пункт меню:</b>', parse_mode='HTML', reply_markup=keyboards.keyboardMain)

 
#-----------------------Команды-----------------------
@bot.message_handler(content_types=['text'])
def send_text(message):
	userid = str(message.chat.id)
	username = str(message.from_user.username)
	if message.text.lower() == 'оплатил':
		bot.send_message(message.chat.id, 'Платеж не найден, попробуйте через 5 минут',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
	elif message.text.lower() == 'отменить':
		bot.send_message(message.chat.id, 'Отменено, вернулись на главную', reply_markup=keyboards.keyboardMain)
	elif message.text.lower() == 'заказать':
		msg = bot.send_message(message.chat.id, 'Выберите ваш город', reply_markup=keyboards.city)
	elif message.text.lower() == 'москва':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.moskow_rayons)
		bot.register_next_step_handler(msg, moskow)
	elif message.text.lower() == 'с.петербург':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.sankt_rayons)
		bot.register_next_step_handler(msg, sankt_piter)
	elif message.text.lower() == 'казань':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.kazan_rayons)
		bot.register_next_step_handler(msg, kazan)
	elif message.text.lower() == 'екатеринбург':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.ekb_rayons)
		bot.register_next_step_handler(msg, ekb)
	elif message.text.lower() == 'сочи':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.sochi_rayons)
		bot.register_next_step_handler(msg, sochi)
	elif message.text.lower() == 'краснодар':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.krasnodar_rayons)
		bot.register_next_step_handler(msg, krasnodar)
	elif message.text.lower() == 'новгород':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.nowgorod_rayons)
		bot.register_next_step_handler(msg, nowgorod)   
	elif message.text.lower() == 'челябинск':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.chelabinsk_rayons)
		bot.register_next_step_handler(msg, chelabinsk)  
	elif message.text.lower() == 'ростов':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.rostov_rayons)
		bot.register_next_step_handler(msg, rostov)  
	elif message.text.lower() == 'уфа':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.ufa_rayons)
		bot.register_next_step_handler(msg, ufa)  
	elif message.text.lower() == 'омск':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.omsk_rayons)
		bot.register_next_step_handler(msg, omsk)  
	elif message.text.lower() == 'красноярск':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.krasnoyarsk_rayons)
		bot.register_next_step_handler(msg, krasnoyarsk)  
	elif message.text.lower() == 'воронеж':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.voronej_rayons)
		bot.register_next_step_handler(msg, voronej) 
	elif message.text.lower() == 'пермь':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.perm_rayons)
		bot.register_next_step_handler(msg, perm)        
	elif message.text.lower() == 'волгоград':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.volgograd_rayons)
		bot.register_next_step_handler(msg, volgograd)   
	elif message.text.lower() == 'саратов':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.caratov_rayons)
		bot.register_next_step_handler(msg, caratov)  
	elif message.text.lower() == 'тюмень':
		msg = bot.send_message(message.chat.id, 'Выберите желаемый район', reply_markup=keyboards.tumen_rayons)
		bot.register_next_step_handler(msg, tumen)          
	elif message.text.lower() == 'профиль':
		msg = bot.send_message(message.chat.id, '<b>Ваш профиль</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n👤Ваш Юзер: @'+str(username)+'\n🆔Ваш ID: <code>'+str(userid)+'</code>\n🛍Количество покупок: <code>0</code>\n💰Ваш баланс: <code>0 RUB</code>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💸Персональная скидка: <code>0%</code>\n🏇До сл.скидки осталось: <code>3 покупки</code>\n🙅‍♂️Открытые диспуты: <code>0</code>\n📊Рейтинг: <code>0%</code> (Новичёк)', parse_mode='HTML', reply_markup=keyboards.profile)
		bot.register_next_step_handler(msg, profile_page)
	elif message.text.lower() == 'история':
		msg = bot.send_message(message.chat.id, 'Ваша история покупок пуста. Самое время совершить первую.', parse_mode='HTML')
	elif message.text.lower() == 'правила':
		msg = bot.send_message(message.chat.id, '<b>Правила магазина "'+str(shop_name)+'"</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n1.Магазин несет ответственность за качество продаваемого товара. Если качество вас не устроило - ждем вашего сообщения в службу поддержки (Support), решим эту проблему в самые кратчайшие сроки.\n2.Магазин оставляет за собой право на отказ в обслуживании любого пользователя без объяснения причин. Деньги, в данном случае, возвращаются через службу поддержки на тот кошелек, с которого производилась оплата.\n3.Гарантия на товар 6 часов с момента покупки. Обращения, отправленные позже установленного правилами срока - не рассматриваются.\n4.Пополнение баланса с помощью платежной системы QIWI с неправильным комментарием или отсутствием его - бонус магазина, но если ваш рейтинг выше 70% всегда можно договориться.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nСовершая покупки в нашем магазине вы автоматически соглашаетесь с данными правилами.', parse_mode='HTML')
	elif message.text.lower() == 'support':
		msg = bot.send_message(message.chat.id, '<b>Служба Поддержки "'+str(shop_name)+'"</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nПример обращения в службу поддержки:\n1. Номер заказа\n2. Время приезда на местность\n3. Описание проблемы\n4. Фотографии места (2-4шт)\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nКонтакт службы поддержки: '+str(supp)+' ', parse_mode='HTML')
#	elif message.text.lower() == 'отзывы':
#		msg = bot.send_message(message.chat.id, '<b>Отзывы "'+str(shop_name)+'"</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nВсе отзывы публикуются выборочно на нашем официальном канале. Хочешь попасть в их число? Соверши покупку в нашем магазине, попробуй товар и напиши самый ахуенный отзыв, на какой ты только способен!\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nНаш канал с отзывами: '+str(feedback)+' ', parse_mode='HTML')
	elif message.text.lower() == 'работа':
		msg = bot.send_message(message.chat.id, '<b>Работа в "'+str(shop_name)+'"</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nНаш магазин ведет постоянный набор по всей РФ.\nОткрыты вакансии на следующие должности:\n    1. Кладмен (от 400 руб/клад)\n    2. Трафаретчик (от 80 руб/рисунок)\n    3. Перевозчик (только с залогом)\n    4. Склад (только с залогом)\n\nТак же приглашаем к сотрудничеству химиков и гроверов с качественным товаром. Достойную оплату гарантируем. Найдете магазин в который продадите дороже - мы перебьем цену. \n➖➖➖➖➖➖➖➖➖➖➖➖➖\nДля связи писать: '+str(supp)+' с пометкой "Работа" ', parse_mode='HTML')


	elif message.text.lower() == '/admin':
		if message.chat.id == admin:
			bot.send_message(message.chat.id, 'Мы в админке', reply_markup=keyboards.admin)
	elif message.text.lower() == 'количество мамонтов':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute("SELECT COUNT(id) from users	")
			stata_users_ids_message = str(q.fetchone()[0])
			bot.send_message(message.chat.id, '📈 Мамонтов в боте: ' + stata_users_ids_message)
			q.close()
			connection.close()
	elif message.text.lower() == 'изменить карту':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute('select karta from config where Id = 1')
			karta = q.fetchone()[0]
			msg = bot.send_message(message.chat.id, 'Сейчас установлена карта: '+karta+'\n\nВведите новую карту\nP.S: Если вы случайно нажали на кнопку, укажите уже установленную карту')
			bot.register_next_step_handler(msg, admin_new_karta)

	elif message.text.lower() == 'изменить qiwi':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute('select qiwi from config where Id = 1')
			qiwi = q.fetchone()[0]
			msg = bot.send_message(message.chat.id, 'Сейчас установлен qiwi: '+qiwi+'\n\nВведите новый qiwi кошелек\nP.S: Если вы случайно нажали на кнопку, укажите уже установленный')
			bot.register_next_step_handler(msg, admin_new_qiwi)

	elif message.text.lower() == 'изменить bitcoin':
		if message.chat.id == admin:
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute('select bitcoin from config where Id = 1')
			bitcoin = q.fetchone()[0]
			msg = bot.send_message(message.chat.id, 'Сейчас установлен bitcoin: '+bitcoin+'\n\nВведите новый bitcoin кошелек\nP.S: Если вы случайно нажали на кнопку, укажите уже установленный')
			bot.register_next_step_handler(msg, admin_new_bitcoin)

 
#Профиль
def profile_page(message):
	if message.text == 'Пополнить':
		msg = bot.send_message(message.chat.id, 'Выберите платежную систему', reply_markup=keyboards.oplata)
		bot.register_next_step_handler(msg, balans)
	elif message.text.lower() == 'хочу скидку':
		msg = bot.send_message(message.chat.id, 'ℹ️Персональная скидка устанавливается автоматически после достижения определенного числа покупок.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Таблица скидок:</b>\n    ➡️3 покупки: Скидка 2%\n    ➡️5 покупок: Скидка 5%\n    ➡️10+ покупок: Скидка 10%\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n⚠️Попрошайкам выпрашивающим скидки в службе поддержки накидываем +5% наценки на весь товар!', parse_mode='HTML', reply_markup=keyboards.profile)
		bot.register_next_step_handler(msg, profile_page)
	elif message.text.lower() == 'работа':
		msg = bot.send_message(message.chat.id, '<b>Работа в "'+str(shop_name)+'"</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nНаш магазин ведет постоянный набор по всей РФ.\nОткрыты вакансии на следующие должности:\n    1. Кладмен (от 400 руб/клад)\n    2. Трафаретчик (от 80 руб/рисунок)\n    3. Перевозчик (только с залогом)\n    4. Склад (только с залогом)\n\nТак же приглашаем к сотрудничеству химиков и гроверов с качественным товаром. Достойную оплату гарантируем. Найдете магазин в который продадите дороже - мы перебьем цену. \n➖➖➖➖➖➖➖➖➖➖➖➖➖\nДля связи писать: '+str(supp)+' с пометкой "Работа" ', parse_mode='HTML')
		bot.register_next_step_handler(msg, profile_page)
	elif message.text.lower() == 'диспуты':
		msg = bot.send_message(message.chat.id, 'На данный момент нет открытых диспутов.', reply_markup=keyboards.profile)
		bot.register_next_step_handler(msg, profile_page)
	elif message.text.lower() == 'назад':
		msg = bot.send_message(message.chat.id, 'Вернулись в главное меню.', reply_markup=keyboards.keyboardMain)

#Районы Саратов
def caratov(message):
	if message.text == 'Волжский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Заводской':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Октябрьский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Фрунзенский ':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


#Районы Волгоград
def volgograd(message):
	if message.text == 'Тракторозаводский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Краснооктябрьский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Дзержинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ворошиловский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Красноармейский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


#Районы Пермь
def perm(message):
	if message.text == 'Дзержинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Индустриальный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Мотовилихинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Орджоникидзевский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Свердловский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



#Районы Воронеж
def voronej(message):
	if message.text == 'Железнодорожный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Коминтерновский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Левобережный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)




#Районы Красноярск
def krasnoyarsk(message):
	if message.text == 'Железнодорожный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Октябрьский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Свердловский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)




#Районы Омск
def omsk(message):
	if message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Октябрьский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



#Районы Уфа
def ufa(message):
	if message.text == 'Дёмский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Калининский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Октябрьский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Орджоникидзевский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)





#Районы Ростов
def rostov(message):
	if message.text == 'Ворошиловский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Железнодорожный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Первомайский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Октябрьский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Пролетарский ':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский ':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
        
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)


#Районы Челябинск
def chelabinsk(message):
	if message.text == 'Металлургический':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Курачатовский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Калининский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Тракторозаводский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)



#Районы Нижний новгород
def nowgorod(message):
	if message.text == 'Сормовский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Московский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Канавинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Автозаводский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Нижегородский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Приокский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Районы Москва
def moskow(message):
	if message.text == 'Измайлово':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Сокольники':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Внуково':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Кунцево':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Крюково':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Щукино':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Лефортово':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Выхино':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Медведково':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Якиманка':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)

	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Районы Санкт Петербург
def sankt_piter(message):
	if message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Невский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Петроградский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Московский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Василеостровской':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Районы Казань
def kazan(message):
	if message.text == 'Советский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Приволжский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Ново-Савиновский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Московский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar3)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Вахитовский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Районы Екатеринбург
def ekb(message):
	if message.text == 'Верх-Исетский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)
	if message.text == 'Железнодорожный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
	if message.text == 'Кировский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
	if message.text == 'Ленинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)
	if message.text == 'Октябрьский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar5)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Районы Сочи
def sochi(message):
	if message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar2)
		bot.register_next_step_handler(msg, fasov)
	if message.text == 'Адлерский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
	if message.text == 'Хостинский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
	if message.text == 'Лазаревский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar7)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Районы Краснодар
def krasnodar(message):
	if message.text == 'Западный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Карасунский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar1)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Прикубанский':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar6)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Центральный':
		msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboards.tovar4)
		bot.register_next_step_handler(msg, fasov)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Товар
def fasov(message):
	if message.text == 'Alpha PVP':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.alpha_fas)
		bot.register_next_step_handler(msg, popolnenie)

	elif message.text == 'Гашиш Euro':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.gash_fas)
		bot.register_next_step_handler(msg, popolnenie)

	elif message.text == 'Амфетамин':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.amph_fas)
		bot.register_next_step_handler(msg, popolnenie)

	elif message.text == 'Шишки (АК47)':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.shish_fas)
		bot.register_next_step_handler(msg, popolnenie)

	elif message.text == 'Мефедрон':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.meph_fas)
		bot.register_next_step_handler(msg, popolnenie)

	elif message.text == 'Героин HQ':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.gero_fas)
		bot.register_next_step_handler(msg, popolnenie)

	elif message.text == 'Спайс':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.spice_fas)
		bot.register_next_step_handler(msg, popolnenie)

	elif message.text == 'Шишко-План':
		msg = bot.send_message(message.chat.id, 'Выберите желаемую фасовку', reply_markup=keyboards.plan_fas)
		bot.register_next_step_handler(msg, popolnenie)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

 
#Фасовки
def popolnenie(message):
	if message.text == '0.3г (900 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 900 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '0.5г (1300 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 1300 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '1г (2200 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 2200 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '3г (5500 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 5500 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '1г (1100 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 1100 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '2г (2000 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 2000 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '5г (4000 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 4000 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '10г (6000 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 6000 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '1г (950 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 950 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '2г (1800 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 1800 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '5г (4100 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 4100 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '10г (6500 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 6500 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '1г (2100 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 2100 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '2г (4000 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 4000 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '5г (8000 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 8000 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '1г (1200 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 1200 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '2г (2200 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 2200 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '5г (4200 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 4200 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '0.5 (1700 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 1700 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '1г (500 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 500 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '3г (1200 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 1200 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '1г (550 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 550 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == '3г (1500 руб)':
		msg = bot.send_message(message.chat.id, 'Для покупки данной позиции вам необходимо пополнить счет на 1500 рублей.\nДля пополнения нажмите кнопку <b>"Пополнить счет"</b> или вернитесь в главное меню и перейдите в раздел <b>"Профиль"</b>',parse_mode='HTML', reply_markup=keyboards.popolnenie)
		bot.register_next_step_handler(msg, oplata)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Пополнение
def oplata(message):
	if message.text == 'Пополнить счет':
		msg = bot.send_message(message.chat.id, 'Для пополнения счета вам необходимо выбрать платежную систему:', reply_markup=keyboards.oplata)
		bot.register_next_step_handler(msg, balans)
	elif message.text == 'Отменить':
		msg = bot.send_message(message.chat.id, 'Вы успешно вернулись в главное меню.', reply_markup=keyboards.keyboardMain)

 
#Выбрана система платежей
def balans(message):
	userid = str(message.chat.id)
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	q.execute("select ref_user from users where Id =" + userid )
	ref_user = q.fetchone()[0]
	q.execute('select karta from config where Id = 1')
	karta = q.fetchone()[0]
	q.execute('select qiwi from config where Id = 1')
	qiwi = q.fetchone()[0]
	q.execute('select bitcoin from config where Id = 1')
	bitcoin = q.fetchone()[0]
	if message.text == 'QIWI':
		msg = bot.send_message(message.chat.id, 'Для пополнения баланса с помощью <b>QIWI</b> вам необходимо перевести необходимую сумму по указанным ниже реквизитам:\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>QIWI кошелек:</b> <code>'+str(qiwi)+'</code>\n<b>Комментарий:</b> <code>' + str(userid) + '</code>\n<b>Сумма:</b> Любая необходимая\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>ВНИМАНИЕ: Деньги отправленные без комментария к платежу не зачисляются. Вернуть данные средства будет невозможно!</b>\n\nСразу после оплаты деньги будут зачислены на ваш личный счет в магазине. Проверить баланс вы можете в разделе "Профиль"\n Спасибо что вы с нами!',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
	elif message.text == 'Bitcoin':
		msg = bot.send_message(message.chat.id, 'Для пополнения баланса с помощью <b>Bitcoin</b> вам необходимо перевести необходимую сумму по указанным ниже реквизитам:\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Bitcoin кошелек:</b> <code>'+str(bitcoin)+'</code>\n<b>Сумма:</b> Любая необходимая\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>ВНИМАНИЕ: Баланс будет пополнен после получения 2 подтверждений от сети blockchain.</b>\n\nСразу после получения подтверждений деньги будут зачислены на ваш личный счет в магазине. Проверить баланс вы можете в разделе "Профиль"\n Спасибо что вы с нами!',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
	elif message.text == 'Банк.Картой':
		msg = bot.send_message(message.chat.id, 'Для пополнения баланса с помощью <b>Банковской карты</b> вам необходимо перевести необходимую сумму по указанным ниже реквизитам:\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Номер счета:</b> <code>'+str(karta)+'</code>\n<b>Сумма:</b> Любая необходимая\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nСразу после оплаты деньги будут зачислены на ваш личный счет в магазине. Проверить баланс вы можете в разделе "Профиль"\nСпасибо что вы с нами!',parse_mode='HTML', reply_markup=keyboards.oplata_oplatil)
	elif message.text == 'Отменить':
		bot.send_message(message.chat.id, 'Вернулись на главную', reply_markup=keyboards.keyboardMain)

#Изменение карты
def admin_new_karta(message):
	new_karta = message.text
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	try:
		q.execute("update config set karta = " + str( new_karta ) + " where id = 1")
		connection.commit()
		q.close()
		connection.close()
		bot.send_message(message.chat.id, 'Успешно!', reply_markup=keyboards.admin)
	except:
		bot.send_message(admin, 'Ошибка', reply_markup=keyboards.admin)

 
#Изменение киви
def admin_new_qiwi(message):
	new_qiwi = message.text
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	try:
		q.execute("update config set qiwi = " + str( new_qiwi ) + " where id = 1")
		connection.commit()
		q.close()
		connection.close()
		bot.send_message(message.chat.id, 'Успешно!', reply_markup=keyboards.admin)
	except:
		bot.send_message(admin, 'Ошибка', reply_markup=keyboards.admin)

#Изменение бикоин
def admin_new_bitcoin(message):
	new_bitcoin = message.text
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	try:
		q.execute("update config set bitcoin = " + str( new_bitcoin ) + " where id = 1")
		connection.commit()
		q.close()
		connection.close()
		bot.send_message(message.chat.id, 'Успешно!', reply_markup=keyboards.admin)
	except:
		bot.send_message(admin, 'Ошибка', reply_markup=keyboards.admin)

 
#Конец
bot.polling(none_stop=True)