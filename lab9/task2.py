class sru_student:
    """
    Module for representing SRU student information and fee status.
    Classes:
        sru_student:
    Represents a student at SRU with attributes for name, roll number, hostel status, and fee payment status.
        Methods:
     __init__(name, roll_no, hostel_status):
Initializes a new student with the given name, roll number, and hostel status. Fee status is set to unpaid by default.
            fee_update(status):
                Updates the fee payment status for the student.
            display_details():
        Prints the student's details including name, roll number, hostel status, and fee payment status.
    """
    def __init__(self, name, roll_no, hostel_status):
        self.name = name                # Store student's name
        self.roll_no = roll_no          # Store student's roll number
        self.hostel_status = hostel_status  # Store student's hostel status
        self.fee_paid = False           # Initialize fee status as unpaid

    def fee_update(self, status):
        """Update the fee payment status."""
        self.fee_paid = status          # Update fee status (True for paid, False for unpaid)

    def display_details(self):
        """Display student details."""
        print(f"Name: {self.name}")     # Print student's name
        print(f"Roll No.: {self.roll_no}")  # Print student's roll number
        print(f"Hostel Status: {self.hostel_status}")  # Print hostel status
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")  # Print fee payment status

# Example usage
if __name__ == "__main__":
    student = sru_student("Alice", "SRU123", "Yes")  # Create a student object
    student.display_details()                        # Display initial details
    student.fee_update(True)                         # Update fee status to paid
    student.display_details()                        # Display updated details