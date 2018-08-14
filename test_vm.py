from vm import run, init

# def test_insert_coin():
#     assert "잔액은 0원입니다." ==  run("잔액")
#     assert "100원을 넣었습니다." ==  run("동전 100")
#     assert "잔액은 100원입니다." ==  run("잔액")
#     assert "100원을 넣었습니다." ==  run("동전 100")
#     assert "잔액은 200원입니다." ==  run("잔액")

# def test_insert_coin_and_check():
#     responst = run("동전 100")
#     assert "100원을 넣었습니다" == response
def test_initial_change_should_be_zero():
    init()
    assert "잔액은 0원입니다." == run("잔액")

def test_insert_coin_and_check():
    init()
    assert "100원을 넣었습니다." == run("동전 100")
    assert "잔액은 100원입니다." == run("잔액")


def test_iaccumulation_of_change():
    init()
    run("동전 100")
    run("동전 100")
    assert "잔액은 200원입니다." == run("잔액")


def test_unknown_command():
    init()
    assert "알 수 없는 명령입니다." == run("웅앵")
    assert "알 수 없는 명령입니다." == run("동줜")
