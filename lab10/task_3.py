class Employee:
    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = float(salary)
    @property
    def name(self) -> str:
        return self._name
    @property
    def salary(self) -> float:
        return self._salary
    def increase_salary(self, percent: float) -> None:
        if percent < -100:
            raise ValueError("Percent cannot reduce salary below zero.")
        self._salary *= (1 + percent / 100)
    def __str__(self) -> str:
        return f"Employee(name={self._name}, salary={self._salary:.2f})"

e = Employee("John", 10000)
e.increase_salary(10)
print(e)
e1 = Employee("Jane", 20000)
e1.increase_salary(5)
print(e1)