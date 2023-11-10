import pytest

from snakesladders.game import SnakesAndLadders


@pytest.mark.parametrize("dice_vals, board_pos",
                         [(1, 1), (2, 11), (5, 16), (4, 20), (2, 20), (6, 26)])
def test_move_method(dice_vals, board_pos, snakesladders_obj):
    snakesladders_obj.move(dice_vals)
    assert snakesladders_obj.pos == board_pos


def test_roll_dice_method():
    dice_val = SnakesAndLadders.roll_dice()
    assert dice_val >= 1 and dice_val <= 6


def test_exception(snakesladders_obj):
    with pytest.raises(AttributeError):
        snakesladders_obj.pos = 1
