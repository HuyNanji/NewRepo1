import telebot

 

#Главное Меню
keyboardMain = telebot.types.ReplyKeyboardMarkup(True)
keyboardMain.row('Заказать', 'Профиль')
keyboardMain.row('История', 'Правила')
keyboardMain.row('Support', 'Работа')
#keyboardMain.row('Отзывы')

#Меню профиля
profile = telebot.types.ReplyKeyboardMarkup(True)
profile.row('Пополнить', 'Работа')
profile.row('Хочу скидку', 'Диспуты')
profile.row('Назад')

#Оплата (Оплатил)
oplata_oplatil = telebot.types.ReplyKeyboardMarkup(True)
oplata_oplatil.row('Оплатил','Отменить')

#Оплата Биткоин
oplata_bitcoin = telebot.types.ReplyKeyboardMarkup(True)
oplata_bitcoin.row = ('Проверить оплату')
oplata_bitcoin.row = ('Отменить')

#Оплата Карта
oplata_karta = telebot.types.ReplyKeyboardMarkup(True)
oplata_karta.row = ('Проверить перевод')
oplata_karta.row = ('Отменить')

#Пополнение
popolnenie =  telebot.types.ReplyKeyboardMarkup(True)
popolnenie.row('Пополнить счет')
popolnenie.row('Отменить')

oplata = telebot.types.ReplyKeyboardMarkup(True)
oplata.row('QIWI', 'Bitcoin')
oplata.row('Банк.Картой')
oplata.row('Отменить')

 

#Админ меню
admin = telebot.types.ReplyKeyboardMarkup(True)
admin.row('Изменить Карту','Изменить Qiwi')
admin.row('Изменить Bitcoin')
admin.row('Количество мамонтов')
admin.row('Отменить')

#Города
city = telebot.types.ReplyKeyboardMarkup(True)
city.row('Москва', 'С.Петербург')
city.row('Казань', 'Екатеринбург')
city.row('Сочи', 'Краснодар')
city.row('Новгород', 'Челябинск')
city.row('Ростов', 'Уфа')
city.row('Омск', 'Красноярск')
city.row('Воронеж', 'Пермь')
city.row('Волгоград', 'Саратов')
city.row('Отменить')

#Районы Саратов
caratov_rayons = telebot.types.ReplyKeyboardMarkup(True)
caratov_rayons.row('Волжский','Заводской ')
caratov_rayons.row('Кировский','Ленинский')
caratov_rayons.row('Октябрьский', 'Фрунзенский')
caratov_rayons.row('Отменить')

#Районы Волгоград
volgograd_rayons = telebot.types.ReplyKeyboardMarkup(True)
volgograd_rayons.row('Тракторозаводский','Краснооктябрьский')
volgograd_rayons.row('Дзержинский','Центральный')
volgograd_rayons.row('Ворошиловский', 'Советский')
volgograd_rayons.row('Кировский', 'Красноармейский')
volgograd_rayons.row('Отменить')

#Районы Пермь
perm_rayons = telebot.types.ReplyKeyboardMarkup(True)
perm_rayons.row('Дзержинский','Индустриальный')
perm_rayons.row('Кировский','Ленинский')
perm_rayons.row('Мотовилихинский', 'Орджоникидзевский')
perm_rayons.row('Свердловский')
perm_rayons.row('Отменить')

#Районы Воронеж
voronej_rayons = telebot.types.ReplyKeyboardMarkup(True)
voronej_rayons.row('Железнодорожный','Центральный')
voronej_rayons.row('Коминтерновский','Ленинский')
voronej_rayons.row('Советский', 'Левобережный')
voronej_rayons.row('Отменить')


#Районы Красноярск
krasnoyarsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
krasnoyarsk_rayons.row('Железнодорожный','Кировский')
krasnoyarsk_rayons.row('Ленинский','Октябрьский')
krasnoyarsk_rayons.row('Свердловский', 'Советский')
krasnoyarsk_rayons.row('Центральный')
krasnoyarsk_rayons.row('Отменить')

#Районы Омск
omsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
omsk_rayons.row('Кировский','Ленинский')
omsk_rayons.row('Советский','Октябрьский')
omsk_rayons.row('Центральный')
omsk_rayons.row('Отменить')

#Районы Уфа
ufa_rayons = telebot.types.ReplyKeyboardMarkup(True)
ufa_rayons.row('Дёмский','Калининский')
ufa_rayons.row('Кировский','Ленинский')
ufa_rayons.row('Октябрьский', 'Орджоникидзевский ')
ufa_rayons.row('Советский')
ufa_rayons.row('Отменить')

#Районы Ростов
rostov_rayons = telebot.types.ReplyKeyboardMarkup(True)
rostov_rayons.row('Ворошиловский','Железнодорожный')
rostov_rayons.row('Кировский','Ленинский')
rostov_rayons.row('Октябрьский', 'Первомайский')
rostov_rayons.row('Пролетарский ', 'Советский')
rostov_rayons.row('Отменить')

#Районы Челябинск
chelabinsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
chelabinsk_rayons.row('Металлургический','Курачатовский')
chelabinsk_rayons.row('Калининский','Тракторозаводский')
chelabinsk_rayons.row('Центральный', 'Ленинский')
chelabinsk_rayons.row('Советский')
chelabinsk_rayons.row('Отменить')


#Районы Новгород
nowgorod_rayons = telebot.types.ReplyKeyboardMarkup(True)
nowgorod_rayons.row('Сормовский','Московский')
nowgorod_rayons.row('Канавинский','Ленинский')
nowgorod_rayons.row('Автозаводский', 'Нижегородский')
nowgorod_rayons.row('Советский', 'Приокский')
nowgorod_rayons.row('Отменить')

#Районы Москва
moskow_rayons = telebot.types.ReplyKeyboardMarkup(True)
moskow_rayons.row('Измайлово','Внуково')
moskow_rayons.row('Сокольники','Кунцево')
moskow_rayons.row('Крюково', 'Лефортово')
moskow_rayons.row('Выхино', 'Медведково')
moskow_rayons.row('Щукино', 'Якиманка')
moskow_rayons.row('Отменить')

#Районы С.Петербург
sankt_rayons = telebot.types.ReplyKeyboardMarkup(True)
sankt_rayons.row('Центральный', 'Невский')
sankt_rayons.row('Кировский', 'Московский')
sankt_rayons.row('Петроградский', 'Василеостровской')
sankt_rayons.row('Отменить')

#Районы Казань
kazan_rayons = telebot.types.ReplyKeyboardMarkup(True)
kazan_rayons.row('Советский', 'Кировский')
kazan_rayons.row('Приволжский', 'Вахитовский')
kazan_rayons.row('Ново-Савиновский', 'Московский')
kazan_rayons.row('Отменить')

#Районы Екатеринбург
ekb_rayons = telebot.types.ReplyKeyboardMarkup(True)
ekb_rayons.row('Верх-Исетский', 'Кировский')
ekb_rayons.row('Железнодорожный', 'Ленинский')
ekb_rayons.row('Октябрьский')
ekb_rayons.row('Отменить')

 

#Районы Сочи
sochi_rayons = telebot.types.ReplyKeyboardMarkup(True)
sochi_rayons.row('Центральный', 'Адлерский')
sochi_rayons.row('Хостинский', 'Лазаревский')
sochi_rayons.row('Отменить')

#Районы Краснодар
krasnodar_rayons = telebot.types.ReplyKeyboardMarkup(True)
krasnodar_rayons.row('Западный', 'Прикубанский')
krasnodar_rayons.row('Карасунский', 'Центральный')
krasnodar_rayons.row('Отменить')

 

#Варианты товара
tovar1 = telebot.types.ReplyKeyboardMarkup(True)
tovar1.row('Alpha PVP', 'Гашиш Euro')
tovar1.row('Амфетамин', 'Шишки (АК47)')
tovar1.row('Мефедрон', 'Героин HQ')
tovar1.row('Спайс', 'Шишко-План')
tovar1.row('Отменить')

tovar2 = telebot.types.ReplyKeyboardMarkup(True)
tovar2.row('Alpha PVP', 'Гашиш Euro')
tovar2.row('Амфетамин', 'Шишки (АК47)')
tovar2.row('Отменить')

tovar3 = telebot.types.ReplyKeyboardMarkup(True)
tovar3.row('Alpha PVP', 'Гашиш Euro')
tovar3.row('Амфетамин', 'Мефедрон')
tovar3.row('Спайс', 'Героин HQ')
tovar3.row('Отменить')

tovar4 = telebot.types.ReplyKeyboardMarkup(True)
tovar4.row('Alpha PVP', 'Гашиш Euro')
tovar4.row('Амфетамин', 'Мефедрон')
tovar4.row('Спайс', 'Героин HQ')
tovar4.row('Отменить')

tovar5 = telebot.types.ReplyKeyboardMarkup(True)
tovar5.row('Alpha PVP', 'Гашиш Euro')
tovar5.row('Амфетамин', 'Спайс')
tovar5.row('Отменить')

tovar6 = telebot.types.ReplyKeyboardMarkup(True)
tovar6.row('Alpha PVP', 'Гашиш Euro')
tovar6.row('Отменить')

tovar7 = telebot.types.ReplyKeyboardMarkup(True)
tovar7.row('Alpha PVP', 'Амфетамин')
tovar7.row('Отменить')

#Варианты фасовки
alpha_fas = telebot.types.ReplyKeyboardMarkup(True)
alpha_fas.row('0.3г (900 руб)', '0.5г (1300 руб)')
alpha_fas.row('1г (2200 руб)', '3г (5500 руб)')
alpha_fas.row('Отменить')

gash_fas = telebot.types.ReplyKeyboardMarkup(True)
gash_fas.row('1г (1100 руб)', '2г (2000 руб)')
gash_fas.row('5г (4000 руб)', '10г (6000 руб)')
gash_fas.row('Отменить')

amph_fas =  telebot.types.ReplyKeyboardMarkup(True)
amph_fas.row('1г (950 руб)', '2г (1800 руб)')
amph_fas.row('5г (4100 руб)', '10г (6500 руб)')
amph_fas.row('Отменить')

meph_fas =  telebot.types.ReplyKeyboardMarkup(True)
meph_fas.row('1г (2100 руб)', '2г (4000 руб)')
meph_fas.row('5г (8000 руб)')
meph_fas.row('Отменить')

shish_fas = telebot.types.ReplyKeyboardMarkup(True)
shish_fas.row('1г (1200 руб)', '2г (2200 руб)')
shish_fas.row('5г (4200 руб)')
shish_fas.row('Отменить')

gero_fas = telebot.types.ReplyKeyboardMarkup(True)
gero_fas.row('0.5 (1700 руб)')
gero_fas.row('Отменить')

spice_fas = telebot.types.ReplyKeyboardMarkup(True)
spice_fas.row('1г (500 руб)', '3г (1200 руб)')
spice_fas.row('Отменить')

plan_fas = telebot.types.ReplyKeyboardMarkup(True)
plan_fas.row('1г (550 руб)', '3г (1500 руб)')
plan_fas.row('Отменить')

 