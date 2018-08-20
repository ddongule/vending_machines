# from vm import run

# def test_insert_coin():
#     assert "잔액은 0원입니다." ==  run("잔액")
#     assert "100원을 넣었습니다." ==  run("동전 100")
#     assert "잔액은 100원입니다." ==  run("잔액")
#     assert "100원을 넣었습니다." ==  run("동전 100")
#     assert "잔액은 200원입니다." ==  run("잔액")

# def test_insert_coin_and_check():
#     responst = run("동전 100")
#     assert "100원을 넣었습니다" == response
# def test_initial_change_should_be_zero():
#     assert "잔액은 0원입니다." ==
#

from vm import VendingMachine

#
# def test_initial_change_should_be_zero():
#     m = VendingMachine()
#     assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다." == m.run("동전 100")
    # assert "잔액은 100원입니다." == m.run("잔액")

#
# def test_accumulation_of_change():
#     m = VendingMachine()
#     m.run("동전 100")
#     m.run("동전 100")
#     assert "잔액은 200원입니다" == m.run("잔액")

def test_unknown_command():
    m = VendingMachine()
    assert "알 수 없는 명령입니다" == m.run("웅앵")

def test_coffee_drink():
    m = VendingMachine()
    m.run("동전 500")
    assert "커피가 나왔습니다. 잔액은 350원 입니다." == m.run("커피 350")

def test_coffee_cannot_drink():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액이 부족합니다. 잔액은 100원 입니다." == m.run("커피 100")

def test_coins():
    m = VendingMachine()
    assert "10원을 넣었습니다." == m.run("동전 10")
    assert "50원을 넣었습니다." == m.run("동전 50")
    assert "100원을 넣었습니다." == m.run("동전 100")
    assert "500원을 넣었습니다." == m.run("동전 500")
    assert "120원을 넣었습니다." == m.run("동전 120")
