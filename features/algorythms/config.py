class Config():
    table_locator = "//div[contains(@class, 'rival')]//div[@data-x='%s' and @data-y='%s']"
    status_addition = "/.."
    opponent_field_locator = "//div[contains(@class, 'battlefield__rival')]"
    timeout = 15
    win_game_string = "Игра закончена. Поздравляем, вы победили!"
    notification_method_locator = "//div[@class='notifications']/div[not(contains(@class, 'none'))]/div[@class='notification-message']"
    max_attempts = 10
    wait_status = "battlefield__wait"
    wait_your_turn_message = "Противник ходит, ждите."
    your_turn_message = "Ваш ход."
    wait_start_game_your_turn_message = "Игра началась, ваш ход."
    wait_start_game_opponent_turn_message = "Игра началась, противник ходит."
    wait_for_opponent_message = "Ожидаем противника."
    battleship_url = "http://ru.battleship-game.org/"
    main_title_locator = "//h1[@class='logo']"
    main_title = "Морской бой"
    place_ships_button_locator = "//li[contains(@class, 'variant__randomly')]/span"
    start_button = "//div[@class='battlefield-start-button']"
    heigh = 10
    width = 10
