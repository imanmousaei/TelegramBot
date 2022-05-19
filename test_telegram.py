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
