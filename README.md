# CarConnect-CaseStudy
### **Introduction**

The CarConnect application is a car-rental platform,admin(owner of the car rent company) 
and customers(who make rental reservations) can access this application for their respective purposes.
This is a simple menu-driven application that runs in the computer locally.
There are options/menus that are need to be chosen by the user based on their role(customer or admin).
Admin and existing customers are bound to logIn to the app in order to access their respective features and perform their actions.
New customers must first Signup and then can logIn using their username and password. 
This Signup and logIn is authenticated and validated thoroughly.
The admins are the ones who can access the details of the customer,like adding new customers,editing their data or manipulating the vehicle information.
And customers can view their profile,edit their details or make reservation,edit their current reservation,view previous reservations.

### **Features**

This app uses the CRUD technique i.e Create,Read,Update and Delete.

* #### Create:
Admin can Create new admin,new customers or add new vehicle.
Customer can create their account in the application through signup.

* #### Read:

Admin can view Vehicle,view Customers,View Reservations made and also view their own profile details.

Customers can view available vehicle for rent,view their past reservations and their profile details

* #### Update:

Admin can change the data/info of Vehicle and reservations dates or daily rates for the vehicles.

Customer can Change their personal details and their reservation(if already reserved a vehicle).

* #### Delete:

Admin can delete a customer or delete a vehicle.

Customer can delete their account or cancel their reservation.

### Real-time Updates in Backend:

When there is a change in the data of customer details they can see that their data getting updated without any refresh on the app 
and the availability of vehicle is also updated just after the reservation.

### Requirements

Python Version: python 3.7 or above.

Packages: Python-mysql-connector.

    pip install mysql-connector-python    

### Running the application

The main.py file in the main package is the file that needs to be run to make the application work.

terminal command:

    python main.py

### Future enhancements

Notifications => as this is an app that runs in a local environment generating real time notifications aren't possible. 
So if this becomes an online app then the app can be built to send real time SMS/Emails to the customer regarding their reservation and account status.

### Conclusion

I worked on this project from scratch and built this simple menu-driven car rental system with proper flow and real-time updates.
This project helped me understand CRUD operations, MySQL integration, Python project structuring, and how to maintain clean code.
There are still many areas where I can improve and enhance this project, but as of now, I’m happy with what I have built.
This is one of my starting steps in developing real-world projects.