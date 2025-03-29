from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"Premium Benefits & Perks\nDirect Channel Links, No Ad Links\nSpecial Access In Events\n\n<blockquote>Pricing Rates\n1 Month - INR 50\n3 Months - INR 130\n6 Months - INR 250\n12 Month - Contact <a href=https://t.me/Mr_G0han>Owner</a></blockquote>\n\n<blockquote>Buy Now\n<a href=https://t.me/Mr_G0han>𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲 𝗧𝗼 𝗕𝘂𝘆</a></blockquote>\n\nWe Have Limited Seats For Premium Users",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝗕𝘂𝘆 𝗣𝗿𝗲𝗺𝗶𝘂𝗺", url="https://t.me/Mr_G0han"),
                        InlineKeyboardButton("All Channels", url="https://t.me/Entertainment_Yoddha")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass