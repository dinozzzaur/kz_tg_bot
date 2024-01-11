from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN_API = "6463697146:AAEcL7z4G-VRLIsrlAEfYihSS6lv64HeZuM"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Жұма: бот жұмыс жасап тұр, мырзам!')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Kanka: керек менюді таңдау арқылы сұрағыңызға жауап ала аласыз\n",
                           reply_markup=kb)
    await message.delete()

#################################################################################
###############################  MENU  ########################################## 

@dp.message_handler(Text(equals="🚍 Транспорт"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="🚍 Транспорт", 
                           reply_markup=kb_transport)
    await message.delete()
    
@dp.message_handler(Text(equals="🏕 Үй & жатақхана"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="🏕 Үй & жатақхана", 
                           reply_markup=kb_ui)
    await message.delete()
     

@dp.message_handler(Text(equals="📞 Телефон & Интернет"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="📞 Телефон & Интернет", 
                           reply_markup=kb_telefon)
    await message.delete()

    
@dp.message_handler(Text(equals="🇹🇷 Ikamet"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="🇹🇷 Ikamet", 
                           reply_markup=kb_ikamet)
    await message.delete()
    

@dp.message_handler(Text(equals="📚 Tömer"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="📚 Tömer", 
                           reply_markup=kb_tomer)
    await message.delete()
 
 
@dp.message_handler(Text(equals="🗽 Университет & Факультет"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="🗽 Университет & Факультет", 
                           reply_markup=kb_univer)
    await message.delete()
    

@dp.message_handler(Text(equals="❓ Адрестер"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="❓ Адрестер", 
                           reply_markup=kb_surak)
    await message.delete()
    

@dp.message_handler(Text(equals="🧐 Ұсыныстар"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="🧐 Ұсыныстар", 
                           reply_markup=kb_usynus)
    await message.delete()   

@dp.message_handler(Text(equals="🦠 Sigorta"))
async def open_kb_transport(message: types.Message):
    await message.answer (text="🦠 Sigorta", 
                           reply_markup=kb_sigorta)
    await message.delete()  
    
@dp.message_handler(Text(equals="🏠 Басты мәзір"))
async def open_kb (message: types.Message):
    await message.answer (text=" 🏠 ", 
                          reply_markup=kb)
    await message.delete()
    
    
################################################################################# 
##############################  SUB-MENU  ####################################### 

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('🚍 Транспорт')
b2 = KeyboardButton('🏕 Үй & жатақхана')
b3 = KeyboardButton('📞 Телефон & Интернет')
b4 = KeyboardButton('🇹🇷 Ikamet')
b5 = KeyboardButton('📚 Tömer')
b6 = KeyboardButton('🗽 Университет & Факультет')
b7 = KeyboardButton('❓ Адрестер')
b8 = KeyboardButton('🧐 Ұсыныстар')
b9 = KeyboardButton('🦠 Sigorta')

kb.add(b1,b2,b3,b4,b5,b6,b7,b8,b9)

kb_transport = ReplyKeyboardMarkup(resize_keyboard=True)
tr1 = KeyboardButton(text="Tam Kart 43-ті қалай аламын?")
tr2 = KeyboardButton(text='Автобусқа билетті қалай аламын?')
tr3 = KeyboardButton(text='Поездға билетті қалай аламын?')
tr4 = KeyboardButton(text='Öğrenci Kart-ын қалай аламын?')
tr5 = KeyboardButton(text='🏠 Басты мәзір')

kb_transport.add(tr1,tr2,tr3,tr4,tr5)

kb_ui = ReplyKeyboardMarkup(resize_keyboard=True)
ui1 = KeyboardButton(text='Жалға берілетін үйлерді қалай тапсам болады?')
ui5 = KeyboardButton(text='🏠 Басты мәзір')

kb_ui.add(ui1,ui5)

kb_telefon = ReplyKeyboardMarkup(resize_keyboard=True)
tl1 = KeyboardButton(text='Телефонды қалай тіркей аламын?')
tl5 = KeyboardButton(text='🏠 Басты мәзір')

kb_telefon.add(tl1,tr5)

kb_ikamet = ReplyKeyboardMarkup(resize_keyboard=True)
ik1 = KeyboardButton(text='Икаметке (ВНЖ) қандай құжаттар керек?')
ik2 = KeyboardButton(text='Ikamet келмей жатыр не істесем болады?')
ik3 = KeyboardButton(text='Ikamet құжаттарын және "Parmak izin" қайда тапсырамын?')
ik4 = KeyboardButton(text='Ikamet - ті қай жерден алып кетсем болады?')
ik5 = KeyboardButton(text='Goç idaresi - не қандай автобус барады?')
ik7 = KeyboardButton(text='🏠 Басты мәзір')
                                    
kb_ikamet.add(ik1,ik2,ik3,ik4,ik4,ik5,ik7)

kb_tomer = ReplyKeyboardMarkup(resize_keyboard=True)
tm1 = KeyboardButton(text='Басқа қаланың TÖMER сертификаты жарамды ма?')
tm2 = KeyboardButton(text='🏠 Басты мәзір')

kb_tomer.add(tm1,tm2)

kb_univer = ReplyKeyboardMarkup(resize_keyboard=True)
un1 = KeyboardButton(text='Факультетке ақшаны қалай төлейміз?')
un2 = KeyboardButton(text='Денклик қалай жасатамын?')
un4 = KeyboardButton(text='Бөлімімді қалай ауыстырсам болады?')
un5 = KeyboardButton(text='🏠 Басты мәзір')
                      
kb_univer.add(un1,un2,un4,un5)

kb_surak = ReplyKeyboardMarkup(resize_keyboard=True)
su1 = KeyboardButton(text='Доллорды лираға қай жерде ауыстырсам болады?')
su2 = KeyboardButton(text='Milli egitim bakanligi яғни білім басқармасының адресі?')
su3 = KeyboardButton(text='Vergi dairesi яғни салық, әкімшілігінің адресі?')
su4 = KeyboardButton(text='İl Göç İdaresi - адресі?')
su5 = KeyboardButton(text='🏠 Басты мәзір')

kb_surak.add(su1,su2,su3,su4,su5)

kb_usynus = ReplyKeyboardMarkup(resize_keyboard=True)
us1 = KeyboardButton(text='Ұсыныстар немесе түзетулер бойынша @kanka_kz -ке жазыңыз)')
us5 = KeyboardButton(text='🏠 Басты мәзір')

kb_usynus.add(us1,us5)

kb_sigorta = ReplyKeyboardMarkup(resize_keyboard=True)
sg1 = KeyboardButton(text="Оnline “sigorta” алу")
#sg2 = KeyboardButton(text="Text") 
sg5 = KeyboardButton(text="🏠 Басты мәзір")

kb_sigorta.add(sg1,sg5)

#################################################################################
#############################  SURAK-JAUAP  ##################################### 

#####  sigorta  ##### NOT COMPLITED! JUST EXAMPLES

@dp.message_handler(Text(equals="Оnline “sigorta” алу"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_sg1, reply_markup=ikbsg1)
   
    
Text_sg1 = """
Төмендегі Google форманы толтырыңыз! 
Ескерту: 
1. WhatsApp  нөмеріңізді жазуды ұмытпаңыз, 
себебі  дайын болған “Sigorta” 1-2 жұмыс күн 
ішінде PDF форматта жіберіледі.""" # <<There we will understand what to do and how to do

#@dp.message_handler(Text(equals="Text"))
#async def open_kb_transport(message: types.Message):
#    await message.answer (text=Text_sg2)
#    
#Text_sg2 = "" # << Example

#####  transport  #####

@dp.message_handler(Text(equals="Tam Kart 43-ті қалай аламын?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_tr1)
    
    
Text_tr1= "Tam Kart 43 -ты қала ішіндегі дүкендерден алып, толтыра аласыз. 1 рет міну құны 11TL жане Tam Kart 43 -ты алу үшін құжат қажет емес."
                           
@dp.message_handler(Text(equals="Автобусқа билетті қалай аламын?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_tr2,reply_markup=ikbtr2)
    
    
Text_tr2="🔽 Автобусқа билетті төмендегі сілтеме арқылы алуыңызға болады 👇"
    
@dp.message_handler(Text(equals="Поездға билетті қалай аламын?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_tr3,reply_markup=ikbtr1)
    
    
Text_tr3="🔽 Поездға билетті төмендегі сілтеме арқылы алуыңызға болады 👇"

@dp.message_handler(Text(equals="Öğrenci Kart-ын қалай аламын?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_tr4,reply_markup=ikbtr4)
    
    
Text_tr4="""🔽 Керекті құжаттар тізімі:
- Öğrenci  belgesi
- 1 шт фото"""

#####  ui  #####

@dp.message_handler(Text(equals="Жалға берілетін үйлерді қалай тапсам болады?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_ui1,reply_markup=ikbui1)
    
    
Text_ui1="Үйді төмендегі сайттан немесе “emlakçı”  арқылы жалға ала аласыз."    

#####  telefon  #####

@dp.message_handler(Text(equals="Телефонды қалай тіркей аламын?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_tl1)
    

Text_tl1="""
Телефоныңызды тіркеу үшін: 
1. "Икамет белгиси" (ВНЖ)
2. IMEI нөмірі (*#06# теру арқылы біле аласыз)
3. Салық, әкімшілігіне (vergi dairesi) 20.000TL төлеу
4. РТТ-дан e-devlet пароль-і
5. Соңғысы телефонды тіркеу 

Тіркеу кұны қымбат болса, орталықтағы телефон жөндейтін
дүкендерде 200-300 лираға жаңа IMEI жасата аласыз.
(P.s. телефондағы барлық, мағлұматтан айырылу қаупі бар)""" 

#####  ikamet  #####

@dp.message_handler(Text(equals="Икаметке (ВНЖ) қандай құжаттар керек?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_ik1, reply_markup=ikbik1)
    
    
Text_ik1="""
- Ikamet (ВНЖ) бланкы толтырылып PDF форматында шығарылуы тиіс
- Паспорттың көшірмесі (өзіңіздің, суретіңіз болған жер мен соңғы кіріп шыққан жердің ксерокопиясы)
- Биометриялық, фото 4шт
- Тұратын жеріңізден анықтама
- Сақтандыру (страховка)
- Оқып жатқаныңыз туралы анықтама""" 

@dp.message_handler(Text(equals="Ikamet келмей жатыр не істесем болады?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_ik2, reply_markup=ikbik2)
    
    
Text_ik2="Сілтеме бойынша өтіп икаметтің қаралымдағы денгейін анықтай аласыз." 
    
@dp.message_handler(Text(equals='Ikamet құжаттарын және "Parmak izin" қайда тапсырамын?'))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_ik3, reply_markup=ikbik3)
    
    
Text_ik3="""Ең бірінші құжаттарды Tömer жанында тұрған Yabanci
Diller ішіндегі Göç idaresi-нің кішігірім офисына алып 
барамыз.Содан кейін екі апта уақыт өткеннен кейін төмендегі адрес бойынша барып саусақ, іздерін 
тапсырамыз.Болды, енді алдағы бір ай күтсеңіз қолыңызда Ikamet тұрады.""" 

@dp.message_handler(Text(equals="Ikamet - ті қай жерден алып кетсем болады?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_ik4, reply_markup=ikbik4)
     
    
Text_ik4="""Tөмендегі адрес бойынша барып,паспортыңызды 
көрсетіп алып кете аласыз.""" 

@dp.message_handler(Text(equals="Goç idaresi - не қандай автобус барады?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_ik5)
    
    
Text_ik5="""7А автобусы арқылы Otogar (Автовокзал)- ғa дейін жетіп, одан әрі
таксимен үнемдеймін десеңіз екі аяқпен жете аласыз""" 
    
#####  tomer  #####

@dp.message_handler(Text(equals="Басқа қаланың TÖMER сертификаты жарамды ма?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_tm1)
    
    
Text_tm1="""Өкінішке орай жарамды емес, Кютахья қаласындағы TÖMER - де кайтадан SBS
(деңгей анықтау емтиханы) емтиханын тапсыруыңыз қажет.""" 

#####  university  #####

@dp.message_handler(Text(equals="Факультетке ақшаны қалай төлейміз?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_un1)
    
    
Text_un1="""
Ziraat Bankasi банкоматында:
"Kartsız işlemler" >"Üniversite veya Eğitim
Ödemeler" >"Anlaşmalı Üniversiteler" >"IL Plaka kodu" >4 3 >"Öğrenci numarası"

Ziraat Bankası қосымшасында:
"Menü" >"Ödemeler" >"Egitim, Sınav ve Üniversiteler" > "Üniversite Harç ve Sınav
Ödemeleri" > "Kütahya DPU" >Ögrenci NO"""

@dp.message_handler(Text(equals="Денклик қалай жасатамын?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_un2)
     
    
Text_un2="""1. Аттестаттың нотариалды,
куәландырылған  аудармасы 
2. Аттестаттың түпнұсқасы
3. Аттестаттқа апостиль 
4. Ikamet (ВНЖ)
5. Паспорт көшірмесі
Denklik жайлы жалпылама ақпаратты осы жерден карай аласыз."""

@dp.message_handler(Text(equals="Бөлімімді қалай ауыстырсам болады?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_un4)
    
    
Text_un4="Бөліміңізді ауыстыру үшін @kanka_kz -ке жаза аласыз. Қалаған бөліміңізге ауысуға көмектеседі.🤗"


#####  suraqtar  #####

@dp.message_handler(Text(equals="Доллорды лираға қай жерде ауыстырсам болады?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_su1, reply_markup=ikbsu1)
     

Text_su1="Tөмендегі адрес бойынша барып ауыстыруға болады."

@dp.message_handler(Text(equals="Milli egitim bakanligi яғни білім басқармасының адресі?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_su2,reply_markup=ikbsu2)
    
    
Text_su2="Mili egitim bakanligi адресі"
    
@dp.message_handler(Text(equals="Vergi dairesi яғни салық, әкімшілігінің адресі?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_su3, reply_markup=ikbsu3)
    
Text_su3="Салық, әкімшілігінің адресі" 

@dp.message_handler(Text(equals="İl Göç İdaresi - адресі?"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_su4, reply_markup=ikbik3)
    

Text_su4="İl Göç İdaresi - адресі"


#####  usunustar  #####
    
@dp.message_handler(Text(equals="Ұсыныстар немесе түзетулер бойынша @kanka_kz -ке жазыңыз)"))
async def open_kb_transport(message: types.Message):
    await message.answer (text=Text_us1)
     
    
Text_us1="Ұсыныстар немесе түзетулер бойынша @kanka_kz -ке жазыңыз)"

#################################################################################
##########################  INLINE KEYBOARD  #################################### 

#####  transport  #####

ikbtr1 = InlineKeyboardMarkup(row_width=2)
iktr1 = InlineKeyboardButton(text='поезд билет',
                           url="https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")
ikbtr1.add(iktr1)

ikbtr2 = InlineKeyboardMarkup(row_width=2)
iktr2_1 = InlineKeyboardButton(text='автобус билет',
                           url="https://obilet.com")
ikbtr2.add(iktr2_1)

ikbtr4 = InlineKeyboardMarkup(row_width=2)
ikik4 = InlineKeyboardButton(text='Каrt 43 - адресі',
                             url="https://maps.app.goo.gl/rjFn2xiVAJ9b12d59")
ikbtr4.add(ikik4)

#####  ui  #####

ikbui1 = InlineKeyboardMarkup(row_width=2)
ikui1 = InlineKeyboardButton(text='sahibinden',
                             url="https://www.sahibinden.com/kiralik/kutahya")
ikbui1.add(ikui1)

#####  ikamet  #####

ikbik1 = InlineKeyboardMarkup(row_width=2)
ikik = InlineKeyboardButton(text='Ikamet бланкын толтыру',
                            url="https://e-ikamet.goc.gov.tr")
ikbik1.add(ikik)

ikbik2 = InlineKeyboardMarkup(row_width=2)
ikik2 = InlineKeyboardButton(text='Ikamet денгейін анықтау',
                               url="https://e-ikamet.goc.gov.tr/Ikamet/DevamEdenBasvuruGiris")
ikbik2.add(ikik2)

ikbik3 = InlineKeyboardMarkup(row_width=2)
ikik3 = InlineKeyboardButton(text='İl Göç İdaresi - адресі',
                               url="https://maps.app.goo.gl/yJej8ytV7TKyqEG26")
ikbik3.add(ikik3)

ikbik4 = InlineKeyboardMarkup(row_width=2)
ikik4 = InlineKeyboardButton(text='Ptt - адресі',
                             url="https://maps.app.goo.gl/HSV4XVfZeqbMNZ239")
ikbik4.add(ikik4)

#####  suraqtar  #####

ikbsu1 = InlineKeyboardMarkup(row_width=2)
iksu1 = InlineKeyboardButton(text='Ақша айырбастау пункт - адресі',
                             url="https://maps.app.goo.gl/wMBpnASthCD7ChDU6")
ikbsu1.add(iksu1)

ikbsu2 = InlineKeyboardMarkup(row_width=2)
iksu2 = InlineKeyboardButton(text='Mili egitim bakanligi - адресі',
                             url="https://maps.app.goo.gl/E8Wxkf9qpNhYhqbu5")
ikbsu2.add(iksu2)

ikbsu3 = InlineKeyboardMarkup(row_width=2)
iksu3 = InlineKeyboardButton(text='Салық, әкімшілігінің - адресі',
                             url="https://maps.app.goo.gl/RuQ3Mkf3LTLKQ1V98")
ikbsu3.add(iksu3)


#####  sigorta  #####

ikbsg1 = InlineKeyboardMarkup(row_width=2)
iksg1 = InlineKeyboardButton(text='online “sigorta” алу',
                             url="https://forms.gle/oUi2tS1SXddtMexk7")
ikbsg1.add(iksg1)

################################################################################# 
##################################  END  ######################################## 

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
    