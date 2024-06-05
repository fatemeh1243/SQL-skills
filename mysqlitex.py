import os
import sqlite3
class ExpenseManager:
    def __init__(self):
        self.conn = sqlite3.connect("exp.db")
        self.cursor = self.conn.cursor()
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def main(self):
        self.clear_screen()
        while True:
            print('1. Add exp 2. View exp 3. Update exp 4. Remove exp 5. Exit')
            choice = input("enter smth:")
            if choice == '1':
                self.add_exp()
            elif choice == '2':
                self.view_exp()
            elif choice == '3':
                self.update_exp()
            elif choice == '4':
                self.remove_exp()
            elif choice == '5':
                print("See you maybe?!")
                break
            else:
                print("Invalid input!")
    def add_exp(self):
        date = input("Please enter date: ")
        category = input('Please enter category: ')
        amount = float(input("Please enter amount: "))
        description = input("Please enter description: ")
        self.cursor.execute(
            "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)", 
            (date, category, amount, description))
        self.conn.commit()
        print("Expense added successfully.")
    def view_exp(self):
        self.cursor.execute("SELECT * FROM exp")
        for exp in self.cursor.fetchall():
            print(exp)
    def update_expense(self):
        id = int(input("Enter exp id: "))
        new_date = input("Please enter new((date:))")
        new_category = input("Please enter new category:")
        new_amount = float(input("Please enter new amount:"))
        new_description = input("Please enter new description:")
        self.cursor.execute((new_date, new_category, new_amount, new_description, id))
        self.conn.commit()
        print("<Expense updated>")
    def remove_exp(self):
        id = int(input("Please enter exp id:"))
        self.cursor.execute("DELETE FROM exp where id = ?",(id,))
        self.conn.commit()
        print(">Exp removed<")
    def run(self):
        self.main()
        self.conn.close()
if __name__ == "__main__":
    manager = ExpenseManager()
    manager.run()