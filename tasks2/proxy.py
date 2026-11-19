from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount: float) -> None: ...


class RealBankAccount(BankAccount):
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print(f"  Xato: summa musbat bo'lishi kerak ({amount})")
        elif amount > self.balance:
            print(f"  Xato: mablag' yetarli emas. Balans: {self.balance:,.2f}, so'ralgan: {amount:,.2f}")
        else:
            self.balance -= amount
            print(f"  Muvaffaqiyatli: {amount:,.2f} yechildi. Qoldiq: {self.balance:,.2f}")


class BankAccountProxy(BankAccount):
    def __init__(self, real_account: RealBankAccount, username: str):
        self._real_account = real_account
        self._username = username
        self._logged_in = False

    def login(self) -> None:
        self._logged_in = True
        print(f"{self._username} tizimga kirdi")

    def logout(self) -> None:
        self._logged_in = False
        print(f"{self._username} tizimdan chiqdi")

    def withdraw(self, amount: float) -> None:
        print(f"{self._username}: {amount:,.2f} yechishga urinish...")
        if not self._logged_in:
            print("  Rad etildi: foydalanuvchi tizimga kirmagan")
            return
        self._real_account.withdraw(amount)


class BankApp:
    @staticmethod
    def main() -> None:
        account: BankAccount = BankAccountProxy(RealBankAccount(1_000_000), "Ali")

        account.withdraw(100_000)

        account.login()
        account.withdraw(200_000)
        account.withdraw(5_000_000)

        account.logout()
        account.withdraw(50_000)


if __name__ == "__main__":
    BankApp.main()
