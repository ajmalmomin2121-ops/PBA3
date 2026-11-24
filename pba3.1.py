class Resident:
    def __init__(self, name, flat_no, fee, status):
        self.name = name
        self.flat_no = flat_no
        self.fee = fee
        self.status = status.lower() if status.lower() in ("paid", "pending") else "pending"

    def display_details(self):
        print(f"Name: {self.name}, Flat: {self.flat_no}, Fee: {self.fee}, Status: {self.status}")


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    def display_all_maintenance(self):
        for resident in self.residents:
            resident.display_details()


if __name__ == "__main__":
    society = Society()
    society.add_resident(Resident("Rahul", "A-101", 2000, "paid"))
    society.add_resident(Resident("Sneha", "B-202", 2000, "pending"))
    society.display_all_maintenance()