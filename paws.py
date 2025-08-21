from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

menu = InlineKeyboardMarkup(inline_keyboard= [
    [
        InlineKeyboardButton(text="Tillar", callback_data="lang")
    ],
    [
        InlineKeyboardButton(text="Ega", callback_data="own")
    ]
])

own_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Instagram", url="https://instagram.com/iskandarvx7"), 
        InlineKeyboardButton(text="Telegram", url="https://t.me/mkingboi")],
        [
        InlineKeyboardButton(text="Github", url="https://github.com/odamboy01"),
        InlineKeyboardButton(text="Orqaga", callback_data="menu")
    ]
])
inline_langs = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Operatsion tizimlar uchun:", callback_data="os"),
    ],
    [
        InlineKeyboardButton(text="🌐 Websaytlar uchun:", callback_data="web")
    ],
    [
        InlineKeyboardButton(text="🔒 Xavfsizlik uchun:", callback_data="security")
    ],
    [
        InlineKeyboardButton(text="📱 Android uchun:", callback_data="android")
    ],
    [
        InlineKeyboardButton(text="🍏 iOS uchun:", callback_data="ios")
    ],
    [
        InlineKeyboardButton(text="🎮 O‘yin yaratish uchun:", callback_data="game")
    ],
    [
        InlineKeyboardButton(text="Orqaga", callback_data="lang")
    ]
])

os_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="C", callback_data="c"),
        InlineKeyboardButton(text="C++", callback_data="cpp"),
        InlineKeyboardButton(text="Rust", callback_data="rust")
    ],
    [
        InlineKeyboardButton(text="GO", callback_data="go"),
        InlineKeyboardButton(text="Assembly", callback_data="assembly"),
        InlineKeyboardButton(text="swift", callback_data="swift"), 
    ],
    [
        InlineKeyboardButton(text="Orqaga", callback_data="lang")
    ]
])

web_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Python", callback_data="web_py"),
        InlineKeyboardButton(text="JavaScript", callback_data="web_js"),
        InlineKeyboardButton(text="TypeScript", callback_data="web_ts"),
        InlineKeyboardButton(text="PHP", callback_data="web_php")],
        [
        InlineKeyboardButton(text="Ruby", callback_data="web_ruby"),
        InlineKeyboardButton(text="Java", callback_data="web_java"),
        InlineKeyboardButton(text="C#", callback_data="web_cs"),
        InlineKeyboardButton(text="Kotlin", callback_data="web_kot")
    ]
])


security_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Python", callback_data="py"),
        InlineKeyboardButton(text="C", callback_data="c"),
        InlineKeyboardButton(text="C++", callback_data="cpp"),
        InlineKeyboardButton(text="Go", callback_data="go"),
        InlineKeyboardButton(text="Rust", callback_data="rust")],
        [
        InlineKeyboardButton(text="Perl", callback_data="perl"),
        InlineKeyboardButton(text="Ruby", callback_data="ruby"),
        InlineKeyboardButton(text="Assembly", callback_data="asm"),
        InlineKeyboardButton(text="Bash", callback_data="bash"),
        InlineKeyboardButton(text="PowerShell", callback_data="ps")
    ]
])

android_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Java", callback_data="android_java"),
        InlineKeyboardButton(text="Kotlin", callback_data="android_kotlin"),
        InlineKeyboardButton(text="C++", callback_data="android_cpp")
    ],
    [
        InlineKeyboardButton(text="Dart (Flutter)", callback_data="android_dart"),
        InlineKeyboardButton(text="C# (Xamarin)", callback_data="android_cs"),
        InlineKeyboardButton(text="Python", callback_data="android_py")
    ]
])


ios_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Swift", callback_data="ios_swift"),
        InlineKeyboardButton(text="Objective-C", callback_data="ios_objc"),
        InlineKeyboardButton(text="C++", callback_data="ios_cpp")
    ],
    [
        InlineKeyboardButton(text="Dart (Flutter)", callback_data="ios_dart"),
        InlineKeyboardButton(text="C# (Xamarin)", callback_data="ios_cs"),
        InlineKeyboardButton(text="Python", callback_data="ios_py")
    ]
])

game_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="C++ (Unreal Engine)", callback_data="game_cpp"),
        InlineKeyboardButton(text="C# (Unity)", callback_data="game_cs"),
        InlineKeyboardButton(text="Rust", callback_data="game_rust")],
        [
        InlineKeyboardButton(text="Java", callback_data="game_java"),
        InlineKeyboardButton(text="Lua", callback_data="game_lua"),
        InlineKeyboardButton(text="JavaScript / TypeScript", callback_data="game_js")
    ],
    [
        InlineKeyboardButton(text="Orqaga", callback_data="lang")
    ]
])



os_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Orqaga", callback_data="lang")
    
    ]
]
)

web_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Orqaga", callback_data="web")
    ]
])

security_back = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Orqaga", callback_data="security")
]
])

android_back = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Orqaga", callback_data="android")
]
])

ios_back = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Orqaga", callback_data="ios")
]
])

game_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Orqaga", callback_data="game")
    ]
])

own_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Orqaga", callback_data="lang")
    ]
])
