#
# # change = 0
# class Kindle:
#     def __init__(self):
#         self.power = False
#         self.page = 1
#
#     def toggle_power(self):
#         self.power = not self.power
#
#     def next_page(self):
#         self.page = self.page + 1
#
#     def prev_page(self):
#         if self.page>1:
#             self.page = self.page - 1
#
#
# class VendingMachine:
#     def __init__(self):
#         self.change = 0
#
#     def run(self, raw):
#         tokens = raw.split(" ")
#         cmd, params = tokens[0], tokens[1:]
#
#         if cmd == "잔액":
#             # return "잔액은 " + str(change) + "원입니다."
#             return "잔액은 " + str(self._change) + "원입니다."
#         elif cmd == "동전":
#             coin = params[0]
#             # change += int(params[0])
#             self._change += int(coin)
#             return coin + "원을 넣었습니다."
#         else:
#             return "알 수 없는 명령입니다."
#
#
# def init():
#     global change
#     change = 0

#
# def run(raw):
#     global change
#
#     tokens = raw.split(" ")
#     cmd, params = tokens[0], tokens[1:]    # return coin + "원을 넣었습니다."
#
#     if cmd not in ["잔액", "동전"]:
#         return "알 수 없는 명령입니다."
#     elif cmd == "잔액":
#         return "잔액은 " + str(change) + "원입니다."
#     else:
#         coin = params[0]
#         change += int(params[0])
#         return coin + "원을 넣었습니다."
#

class VendingMachine:
    def __init__(self):
        self._change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다"

        elif cmd == "동전":
            coin = params[0]

            if coin == "10":
                return coin + "원을 넣었습니다."

            elif coin == "50":
                return coin + "원을 넣었습니다."

            elif coin == "100":
                return coin + "원을 넣었습니다."

            elif coin == "500":
                return coin + "원을 넣었습니다."

            elif :
                return "알 수 없는 동전입니다."


        elif cmd == "커피":
            coin = params[0]

            if coin == "350":
                # self._change = int(coin) - 150
                return "커피가 나왔습니다. 잔액은 " + coin + "원 입니다."
            else:
                coin = "100"
                return "잔액이 부족합니다. 잔액은 " + coin + "원 입니다."
        else:
            return "알 수 없는 명령입니다"









# 지은님 코드!
    # 
    # def run(self, raw):
    #     tokens = raw.split(" ")
    #     cmd, params = tokens[0], tokens[1:]
    #
    #     if cmd == "잔액":
    #         return "잔액은 " + str(self._change) + "원입니다"
    #     elif cmd == "동전":
    #         known_coins = ["10", "50", "100", "500"]
    #
    #         coin = params[0]
    #         if coin not in known_coins:
    #             return "알 수 없는 동전입니다"
    #         self._change += int(coin)
    #         return coin + "원을 넣었습니다"
    #
    #     elif cmd == "음료":
    #         known_beverage = "커피"
    #         price = 150
    #
    #         beverage = params[0]
    #         if beverage != known_beverage:
    #             return "알 수 없는 음료입니다"
    #         if self._change < price:
    #             return "잔액이 부족합니다"
    #         self._change = self._change - price
    #         return beverage + "가 나왔습니다"
    #     else:
    #         return "알 수 없는 명령입니다"
    #
    #




C
