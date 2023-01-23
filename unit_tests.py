from laba import read_all_lines

lines = read_all_lines()


def total_value_of_operation():
    total = 0
    for line in lines:
        if line[2] == "расход":
            total -= line[4]
        elif line[2] == "приход":
            total += line[4]
        else:
            return "Данные введены не корректны"
    return total


def test_unit():
    value = total_value_of_operation()
    assert value != 0, "Суммарное значение операций каким-то образом оказалось равно 0"
    assert value > 0, "Расходы превысили вашу зарплату"
    assert value < 996.74, "Вы не тратите деньги?"
    assert value == 871.07, "Я точно знаю сколько должно остаться на счету..."
