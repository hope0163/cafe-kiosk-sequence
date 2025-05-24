class Kiosk:
    def select_menu(self, item):
        print(f"메뉴 선택: {item}")

    def confirm_order(self):
        print("주문 확인 요청")
        return True

    def request_payment(self):
        print("결제 요청")
        print("결제 성공")

    def send_order_to_barista(self):
        print("바리스타에게 제조 요청")

    def notify_user(self):
        print("제조 완료, 픽업 알림")


class Barista:
    def make_drink(self):
        print("음료 제조 중...")
        print("음료 제조 완료")


def cafe_order_system():
    kiosk = Kiosk()
    barista = Barista()

    kiosk.select_menu("아메리카노")
    if kiosk.confirm_order():
        kiosk.request_payment()
        kiosk.send_order_to_barista()
        barista.make_drink()
        kiosk.notify_user()


if __name__ == "__main__":
    cafe_order_system()
