import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.types import Message

from paws import *
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Nagaaaaaap", reply_markup=menu)

@dp.message(F.animation)
async def gif_id(message: Message):
    await message.reply(f"GIF ID: {message.animation.file_id}")


# langs
@dp.callback_query(F.data == 'lang')
async def langs(callback: CallbackQuery):
    await callback.message.edit_text("Yo'nalish tanlang: ", reply_markup=inline_langs)

# OS
@dp.callback_query(F.data == 'lang')
async def os(callback: CallbackQuery):
    await callback.message.edit_text("💻 Operatsion tizimlar uchun:", reply_markup=os_buttons)

# C
@dp.callback_query(F.data == 'c')
async def c(callback: CallbackQuery):
    await callback.message.edit_text(
        "C dasturlash tili 1972-yilda Dennis Ritchie tomonidan yaratilgan. "
        "U operatsion tizimlar, kompilyatorlar va mikrokontrollerlarda keng qo‘llaniladi.\n"
        "C juda tez va samarali, past darajadagi xotira boshqaruvi imkonini beradi. "
        "Ko‘plab zamonaviy tillar, masalan C++, Java va C# aynan undan rivojlangan. "
        "Biroq avtomatik xotira boshqaruvi yo‘qligi va murakkab sintaksisi sababli boshlovchilar uchun qiyin hisoblanadi.",
        reply_markup=os_back
    )

# C++
@dp.callback_query(F.data == 'cpp')
async def cpp(callback: CallbackQuery):
    await callback.message.edit_text(
        "C++ dasturlash tili 1983-yilda Bjarne Stroustrup tomonidan C tiliga asoslanib yaratilgan. "
        "U tezkor va samarali bo‘lib, tizim dasturlash, o‘yinlar, dasturiy ta’minot va grafikada keng qo‘llaniladi.\n"
        "C++ obyektga yo‘naltirilgan dasturlashni qo‘llab-quvvatlaydi, shu sababli katta loyihalarda juda qulay. "
        "Afzalliklari — tezlik va kuchli imkoniyatlar, kamchiligi esa murakkab sintaksis va yuqori o‘rganish chizig‘idir.",
        reply_markup=os_back
    )

# Rust
@dp.callback_query(F.data == 'rust')
async def rust(callback: CallbackQuery):
    await callback.message.edit_text(
        "Rust 2010-yilda Mozilla kompaniyasi tomonidan yaratilgan. "
        "U xavfsizlik, tezlik va parallel ishlashga katta e’tibor qaratadi.\n"
        "Rust xotira xatolarini kamaytiradi va avtomatik boshqaradi, shu bilan birga juda tez ishlaydi. "
        "Asosan tizim dasturlash, xavfsizlik va veb-serverlarda qo‘llaniladi. "
        "Afzalligi — xavfsizlik va tezlik, kamchiligi esa murakkab sintaksis va o‘rganish qiyinligidir.",
        reply_markup=os_back
    )

# Go
@dp.callback_query(F.data == 'go')
async def go(callback: CallbackQuery):
    await callback.message.edit_text(
        "Go dasturlash tili 2009-yilda Google tomonidan ishlab chiqilgan. "
        "U soddalik, tezlik va samaradorlikni birlashtiradi.\n"
        "Go asosan veb-serverlar, bulutli xizmatlar va katta tizimlarda ishlatiladi. "
        "Sintaksisi oson, kompilyatsiya tez, va ichki parallel ishlash imkoniyati kuchli. "
        "Afzalliklari — samaradorlik va oson o‘rganish, kamchiligi esa ba’zi zamonaviy funksiyalarning yetishmasligidir.",
        reply_markup=os_back
    )

# Assembly
@dp.callback_query(F.data == 'assembly')
async def assembly(callback: CallbackQuery):
    await callback.message.edit_text(
        "Assembly dasturlash tili eng past darajadagi tillardan biri bo‘lib, "
        "kompyuter protsessori tushunadigan mashina kodiga juda yaqin.\n"
        "U juda tez va samarali, ammo yozilishi va o‘qilishi murakkab. "
        "Assembly asosan operatsion tizimlar, drayverlar, mikrokontrollerlar va resurs cheklangan qurilmalarda ishlatiladi. "
        "Afzalligi — to‘liq nazorat va maksimal tezlik, kamchiligi esa murakkablik va platformaga bog‘liqligidir.",
        reply_markup=os_back
    )

# Swift
@dp.callback_query(F.data == 'swift')
async def swift(callback: CallbackQuery):
    await callback.message.edit_text(
        "Swift dasturlash tili 2014-yilda Apple tomonidan yaratilgan bo‘lib, "
        "asosan iOS, macOS va boshqa Apple platformalari uchun mo‘ljallangan. "
        "U xavfsiz, tez va zamonaviy sintaksisga ega.\n"
        "Swift o‘qilishi va yozilishi sodda, shu sababli yangi dasturchilar uchun ham qulay. "
        "Asosan mobil ilovalar va Apple ekotizimidagi dasturlarda qo‘llaniladi. "
        "Afzalligi — xavfsizlik va qulaylik, kamchiligi esa faqat Apple tizimlariga cheklanganligidir.",
        reply_markup=os_back
    )
# ==========WEB============

@dp.callback_query(F.data == 'web')
async def web(callback: CallbackQuery):
    await callback.message.edit_text("🌐 Websaytlar uchun:", reply_markup=web_buttons)

# 🌐 Web tillari

# 🌐 Web tillari

@dp.callback_query(F.data == 'web_py')
async def web_py(callback: CallbackQuery):
    await callback.message.edit_text(
        "Python dasturlash tili 1991-yilda Guido van Rossum tomonidan yaratilgan. "
        "U soddaligi, o‘qilishi va keng kutubxonalar to‘plami bilan mashhur. "
        "Python veb dasturlash, sun’iy intellekt, ma’lumotlar tahlili, avtomatlashtirish va ko‘plab boshqa sohalarda qo‘llaniladi. "
        "Afzalligi — oson o‘rganish va katta hamjamiyat, kamchiligi esa tezlikning pastligi va resurs talabchanligidir.",
        reply_markup=web_back
    )

@dp.callback_query(F.data == 'web_js')
async def web_js(callback: CallbackQuery):
    await callback.message.edit_text(
        "JavaScript dasturlash tili 1995-yilda Brendan Eich tomonidan yaratilgan. "
        "U asosan veb-sahifalarga interaktivlik qo‘shish uchun ishlatiladi. "
        "Hozirda JavaScript frontend (React, Vue, Angular) va backend (Node.js) dasturlashda keng qo‘llaniladi. "
        "Afzalligi — brauzerda to‘g‘ridan-to‘g‘ri ishlashi va katta ekotizim, kamchiligi esa murakkablik va turli brauzer muvofiqlik muammolaridir.",
        reply_markup=web_back
    )

@dp.callback_query(F.data == 'web_ts')
async def web_ts(callback: CallbackQuery):
    await callback.message.edit_text(
        "TypeScript dasturlash tili 2012-yilda Microsoft tomonidan ishlab chiqilgan. "
        "U JavaScript’ning kuchaytirilgan versiyasi bo‘lib, unga statik tiplash imkoniyatini qo‘shadi. "
        "TypeScript yirik loyihalarda xatolarni kamaytirish va kodni tartibli saqlashga yordam beradi. "
        "Afzalligi — kuchli tip nazorati, kamchiligi esa qo‘shimcha kompilyatsiya bosqichidir.",
        reply_markup=web_back
    )

@dp.callback_query(F.data == 'web_php')
async def web_php(callback: CallbackQuery):
    await callback.message.edit_text(
        "PHP dasturlash tili 1995-yilda Rasmus Lerdorf tomonidan yaratilgan. "
        "U asosan dinamik veb-saytlar va server tomonida ishlaydigan dasturlar yaratishda qo‘llaniladi. "
        "PHP oson sintaksisga ega va WordPress, Laravel kabi mashhur tizimlar asosida ishlaydi. "
        "Afzalligi — keng qo‘llanilishi va ko‘plab tayyor vositalar, kamchiligi esa zamonaviy tillarga qaraganda sekinroq ishlashi va xavfsizlikka ko‘proq e’tibor talab qilinishidir.",
        reply_markup=web_back
    )

@dp.callback_query(F.data == 'web_ruby')
async def web_ruby(callback: CallbackQuery):
    await callback.message.edit_text(
        "Ruby dasturlash tili 1995-yilda Yukihiro Matsumoto tomonidan yaratilgan. "
        "U soddaligi va o‘qilishi qulay sintaksisi bilan mashhur. "
        "Ruby ko‘pincha veb dasturlashda, ayniqsa Ruby on Rails freymvorki orqali keng qo‘llaniladi. "
        "Afzalligi — ishlab chiqishni tezlashtirishi va dasturchiga qulaylik yaratishi, kamchiligi esa sekinroq ishlashi va katta loyihalarda samaradorlik muammolari bo‘lishidir.",
        reply_markup=web_back
    )

@dp.callback_query(F.data == 'web_java')
async def web_java(callback: CallbackQuery):
    await callback.message.edit_text(
        "Java dasturlash tili 1995-yilda Sun Microsystems tomonidan yaratilgan. "
        "U ko‘p platformali va keng qo‘llaniladigan til bo‘lib, veb ilovalar, Android dasturlari va katta tizimlarda ishlatiladi. "
        "Afzalligi — barqarorlik va kuchli ekotizim, kamchiligi esa sekinroq ishlashi va sintaksisining murakkabligidir.",
        reply_markup=web_back
    )

@dp.callback_query(F.data == 'web_cs')
async def web_cs(callback: CallbackQuery):
    await callback.message.edit_text(
        "C# dasturlash tili Microsoft tomonidan yaratilgan bo‘lib, asosan .NET platformasida qo‘llaniladi. "
        "U veb ilovalar, o‘yinlar (Unity orqali) va korporativ dasturlar yaratishda keng ishlatiladi. "
        "Afzalligi — kuchli integratsiya va keng imkoniyatlar, kamchiligi esa asosan Microsoft ekotizimiga bog‘liqdir.",
        reply_markup=web_back
    )

@dp.callback_query(F.data == 'web_kot')
async def web_kot(callback: CallbackQuery):
    await callback.message.edit_text(
        "Kotlin dasturlash tili 2011-yilda JetBrains tomonidan ishlab chiqilgan. "
        "U Java bilan to‘liq mos keladi va Android dasturlashda keng qo‘llaniladi. "
        "Kotlin sintaksisi oddiy va ixcham bo‘lib, dasturchilar uchun qulaylik yaratadi. "
        "Afzalligi — soddalik va xavfsizlik, kamchiligi esa Java’ga qaraganda kichikroq hamjamiyatga ega ekanligidir.",
        reply_markup=web_back
    )

# ==========SECURITY============



@dp.callback_query(F.data == 'security')
async def security(callback: CallbackQuery):
    await callback.message.edit_text("🔒 Xavfsizlik uchun:", reply_markup=security_buttons)



@dp.callback_query(F.data == 'py')
async def sec_python(callback: CallbackQuery):
    await callback.message.edit_text(
        "Python xavfsizlik sohasida juda mashhur til. "
        "U penetration testing, exploit yozish va avtomatlashtirishda keng qo‘llaniladi. "
        "Ko‘plab xavfsizlik kutubxonalari mavjud (masalan, Scapy, Impacket). "
        "Afzalligi — soddalik va boy kutubxonalar, kamchiligi esa tezlikning pastligidir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'c')
async def sec_c(callback: CallbackQuery):
    await callback.message.edit_text(
        "C tili xavfsizlikda juda muhim, chunki u operatsion tizimlar va past darajadagi dasturlarni yaratishda ishlatiladi. "
        "Ko‘plab ekspluatatsiyalar va xakerlik vositalari C tilida yozilgan. "
        "Afzalligi — tezlik va to‘liq nazorat, kamchiligi esa murakkab sintaksisdir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'cpp')
async def sec_cpp(callback: CallbackQuery):
    await callback.message.edit_text(
        "C++ xavfsizlikda kuchli vosita hisoblanadi. "
        "U katta hajmdagi dasturlar va ekspluatatsiyalar yozishda qo‘llaniladi. "
        "Afzalligi — obyektga yo‘naltirilgan imkoniyatlar va tezlik, kamchiligi esa murakkabligi.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'go')
async def sec_go(callback: CallbackQuery):
    await callback.message.edit_text(
        "Go (Golang) xavfsizlik va tarmoqlar sohasida tez sur’atlarda rivojlanmoqda. "
        "Uning parallel ishlash imkoniyatlari skanerlash, server va tarmoqli dasturlar uchun qulay. "
        "Afzalligi — samaradorlik va soddalik, kamchiligi esa kichikroq hamjamiyatdir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'rust')
async def sec_rust(callback: CallbackQuery):
    await callback.message.edit_text(
        "Rust xavfsizlikda xotira xatolaridan xoli bo‘lishi bilan mashhur. "
        "U xavfsiz tizimlar, kriptografiya va ishonchli dasturlar yaratishda qo‘llaniladi. "
        "Afzalligi — xavfsizlik va tezlik, kamchiligi esa murakkab sintaksisdir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'perl')
async def sec_perl(callback: CallbackQuery):
    await callback.message.edit_text(
        "Perl dasturlash tili xavfsizlik va tizim boshqaruvida ishlatiladi. "
        "Ko‘plab eski xavfsizlik skriptlari va ekspluatatsiyalar Perl’da yozilgan. "
        "Afzalligi — matn bilan ishlashdagi kuchli imkoniyatlari, kamchiligi esa zamonaviy loyihalarda kam qo‘llanilishidir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'ruby')
async def sec_ruby(callback: CallbackQuery):
    await callback.message.edit_text(
        "Ruby xavfsizlikda asosan Metasploit Framework orqali mashhur. "
        "Metasploit — eng mashhur ekspluatatsiya vositalaridan biri bo‘lib, Ruby’da yozilgan. "
        "Afzalligi — qulaylik va xavfsizlik vositalari, kamchiligi esa resurs ko‘p sarflanishi va sekin ishlashidir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'asm')
async def sec_asm(callback: CallbackQuery):
    await callback.message.edit_text(
        "Assembly xavfsizlikda ekspluatatsiyalar yozish, shellcode yaratish va past darajadagi xakerlik amaliyotlarida qo‘llaniladi. "
        "Afzalligi — to‘liq nazorat va maksimal samaradorlik, kamchiligi esa murakkablik va platformaga bog‘liqligidir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'bash')
async def sec_bash(callback: CallbackQuery):
    await callback.message.edit_text(
        "Bash xavfsizlikda skriptlar, avtomatlashtirish va tizim boshqaruvida keng ishlatiladi. "
        "Pentest jarayonlarida tezkor buyruqlar va avtomatik hujum skriptlari yozish uchun qulay. "
        "Afzalligi — oson va tezkor ishlash, kamchiligi esa murakkab loyihalarda yetarli emasligidir.",
        reply_markup=security_back
    )

@dp.callback_query(F.data == 'ps')
async def sec_powershell(callback: CallbackQuery):
    await callback.message.edit_text(
        "PowerShell xavfsizlikda asosan Windows tizimlarida ishlatiladi. "
        "U administrator buyruqlarini bajarish, ekspluatatsiyalar va avtomatlashtirishda qo‘llaniladi. "
        "Afzalligi — Windows bilan kuchli integratsiya, kamchiligi esa faqat Windows muhitida samarali ishlashidir.",
        reply_markup=security_back
    )

# =========ANDROID===========

@dp.callback_query(F.data == 'android')
async def android(callback: CallbackQuery):
    await callback.message.edit_text("📱 Android uchun:", reply_markup=android_buttons)


@dp.callback_query(F.data == 'android_java')
async def android_java(callback: CallbackQuery):
    await callback.message.edit_text(
        "Java Android dasturlashda eng asosiy tillardan biridir. "
        "U 1995-yilda Sun Microsystems tomonidan yaratilgan va Android SDK bilan to‘liq ishlaydi. "
        "Afzalligi — keng qo‘llanilish va barqarorlik, kamchiligi esa sintaksisining uzun va biroz murakkabligidir.",
        reply_markup=android_back
    )

@dp.callback_query(F.data == 'android_kotlin')
async def android_kotlin(callback: CallbackQuery):
    await callback.message.edit_text(
        "Kotlin 2011-yilda JetBrains tomonidan ishlab chiqilgan. "
        "U Android uchun rasmiy til sifatida tan olingan va Java bilan to‘liq mos keladi. "
        "Afzalligi — ixcham sintaksis va xavfsizlik, kamchiligi esa Java’ga nisbatan kichikroq hamjamiyatdir.",
        reply_markup=android_back
    )

@dp.callback_query(F.data == 'android_cpp')
async def android_cpp(callback: CallbackQuery):
    await callback.message.edit_text(
        "C++ Android dasturlarida asosan NDK orqali qo‘llaniladi. "
        "U yuqori unumdorlik talab qilinadigan o‘yinlar va tizim dasturlarida ishlatiladi. "
        "Afzalligi — tezlik va samaradorlik, kamchiligi esa murakkab sintaksis va o‘rganish chizig‘idir.",
        reply_markup=android_back
    )

@dp.callback_query(F.data == 'android_dart')
async def android_dart(callback: CallbackQuery):
    await callback.message.edit_text(
        "Dart dasturlash tili Google tomonidan ishlab chiqilgan bo‘lib, Flutter freymvorki orqali mashhur bo‘lgan. "
        "U bitta kod bazasi bilan Android va iOS uchun dastur yaratishga imkon beradi. "
        "Afzalligi — tez ishlab chiqish va multiplatforma imkoniyati, kamchiligi esa kichikroq hamjamiyatdir.",
        reply_markup=android_back
    )

@dp.callback_query(F.data == 'android_cs')
async def android_cs(callback: CallbackQuery):
    await callback.message.edit_text(
        "C# Android uchun Xamarin platformasi orqali qo‘llaniladi. "
        "U Microsoft ekotizimi bilan integratsiyalashgan va kross-platforma ilovalar yaratishga imkon beradi. "
        "Afzalligi — .NET imkoniyatlari, kamchiligi esa ishlash tezligi va og‘irligi.",
        reply_markup=android_back
    )

@dp.callback_query(F.data == 'android_py')
async def android_py(callback: CallbackQuery):
    await callback.message.edit_text(
        "Python Android dasturlashda keng tarqalgan emas, ammo Kivy, BeeWare kabi freymvorklar orqali foydalanish mumkin. "
        "Afzalligi — soddalik va oson o‘rganish, kamchiligi esa rasmiy qo‘llab-quvvatlashning yo‘qligi va samaradorlik muammolaridir.",
        reply_markup=android_back
    )

# ===========IOS============

@dp.callback_query(F.data == 'ios')
async def ios(callback: CallbackQuery):
    await callback.message.edit_text("🍏 iOS uchun:", reply_markup=ios_buttons)

@dp.callback_query(F.data == 'ios_swift')
async def ios_swift(callback: CallbackQuery):
    await callback.message.edit_text(
        "Swift dasturlash tili 2014-yilda Apple tomonidan yaratilgan bo‘lib, asosan iOS, macOS va boshqa Apple platformalari uchun mo‘ljallangan. "
        "U xavfsiz, tez va zamonaviy sintaksisga ega. "
        "Swift o‘qilishi va yozilishi sodda, shu sababli yangi dasturchilar uchun ham qulay. "
        "Afzalligi — xavfsizlik va qulaylik, kamchiligi esa faqat Apple tizimlariga cheklanganligidir.",
        reply_markup=ios_back
    )

@dp.callback_query(F.data == 'ios_objc')
async def ios_objc(callback: CallbackQuery):
    await callback.message.edit_text(
        "Objective-C dasturlash tili Apple tomonidan iOS va macOS uchun uzoq vaqt davomida asosiy til bo‘lib kelgan. "
        "U C tiliga asoslangan va obyektga yo‘naltirilgan dasturlash imkoniyatlarini qo‘shadi. "
        "Afzalligi — kuchli barqarorlik va katta kutubxonalar, kamchiligi esa sintaksisining murakkabligi va Swiftga nisbatan kamroq qulaylikdir.",
        reply_markup=ios_back
    )

@dp.callback_query(F.data == 'ios_cpp')
async def ios_cpp(callback: CallbackQuery):
    await callback.message.edit_text(
        "C++ iOS dasturlashda yuqori unumdorlikka ega komponentlar va o‘yinlar yaratishda qo‘llaniladi. "
        "U tezligi va samaradorligi tufayli grafik tizimlarda keng ishlatiladi. "
        "Afzalligi — maksimal tezlik va kuchli imkoniyatlar, kamchiligi esa murakkab sintaksis va o‘rganish chizig‘idir.",
        reply_markup=ios_back
    )

@dp.callback_query(F.data == 'ios_dart')
async def ios_dart(callback: CallbackQuery):
    await callback.message.edit_text(
        "Dart dasturlash tili Google tomonidan ishlab chiqilgan bo‘lib, Flutter freymvorki orqali mashhur bo‘lgan. "
        "U bitta kod bazasi bilan iOS va Android uchun dastur yaratishga imkon beradi. "
        "Afzalligi — multiplatforma imkoniyati va tez ishlab chiqish, kamchiligi esa kichikroq hamjamiyatdir.",
        reply_markup=ios_back
    )

@dp.callback_query(F.data == 'ios_cs')
async def ios_cs(callback: CallbackQuery):
    await callback.message.edit_text(
        "C# iOS dasturlarini Xamarin platformasi orqali ishlab chiqishda qo‘llaniladi. "
        "U kross-platforma ilovalar yaratishga imkon beradi va .NET imkoniyatlaridan foydalanadi. "
        "Afzalligi — Microsoft ekotizimi bilan integratsiya, kamchiligi esa og‘irlik va ishlash tezligi pastroq bo‘lishidir.",
        reply_markup=ios_back
    )

@dp.callback_query(F.data == 'ios_py')
async def ios_py(callback: CallbackQuery):
    await callback.message.edit_text(
        "Python iOS dasturlash uchun rasmiy til emas, lekin Kivy, BeeWare kabi freymvorklar orqali qo‘llanilishi mumkin. "
        "Afzalligi — oson o‘rganish va soddalik, kamchiligi esa cheklangan qo‘llab-quvvatlash va samaradorlik muammolaridir.",
        reply_markup=ios_back
    )

# ============GAME================

@dp.callback_query(F.data == 'game')
async def game(callback: CallbackQuery):
    await callback.message.edit_text("🎮 O‘yin yaratish uchun:", reply_markup=game_buttons)

@dp.callback_query(F.data == 'game_cpp')
async def game_cpp(callback: CallbackQuery):
    await callback.message.edit_text(
        "C++ Unreal Engine orqali o‘yin yaratishda eng ko‘p qo‘llaniladigan tillardan biridir. "
        "U yuqori tezlik, kuchli grafika imkoniyatlari va murakkab o‘yin mexanikalarini yaratishda ishlatiladi. "
        "Afzalligi — maksimal samaradorlik, kamchiligi esa murakkab sintaksis va o‘rganish chizig‘idir.",
        reply_markup=game_back
    )

@dp.callback_query(F.data == 'game_cs')
async def game_cs(callback: CallbackQuery):
    await callback.message.edit_text(
        "C# Unity o‘yin dvigateli orqali keng qo‘llaniladi. "
        "U 2D va 3D o‘yinlar yaratishda juda qulay va oson o‘rganiladi. "
        "Afzalligi — Unity ekotizimi va tez ishlab chiqish, kamchiligi esa resurs talabchanligi.",
        reply_markup=game_back
    )

@dp.callback_query(F.data == 'game_rust')
async def game_rust(callback: CallbackQuery):
    await callback.message.edit_text(
        "Rust yangi va xavfsiz til sifatida o‘yin dvigatellari va grafik tizimlarda qo‘llanila boshlagan. "
        "U tezligi va xotira xavfsizligi bilan ajralib turadi. "
        "Afzalligi — xavfsizlik va samaradorlik, kamchiligi esa kichikroq hamjamiyat va kamroq tayyor kutubxonalar.",
        reply_markup=game_back
    )

@dp.callback_query(F.data == 'game_java')
async def game_java(callback: CallbackQuery):
    await callback.message.edit_text(
        "Java mobil o‘yinlar (Android) va ayrim desktop o‘yinlarda qo‘llaniladi. "
        "Minecraft kabi mashhur o‘yinlar ham Java’da yozilgan. "
        "Afzalligi — kross-platforma imkoniyati, kamchiligi esa pastroq unumdorlik.",
        reply_markup=game_back
    )

@dp.callback_query(F.data == 'game_lua')
async def game_lua(callback: CallbackQuery):
    await callback.message.edit_text(
        "Lua ssenariy tili sifatida o‘yin dvigatellarida keng qo‘llaniladi. "
        "Roblox va World of Warcraft kabi o‘yinlarda scripting uchun ishlatiladi. "
        "Afzalligi — yengillik va tezlik, kamchiligi esa to‘liq funksional til sifatida imkoniyatlari cheklangan.",
        reply_markup=game_back
    )

@dp.callback_query(F.data == 'game_js')
async def game_js(callback: CallbackQuery):
    await callback.message.edit_text(
        "JavaScript va TypeScript asosan brauzer o‘yinlari va WebGL asosidagi loyihalarda qo‘llaniladi. "
        "Phaser, Babylon.js, Three.js kabi kutubxonalar bilan ishlatiladi. "
        "Afzalligi — veb asosida o‘yin yaratish imkoniyati, kamchiligi esa resurs talabchanligi va cheklangan unumdorlikdir.",
        reply_markup=game_back
    )

@dp.callback_query(F.data == 'own')
async def own(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌐 Mening sahifalarim:",
        reply_markup=own_buttons
    )


# Main loop
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur to'xtadi!")
