import TelegramBot


def test_send_msg():
    try:
        bot = TelegramBot.TelegramBot()
        bot.send_msg("test")
    except:
        assert False


def test_get_updates():
    try:
        bot = TelegramBot.TelegramBot()
        updates = bot.get_updates()
        for u in updates:
            # print(u.effective_user)
            print(f"{u.message.chat.username} : {u.message.chat.id}")
    except:
        assert False


if __name__ == "__main__":
    test_send_msg()
    test_get_updates()
    print("All tests passed")

a = {'update_id': 867764368, 'message': {'new_chat_photo': [], 'delete_chat_photo': False, 'photo': [], 'new_chat_members': [], 'group_chat_created': False, 'chat': {'last_name': 'Mousaei', 'first_name': 'Iman', 'username': 'ImanMousaei', 'type': 'private', 'id': 968197748}, 'text': 'hello iman',
                                         'caption_entities': [], 'date': 1647174135, 'message_id': 6, 'supergroup_chat_created': False, 'entities': [], 'channel_chat_created': False, 'from': {'first_name': 'Iman', 'language_code': 'en', 'id': 968197748, 'username': 'ImanMousaei', 'is_bot': False, 'last_name': 'Mousaei'}}}
