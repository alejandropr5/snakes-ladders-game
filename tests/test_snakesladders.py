from snakesladders.main import SnakesAndLadders


def test_game():
    sal = SnakesAndLadders()
    dice_vals = (1, 2, 5, 4, 2, 6)
    board_pos = (1, 11, 16, 20, 20, False)

    for val, pos in zip(dice_vals, board_pos):
        game_finished = sal.change_game_state(val)
        assert sal.new_abs_pos(0) and not game_finished == pos
