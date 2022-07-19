from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

SUPPORT_LINK = 'https://t.me/Yanamsf_help_bot'  # Change it to your link

activation_keyboard = InlineKeyboardMarkup(row_width=2,
                                           inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(text='Activation', callback_data='Activation'),

                                                   InlineKeyboardButton(text='Support',
                                                                        url=SUPPORT_LINK)
                                               ]
                                           ]
                                           )

renew_keyboard = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Renew Sub', callback_data='Renew'),

                                              InlineKeyboardButton(text='Support',
                                                                   url=SUPPORT_LINK)
                                          ]
                                      ]
                                      )
