
# Necessary Imports
from Dao.AdminService import AdminService
# from Dao.AuthenticationService import AuthenticationService
from Dao.CustomerService import CustomerService
from Dao.VehicleService import VehicleService
from Dao.ReservationService import ReservationService
from CarConnect.entity import Admin as CarConnectAdmin
from CarConnect.entity.Customer import Customer as CarConnectCustomer
from CarConnect.entity import Vehicle as CarConnectVehicle
from CarConnect.entity import Reservation as CarConnectReservation
from CarConnect.exceptions import AdminNotFoundException as CarConnectAdminNotFoundException
from CarConnect.exceptions import AuthenticationException as CarConnectAuthenticationException
from CarConnect.exceptions import ReservationNotFoundException as CarConnectReservationNotFoundException
from CarConnect.exceptions import VehicleNotFoundException as CarConnectVehicleNotFoundException
from datetime import datetime

# ===========================
# Main Menu
# ===========================
def main_menu():
    while True:
        choice=''
        print("\n===== CarConnect Main Menu =====")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Customer Registration")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("\nPlease enter a valid number!")
            continue

        if choice == '1':
            admin_login()
        elif choice == '2':
            customer_login()
        elif choice == '3':
            customer_register()
        elif choice == '4':
            print("\nExiting the application...")
            break
        else:
            print("\nInvalid choice. Please try again.")

# ===========================
# Admin Login
# ===========================
def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")
    admin_service = AdminService()

    try:
        admin = admin_service.authenticate_admin(username, password)
        print(f"\nWelcome, {admin.get_first_name()} {admin.get_last_name()}!")
        print("You have successfully logged in as Admin.")
        admin_menu(admin)

    except CarConnectAuthenticationException.AuthenticationException as e:
        print(f"\nLogin failed: {e}")
    except CarConnectAdminNotFoundException.AdminNotFoundException as e:
        print(f"\nLogin failed: {e}")

# ===========================
# Admin Menu
# ===========================
def admin_menu(admin):
    vehicle_service = VehicleService()
    admin_service = AdminService()

    while True:
        choice=''
        print("\n===== Admin Menu =====")
        print("1. View Profile")
        print("2. Add Vehicle")
        print("3. View All Vehicles")
        print("4. Get vehicle by ID")
        print("5. Update Vehicle Daily Rate")
        print("6. Delete Vehicle")
        print("7. Register New Admin")
        print("8. Update Admin Profile")
        print("9. Delete Admin")
        print("10.Handle Customers")
        print("11.View Report")
        print("12. Logout")

        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("\nPlease enter a valid number!")
            continue

        if choice == '1':
            print(f"\nAdmin ID: {admin.get_admin_id()}")
            print(f"Name: {admin.get_first_name()} {admin.get_last_name()}")
            print(f"Email: {admin.get_email()}")
            print(f"Phone: {admin.get_phone_number()}")
            print(f"Role: {admin.get_role()}")
            print(f"Join Date: {admin.get_join_date().strftime('%Y-%m-%d')}")

        elif choice == '2':
            print("\n===== Add Vehicle =====")
            model = input("Enter Model: ")
            make = input("Enter Make: ")
            year = input("Enter Year: ")
            color = input("Enter Color: ")
            registration_number = input("Enter Registration Number: ")
            daily_rate = float(input("Enter Daily Rate: "))
            category = input("Enter Category: ")

            vehicle = CarConnectVehicle.Vehicle(
                model=model,
                make=make,
                year=year,
                color=color,
                registration_number=registration_number,
                availability=True,
                daily_rate=daily_rate,
                category=category
            )

            vehicle_service.add_vehicle(vehicle)

        elif choice == '3':
            print("\n===== All Vehicles =====")
            vehicles = vehicle_service.get_all_vehicles()
            for v in vehicles:
                print(f"\nID: {v.get_vehicle_id()} | Model: {v.get_model()} | Make: {v.get_make()} | Year: {v.get_year()} | Color: {v.get_color()} | RegNo: {v.get_registration_number()} | Available: {v.is_available()} | Rate: {v.get_daily_rate()} | Category: {v.get_category()}")

        elif choice == '4':
            try:
                vehicle_id = int(input("\nEnter Vehicle ID to View: "))
                vehicle = vehicle_service.get_vehicle_by_id(vehicle_id)
                if vehicle:
                    print(f"\nVehicle ID: {vehicle.get_vehicle_id()}")
                    print(f"Model: {vehicle.get_model()}")
                    print(f"Make: {vehicle.get_make()}")
                    print(f"Year: {vehicle.get_year()}")
                    print(f"Color: {vehicle.get_color()}")
                    print(f"Registration Number: {vehicle.get_registration_number()}")
                    print(f"Availability: {'Available' if vehicle.is_available() else 'Not Available'}")
                    print(f"Daily Rate: ₹{vehicle.get_daily_rate()}")
                    print(f"Category: {vehicle.get_category()}")
                else:
                    print("\nVehicle not found.")
            except ValueError:
                print("\nPlease enter a valid Vehicle ID!")

        elif choice == '5':
            try:
                vehicle_id = int(input("\nEnter Vehicle ID to Update: "))
                new_rate = float(input("Enter New Daily Rate: "))
                vehicle_service.update_vehicle(vehicle_id, new_rate)
            except ValueError:
                print("\nInvalid input! Please enter correct details.")
            except CarConnectVehicleNotFoundException.VehicleNotFoundException as e:
                print(f"\n{e}")

        elif choice == '6':
            try:
                vehicle_id = int(input("\nEnter Vehicle ID to Delete: "))
                vehicle_service.delete_vehicle(vehicle_id)
            except ValueError:
                print("\nPlease enter a valid Vehicle ID!")
            except CarConnectVehicleNotFoundException.VehicleNotFoundException as e:
                print(f"\n{e}")

        elif choice == '7':
            print("\n===== Register New Admin =====")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            role = input("Enter Role: ")
            join_date = datetime.now().strftime('%Y-%m-%d')

            new_admin = CarConnectAdmin.Admin(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                username=username,
                password=password,
                role=role,
                join_date=join_date
            )

            admin_service.register_admin(new_admin)

        elif choice == '8':
            print("\n===== Update Admin Profile =====")
            print("1. First Name")
            print("2. Last Name")
            print("3. Email")
            print("4. Phone Number")
            print("5. Username")
            print("6. Password")
            update_choice = input("Select the detail you want to update: ")

            field_map = {
                '1': 'FirstName',
                '2': 'LastName',
                '3': 'Email',
                '4': 'PhoneNumber',
                '5': 'Username',
                '6': 'Password'
            }

            if update_choice in field_map:
                new_value = input(f"Enter new {field_map[update_choice]}: ")
                admin_service.update_admin(admin.get_admin_id(), field_map[update_choice], new_value)
            else:
                print("\nInvalid selection.")

        elif choice == '9':
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == 'yes':
                success = admin_service.delete_admin(admin.get_admin_id())
                if success:
                    print("\nAdmin account deleted. Logging out...")
                    break
            else:
                print("\nAdmin deletion cancelled.")

        elif choice == '10':
            while True:
                print("\n===== Customer Management =====")
                print("1. View Customer by ID")
                print("2. Register New Customer")
                print("3. Update Customer")
                print("4. Delete Customer")
                print("5. Exit to Admin Menu")

                option = input("Enter your choice: ")

                if option == '1':
                    try:
                        customer_id = int(input("Enter Customer ID: "))
                        from Dao.CustomerService import CustomerService
                        customer_service = CustomerService()
                        customer = customer_service.get_customer_by_id(customer_id)
                        if customer:
                            print(f"\nCustomer ID: {customer.get_customer_id()}")
                            print(f"Name: {customer.get_first_name()} {customer.get_last_name()}")
                            print(f"Email: {customer.get_email()}")
                            print(f"Phone: {customer.get_phone_number()}")
                            print(f"Address: {customer.get_address()}")
                            print(f"Username: {customer.get_username()}")
                            print(f"Registration Date: {customer.get_registration_date().strftime('%Y-%m-%d')}")
                        else:
                            print("\nCustomer not found.")
                    except ValueError:
                        print("\nPlease enter a valid Customer ID.")

                elif option == '2':
                    try:
                        first_name = input("Enter First Name: ")
                        last_name = input("Enter Last Name: ")
                        email = input("Enter Email: ")
                        phone_number = input("Enter Phone Number: ")
                        address = input("Enter Address: ")
                        username = input("Enter Username: ")
                        password = input("Enter Password: ")
                        from datetime import datetime
                        registration_date = datetime.now().strftime('%Y-%m-%d')

                        from CarConnect.entity import Customer as CarConnectCustomer
                        from Dao.CustomerService import CustomerService
                        customer_service = CustomerService()

                        new_customer = CarConnectCustomer.Customer(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone_number=phone_number,
                            address=address,
                            username=username,
                            password=password,
                            registration_date=registration_date
                        )

                        customer_service.register_customer(new_customer)
                        # print("\nCustomer registered successfully!")

                    except Exception as e:
                        print(f"\nError: {e}")

                elif option == '3':
                    try:
                        customer_id = int(input("Enter Customer ID to update: "))
                        from Dao.CustomerService import CustomerService
                        customer_service = CustomerService()

                        print("\n===== Update Options =====")
                        print("1. First Name")
                        print("2. Last Name")
                        print("3. Email")
                        print("4. Username")
                        print("5. Password")
                        update_option = input("Select the detail you want to update: ")

                        field_map = {
                            '1': 'FirstName',
                            '2': 'LastName',
                            '3': 'Email',
                            '4': 'Username',
                            '5': 'Password'
                        }

                        if update_option in field_map:
                            new_value = input(f"Enter new {field_map[update_option]}: ")
                            success = customer_service.update_customer_profile(customer_id, field_map[update_option],
                                                                               new_value)
                            if success:
                                print("\nCustomer profile updated successfully!")
                        else:
                            print("\nInvalid selection.")
                    except ValueError:
                        print("\nPlease enter a valid Customer ID.")

                elif option == '4':
                    try:
                        customer_id = int(input("Enter Customer ID to delete: "))
                        from Dao.CustomerService import CustomerService
                        customer_service = CustomerService()

                        confirm = input("Are you sure you want to delete this customer? (yes/no): ")
                        if confirm.lower() == 'yes':
                            success = customer_service.delete_customer(customer_id)
                            if success:
                                print("\nCustomer deleted successfully!")
                        else:
                            print("\nCustomer deletion cancelled.")

                    except ValueError:
                        print("\nPlease enter a valid Customer ID.")

                elif option == '5':
                    break

                else:
                    print("\nInvalid choice. Please try again.")

        elif choice == '11':
            while True:
                print("\n===== Report Management =====")
                print("1. View All Reservations")
                print("2. View Reservations by Customer ID")
                print("3. View Reservations by Vehicle ID")
                print("4. Back to Admin Menu")

                report_choice = input("Enter your choice: ")

                if report_choice == '1':
                    reservations = ReservationService().get_all_reservations()
                    if not reservations:
                        print("\nNo reservations found.")
                    else:
                        print("\n===== All Reservations =====")
                        for r in reservations:
                            print(
                                f"\nReservation ID: {r.get_reservation_id()} | Customer ID: {r.get_customer_id()} | Vehicle ID: {r.get_vehicle_id()} | Start: {r.get_start_date().strftime('%Y-%m-%d')} | End: {r.get_end_date().strftime('%Y-%m-%d')} | Total Cost: ₹{r.get_total_cost()} | Status: {r.get_status()}")

                elif report_choice == '2':
                    try:
                        customer_id = int(input("Enter Customer ID: "))
                        reservations = ReservationService().get_customer_reservations(customer_id)
                        if not reservations:
                            print("\nNo reservations found for this customer.")
                        else:
                            print("\n===== Customer Reservations =====")
                            for r in reservations:
                                print(
                                    f"\nReservation ID: {r.get_reservation_id()} | Vehicle ID: {r.get_vehicle_id()} | Start: {r.get_start_date().strftime('%Y-%m-%d')} | End: {r.get_end_date().strftime('%Y-%m-%d')} | Total Cost: ₹{r.get_total_cost()} | Status: {r.get_status()}")
                    except ValueError:
                        print("\nInvalid Customer ID!")

                elif report_choice == '3':
                    try:
                        vehicle_id = int(input("Enter Vehicle ID: "))
                        reservations = ReservationService().get_reservations_by_vehicle_id(vehicle_id)
                        if not reservations:
                            print("\nNo reservations found for this vehicle.")
                        else:
                            print("\n===== Vehicle Reservations =====")
                            for r in reservations:
                                print(
                                    f"\nReservation ID: {r.get_reservation_id()} | Customer ID: {r.get_customer_id()} | Start: {r.get_start_date().strftime('%Y-%m-%d')} | End: {r.get_end_date().strftime('%Y-%m-%d')} | Total Cost: ₹{r.get_total_cost()} | Status: {r.get_status()}")
                    except ValueError:
                        print("\nInvalid Vehicle ID!")

                elif report_choice == '4':
                    break

                else:
                    print("\nInvalid choice. Please try again.")

        elif choice == '12':
            print("\nLogging out...")
            break

        else:
            print("\nInvalid choice. Please try again.")

# ===========================
# Customer Registration
# ===========================
def customer_register():
    customer_service = CustomerService()
    print("\n===== Customer Registration =====")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    phone_number = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    registration_date = datetime.now().strftime('%Y-%m-%d')

    customer = CarConnectCustomer(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        address=address,
        username=username,
        password=password,
        registration_date=registration_date
    )

    customer_service.register_customer(customer)

# ===========================
# Customer Login
# ===========================
def customer_login():
    customer_service = CustomerService()
    print("\n===== Customer Login =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        customer = customer_service.authenticate_customer(username, password)
        print(f"\nWelcome, {customer.get_first_name()} {customer.get_last_name()}!")
        customer_menu(customer)

    except CarConnectAuthenticationException.AuthenticationException as e:
        print(f"\nLogin failed: {e}")

# ===========================
# Customer Menu
# ===========================
def customer_menu(customer):
    vehicle_service = VehicleService()
    reservation_service = ReservationService()

    while True:
        choice=''
        print("\n===== Customer Menu =====")
        print("1. View Profile")
        print("2. View All Available Vehicles")
        print("3. Make a Reservation")
        print("4. View My Reservations")
        print("5. Update Profile")
        print("6. Delete My Account")
        print("7. Cancel Reservation")
        print("8. Update Reservation")
        print("9. Logout")
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("\nPlease enter a valid number!")
            continue

        if choice == '1': #viewing profile
            print(f"\nCustomer ID: {customer.get_customer_id()}")
            print(f"Name: {customer.get_first_name()} {customer.get_last_name()}")
            print(f"Email: {customer.get_email()}")
            print(f"Phone: {customer.get_phone_number()}")
            print(f"Address: {customer.get_address()}")
            print(f"Username: {customer.get_username()}")
            print(f"Registration Date: {customer.get_registration_date().strftime('%Y-%m-%d')}")

        elif choice == '2': #viewing all available vehicles
            print("\n===== Available Vehicles =====")
            vehicles = vehicle_service.get_available_vehicles()
            for v in vehicles:
                print(f"\nID: {v.get_vehicle_id()} | Model: {v.get_model()} | Make: {v.get_make()} | Year: {v.get_year()} | Color: {v.get_color()} | RegNo: {v.get_registration_number()} | Available: {v.is_available()} | Rate: {v.get_daily_rate()} | Category: {v.get_category()}")

        elif choice == '3': #Reserving a vehicle

            try:
                vehicle_id = int(input("\nEnter Vehicle ID to Reserve: "))
            except ValueError:
                print("\nPlease enter a valid Vehicle ID!")
                continue
            # if not vehicle_service.is_vehicle_active(vehicle_id):
            #     print("\nThe selected vehicle is currently not available (marked unavailable).")
            #     continue
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            is_available = reservation_service.is_vehicle_available(vehicle_id, start_date, end_date)
            if is_available:
                start = datetime.strptime(start_date, '%Y-%m-%d')
                end = datetime.strptime(end_date, '%Y-%m-%d')
                num_days = (end - start).days + 1  # Including both start and end dates
                daily_rate = vehicle_service.get_vehicle_daily_rate(vehicle_id)
                if daily_rate is None:
                    print("\nVehicle not found.")
                    continue
                total_cost = num_days * daily_rate
                print(f"\nYour total cost for this reservation is: ₹{total_cost}")
                reservation = CarConnectReservation.Reservation(
                    customer_id=customer.get_customer_id(),
                    vehicle_id=vehicle_id,
                    start_date=start_date,
                    end_date=end_date,
                    total_cost=total_cost
                )
                reservation_service.create_reservation(reservation)
                # vehicle_service.mark_vehicle_unavailable(vehicle_id)

            else:
                print("\nThe selected vehicle is not available for the selected dates.")

        elif choice == '4': #Viewing past reservations
            try:
                reservations = reservation_service.get_customer_reservations(customer.get_customer_id())
                print("\n===== Your Reservations =====")
                for r in reservations:
                    print(f"\nReservation ID: {r.get_reservation_id()} | Vehicle ID: {r.get_vehicle_id()} | Start Date: {r.get_start_date().strftime('%Y-%m-%d')} | End Date: {r.get_end_date().strftime('%Y-%m-%d')} | Total Cost: {r.get_total_cost()}")

            except CarConnectReservationNotFoundException.ReservationNotFoundException as e:
                print(f"\n{e}")

        elif choice == '5': #updating the user profile
            print("\n===== Update Profile =====")
            print("1. First Name")
            print("2. Last Name")
            print("3. Email")
            print("4. Username")
            print("5. Password")
            try:
                update_choice = input("Select the detail you want to update: ")
            except ValueError:
                print("\nPlease enter a valid number!")
                continue
            field_map = {
                '1': 'FirstName',
                '2': 'LastName',
                '3': 'Email',
                '4': 'Username',
                '5': 'Password'
            }
            if update_choice in field_map:
                new_value = input(f"Enter new {field_map[update_choice]}: ")
                auth_service = CustomerService()
                update_success=auth_service.update_customer_profile(customer.get_customer_id(), field_map[update_choice],
                                                         new_value)
                if update_success:
                    customer = auth_service.get_customer_by_id(customer.get_customer_id())
                    print("\nProfile updated successfully!")

            else:
                print("\nInvalid selection.")

        elif choice == '6':
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == 'yes':
                auth_service = CustomerService()
                success = auth_service.delete_customer(customer.get_customer_id())
                if success:
                    print("\nAccount deleted. Logging out...")
                    break
            else:
                print("\nAccount deletion cancelled.")


        elif choice == '7':
            reservation_id=None
            reservations = reservation_service.get_customer_reservations(customer.get_customer_id())
            if not reservations:
                print("\nYou have no reservations to cancel!")
                continue
            print("\n===== Your Reservations =====")
            for r in reservations:
                print(f"\nReservation ID: {r.get_reservation_id()} | Vehicle ID: {r.get_vehicle_id()} | "
                      f"Start Date: {r.get_start_date().strftime('%Y-%m-%d')} | End Date: {r.get_end_date().strftime('%Y-%m-%d')} | "
                      f"Total Cost: {r.get_total_cost()}")
            try:
                reservation_id = int(input("Enter Reservation ID to cancel: "))
            except ValueError:
                print("\nInvalid input. Please enter a valid Reservation ID.")
                continue
            matching_reservation = None
            for res in reservations:
                if res.get_reservation_id() == reservation_id:
                    matching_reservation = res
                    break
            if not matching_reservation:
                print("\nInvalid Reservation ID. You can only cancel your own reservations.")
                continue
            success = reservation_service.cancel_reservation(reservation_id)
            if success:
                print("\nReservation successfully cancelled.")

        elif choice == '8':
            try:
                reservations = reservation_service.get_customer_reservations(customer.get_customer_id())
                if not reservations:
                    print("\nYou have no reservations to update.")
                    continue

                print("\n===== Your Reservations =====")
                for r in reservations:
                    print(
                        f"\nReservation ID: {r.get_reservation_id()} | Vehicle ID: {r.get_vehicle_id()} | Start Date: {r.get_start_date().strftime('%Y-%m-%d')} | End Date: {r.get_end_date().strftime('%Y-%m-%d')} | Total Cost: {r.get_total_cost()}")

                reservation_id = int(input("\nEnter the Reservation ID you want to update: "))

                matching_reservation = None
                for res in reservations:
                    if res.get_reservation_id() == reservation_id:
                        matching_reservation = res
                        break

                if not matching_reservation:
                    print("\nInvalid Reservation ID. You can only update your own reservations.")
                    continue

                while True:
                    print("\n===== Update Reservation Menu =====")
                    print("1. Change Dates Only")
                    print("2. Change Vehicle Only")
                    print("3. Change Both Dates and Vehicle")
                    print("4. Back to Customer Menu")

                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':  # Change Dates Only
                        new_start_date = input("Enter new Start Date (YYYY-MM-DD): ")
                        new_end_date = input("Enter new End Date (YYYY-MM-DD): ")

                        existing_reservation = reservation_service.get_reservation_by_id(reservation_id)
                        if existing_reservation:
                            success = reservation_service.update_reservation(reservation_id,
                                                                             existing_reservation.get_vehicle_id(),
                                                                             new_start_date, new_end_date)
                            if success:
                                print("\nReservation dates updated successfully.")
                            break
                        else:
                            print("\nReservation not found!")
                            break

                    elif sub_choice == '2':  # Change Vehicle Only
                        new_vehicle_id = int(input("Enter New Vehicle ID: "))

                        existing_reservation = reservation_service.get_reservation_by_id(reservation_id)
                        if existing_reservation:
                            success = reservation_service.update_reservation(reservation_id, new_vehicle_id,
                                                                             existing_reservation.get_start_date().strftime(
                                                                                 '%Y-%m-%d'),
                                                                             existing_reservation.get_end_date().strftime(
                                                                                 '%Y-%m-%d'))
                            if success:
                                print("\nReservation vehicle updated successfully.")
                            break
                        else:
                            print("\nReservation not found!")
                            break

                    elif sub_choice == '3':  # Change Both Dates and Vehicle
                        new_vehicle_id = int(input("Enter New Vehicle ID: "))
                        new_start_date = input("Enter new Start Date (YYYY-MM-DD): ")
                        new_end_date = input("Enter new End Date (YYYY-MM-DD): ")

                        success = reservation_service.update_reservation(reservation_id, new_vehicle_id, new_start_date,
                                                                         new_end_date)
                        if success:
                            print("\nReservation updated successfully with new vehicle and dates.")
                        break

                    elif sub_choice == '4':  # Go back
                        break
                    else:
                        print("\nInvalid choice in update menu. Please try again.")
            except ValueError:
                print("\nInvalid input. Please enter valid IDs and dates.")

        elif choice == '9': #exiting the menu
            print("\nLogging out...")
            break
        else:
            print("\nInvalid choice. Please try again.")


# ===========================
# Run App
# ===========================
if __name__ == "__main__":
    main_menu()

