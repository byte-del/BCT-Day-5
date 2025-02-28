from prettytable import PrettyTable

class UserManager:
    users = []  # Class variable to store users

    @classmethod  #it belongs to the class rather than as instance of the class
    def display_users(cls):
        """Display users in a table format using PrettyTable."""
        if not cls.users:
            print("No users registered yet.")
            return

        table = PrettyTable()
        table.field_names = ["Email", "Password"]

        for user in cls.users:
            table.add_row([user["e"], user["p"]])

        print(table)

    @classmethod
    def signup(cls):
        """Function to handle user signup."""
        while True:
            email = input("Enter your email to sign up: ").strip()
            if email in [user["e"] for user in cls.users]:
                print("This email is already registered. Try signing in.")
                continue

            password = input("Create a password: ")
            confirm_password = input("Confirm your password: ")

            if password != confirm_password:
                print("Passwords do not match. Try again.")
                continue

            if email.endswith("@gmail.com"):
                cls.users.append({"e": email, "p": password})
                print("Signup successful! You can now sign in.")
                break
            else:
                print("Enter a valid Gmail address.")

    @classmethod
    def signin(cls):
        """Function to handle user sign-in."""
        while True:
            email = input("Enter your email to sign in: ").strip()
            password = input("Enter your password: ")

            for user in cls.users:
                if user["e"] == email and user["p"] == password:
                    print("Sign in successful! Welcome.")
                    return

            print("Incorrect email or password. Please try again.")

    @classmethod
    def main(cls):
        """Main menu function to handle user interaction."""
        while True:
            print("\n1. Sign up")
            print("2. Sign in")
            print("3. Display Users")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                cls.signup()
            elif choice == "2":
                cls.signin()
            elif choice == "3":
                cls.display_users()
            elif choice == "4":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    UserManager.main()