# ☕ Python 기반 Cafe Kiosk 시뮬레이션

## 📌 주제
일상 속 소프트웨어 사용 사례 - 키오스크를 통한 카페 주문 흐름 시뮬레이션

## 📊 시퀀스 다이어그램
Mermaid를 활용한 시퀀스 다이어그램 ([Mermaid Live Editor](https://mermaid.live)에서 확인 가능)

```mermaid
sequenceDiagram
    participant User
    participant Kiosk
    participant PaymentSystem
    participant Barista

    User->>Kiosk: 메뉴 선택
    Kiosk->>User: 주문 확인 요청
    User->>Kiosk: 주문 확정
    Kiosk->>PaymentSystem: 결제 요청
    PaymentSystem-->>Kiosk: 결제 성공 응답
    Kiosk->>Barista: 제조 요청
    Barista-->>Kiosk: 제조 완료
    Kiosk->>User: 픽업 알림
