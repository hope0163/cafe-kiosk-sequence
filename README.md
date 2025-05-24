# ☕ Python 기반 Cafe Kiosk 시뮬레이션

일상 속 소프트웨어 사용 사례를 기반으로 한 키오스크 주문 흐름을 모델링하고, 이를 Python 코드로 구현


## 모듈 평가

### ✅ 응집도 (Cohesion)
- `Kiosk` 클래스는 **주문, 결제, 알림** 등 키오스크의 역할에 집중합니다.
- `Barista` 클래스는 **음료 제조**에만 집중합니다.
- 각 클래스는 **단일 책임 원칙(SRP)**을 잘 따르며, **높은 응집도**를 유지합니다.

### ✅ 결합도 (Coupling)
- 클래스 간에는 **직접적인 데이터 의존 없이 메서드 호출**로만 상호작용합니다.
- 구조적으로 유연하며, **유지보수 및 확장에 유리한 낮은 결합도**를 갖습니다.

---


## 시퀀스 다이어그램

- **주제**: 사용자가 키오스크를 이용해 카페 음료를 주문하는 흐름

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


