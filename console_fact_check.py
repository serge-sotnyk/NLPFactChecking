from solver.FactChecker import FactChecker


def console_repl():
    checker = FactChecker()

    while True:
        try:
            fact = input("fact>").strip()
            if not fact:
                return
            result = checker.check_fact(fact)
            if result > 0.7:
                print("It looks like fact is true.")
            else:
                print("It looks like fact is false.")
            print()
        except Exception as ex:
            print("Error:")
            print(ex)


if __name__ == "__main__":
    print("Enter facts to check. Empty string to exit from application.")
    console_repl()
