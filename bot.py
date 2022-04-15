import telebot

bot=telebot.TeleBot('5177554108:AAGKqa3q77Q1pgC4EOrMA9N8RMwcGfvsYsc')

goods_name = {'Elf Bar Classic 1500 Blueberry':20,'Elf Bar Classic 1500 Mango':20,'Elf Bar Classic 1500 Grape':20,'Elf Bar Classic 1500 Banana ice':20,'Elf Bar Classic 1500 Spearmint':20,'Elf Bar Classic 1500 Watermelon':20,'Elf Bar Classic 1500 Apple Peach':20,'Elf Bar Lux 1500 Red Bull Grape':20,'Elf Bar Lux 1500 Mango Peach Watermelon':20,'Elf Bar Lux 1500 Banana Milk':20}
wait_goods = 1000000000
wait_fullname = 1000000000
wait_count = 1000000000
wait_phone = 1000000000
wait_adress = 1000000000
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(True)
    item1 = telebot.types.KeyboardButton('💨 Elf Bar Classic 1500')
    item2 = telebot.types.KeyboardButton('💨 ELF BAR Lux 1500')
    markup.add(item1,item2)
    bot.send_message(message.chat.id,'Шановний відвідувач, ми є оптовими постачальниками одноразових електронних сигарет ELF BAR 1500💨\n\nНаші переваги серед конкурентів:\n- гарантуємо якість та надійність📌\n- тільки оригінал✨\n- найдешевші ціни на 🇺🇦 ринку\n- бонуси та знижки постійним клієнтам 🎁\n\nМи раді, що ви з нами!🥰',reply_markup=markup)
@bot.message_handler(regexp='💵 Купити|💸 Купити')
def get_order(message):
    global wait_goods
    wait_goods = message.message_id
    global username
    username = message.from_user.username
    global goods
    if message.text == '💵 Купити':
        goods = 'Elf Bar Classic 1500'
    elif message.text == '💸 Купити':
        goods = 'ELF BAR Lux 1500'
    markup_goods = telebot.types.ReplyKeyboardMarkup(True)
    row_count = 0
    if goods == 'Elf Bar Classic 1500':
        for i in goods_name:
            if row_count < 7:
                markup_goods.add(i)
            row_count += 1
    elif goods == 'ELF BAR Lux 1500':
        for i in goods_name:
            if row_count > 6:
                markup_goods.add(i)
            row_count += 1
    bot.send_message(message.chat.id,'📃 Зробіть вибір моделі',reply_markup=markup_goods)
@bot.message_handler(func=lambda message: wait_goods+2==message.message_id, content_types=['text'])
def get_order(message):
    global wait_count
    wait_count = message.message_id
    global goods
    goods = message.text
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'📃 Введіть кількість (від 10 шт.)',reply_markup=markup)
@bot.message_handler(func=lambda message: wait_count+2==message.message_id, content_types=['text'])
def get_order(message):
    global wait_fullname
    wait_fullname = message.message_id
    global count
    count = message.text
    if int(count) < 10:
        bot.send_message(message.chat.id,'Допустима кількість від 10 шт.')
        start(message)
    else:
        bot.send_message(message.chat.id,'📃 Введіть ПІБ')
@bot.message_handler(func=lambda message: wait_fullname+2==message.message_id, content_types=['text'])
def get_order(message):
    global wait_phone
    wait_phone = message.message_id
    global fullname
    fullname = message.text
    bot.send_message(message.chat.id,'📃 Введіть номер телефону')
@bot.message_handler(func=lambda message: wait_phone+2==message.message_id, content_types=['text'])
def get_order(message):
    global phone
    phone = message.text
    inline_murkup = telebot.types.InlineKeyboardMarkup(row_width=2)
    item1 = telebot.types.InlineKeyboardButton('Нова Пошта', callback_data ='novaposhta')
    item2 = telebot.types.InlineKeyboardButton('Укрпошта', callback_data ='ukrposhta')
    inline_murkup.add(item1,item2)
    bot.send_message(message.chat.id,'📃 Виберіть поштовий сервіс', reply_markup=inline_murkup)
@bot.callback_query_handler(func = lambda call: True)
def get_order(call):
    global wait_adress
    wait_adress = call.message.message_id
    global delivery
    if call.message:
        if call.data == 'novaposhta':
            delivery = 'Нова Пошта'
            bot.send_message(call.message.chat.id,'📃 Введіть адресу вашого відділення')
        elif call.data == 'ukrposhta':
            delivery = 'Укрпошта'
            bot.send_message(call.message.chat.id,'📃 Введіть адресу вашого відділення')
        elif call.data == 'successfull':
            bot.send_message(call.message.chat.id,'✅ Замовлення підтверджено')
        elif call.data == 'unsuccessfull':
            bot.send_message(call.message.chat.id,'❌ Замовлення відмінено')
@bot.message_handler(func=lambda message: wait_adress+2==message.message_id, content_types=['text'])
def get_order(message):
    global adress
    adress = message.text
    inline_admin_markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    item1 = telebot.types.InlineKeyboardButton('✅ Підтвердити', callback_data ='successfull')
    item2 = telebot.types.InlineKeyboardButton('❌ Відмінити', callback_data ='unsuccessfull')
    inline_admin_markup.add(item1,item2)
    bot.send_message(917236708,f'Username: @{username}\nGoods: {goods}\nCount: {count}\nFullname: {fullname}\nPhone: {phone}\nDelivery: {delivery}\nAdress: {adress}',reply_markup=inline_admin_markup)
    bot.send_message(message.chat.id,'✅ Замовлення зареєстровано, після обробки вам напише наш менеджер')
@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text=='💨 Elf Bar Classic 1500':
        markup = telebot.types.ReplyKeyboardMarkup(True)
        buy = telebot.types.KeyboardButton('💵 Купити')
        back = telebot.types.KeyboardButton('↩️ Назад')
        markup.add(buy,back)
        elf_bar_text = ''
        row_count = 0
        for i in goods_name:
            if row_count < 7:
                elf_bar_text = f'{elf_bar_text}\n{i} - {goods_name[i]} шт.'
            row_count += 1
        bot.send_message(message.chat.id,elf_bar_text,reply_markup=markup)
    elif message.text=='💨 ELF BAR Lux 1500':
        markup = telebot.types.ReplyKeyboardMarkup(True)
        buy = telebot.types.KeyboardButton('💸 Купити')
        back = telebot.types.KeyboardButton('↩️ Назад')
        markup.add(buy,back)
        elf_bar_text = ''
        row_count = 0
        for i in goods_name:
            if row_count > 6:
                elf_bar_text = f'{elf_bar_text}\n{i} - {goods_name[i]} шт.'
            row_count += 1
        bot.send_message(message.chat.id,elf_bar_text,reply_markup=markup)
    elif message.text=='↩️ Назад':
        start(message)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)