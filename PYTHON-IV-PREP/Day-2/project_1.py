import os
import csv
import shutil
from datetime import date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(incoming_count, success_count, rejected_count):
    # Email configuration
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"
    sender_email = "sender@example.com"
    receiver_email = "receiver@example.com"

    # Get the current date
    current_date = date.today().strftime("%Y-%m-%d")

    # Email content
    subject = f"Validation Email {current_date}"
    body = f"Incoming Files: {incoming_count}\nSuccess Files: {success_count}\nRejected Files: {rejected_count}"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send the email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)


def process_files():
    incoming_folder = "incoming_files"
    success_folder = "success_files"
    rejected_folder = "rejected_files"

    # Create current_date folder paths
    current_date = date.today().strftime("%Y%m%d")
    current_date_folder = os.path.join(success_folder, current_date)
    current_date_rejected_folder = os.path.join(rejected_folder, current_date)

    # Create success_files/current_date and rejected_files/current_date folders
    os.makedirs(current_date_folder, exist_ok=True)
    os.makedirs(current_date_rejected_folder, exist_ok=True)

    # Count the number of files in incoming_files/current_date
    incoming_count = len(os.listdir(os.path.join(incoming_folder, current_date)))

    if incoming_count > 0:
        # Process each file in incoming_files/current_date
        for file_name in os.listdir(os.path.join(incoming_folder, current_date)):
            file_path = os.path.join(incoming_folder, current_date, file_name)

            # Verify file conditions
            if (
                    os.path.isfile(file_path)
                    and file_name.endswith(".csv")
                    and not file_name.startswith("product_master")
            ):
                # Verify order file and extract data
                orders_to_notify = []
                with open(file_path, "r") as order_file:
                    order_reader = csv.DictReader(order_file)
                    for order in order_reader:
                        order_id = order["order_id"]
                        order_date = order["order_date"]
                        product_id = order["product_id"]
                        quantity = order["quantity"]
                        sales = order["sales"]
                        city = order["city"]

                        # Verify conditions
                        issues = []
                        if order_date > date.today().strftime("%d/%m/%Y"):
                            issues.append("Order date in the future")
                        if not all(order.values()):
                            issues.append("Empty field(s)")
                        if city != "Bangalore" and city != "Mumbai":
                            issues.append("Invalid city")

                        if issues:
                            issues_str = "; ".join(issues)
                            orders_to_notify.append(
                                {
                                    "Order ID": order_id,
                                    "Order Date": order_date,
                                    "Product ID": product_id,
                                    "Quantity": quantity,
                                    "Sales": sales,
                                    "City": city,
                                    "Issue": issues_str,
                                }
                            )

                if orders_to_notify:
                    # Move file to rejected_files/current_date folder
                    rejected_file_path = os.path.join(current_date_rejected_folder, file_name)
                    shutil.move(file_path, rejected_file_path)

                    # Create rejected file with orders and issues
                    rejected_csv_file = os.path.splitext(file_name)[0] + "_rejected.csv"
                    rejected_csv_path = os.path.join(current_date_rejected_folder, rejected_csv_file)
                    with open(rejected_csv_path, "w", newline="") as csv_file:
                        fieldnames = [
                            "Order ID",
                            "Order Date",
                            "Product ID",
                            "Quantity",
                            "Sales",
                            "City",
                            "Issue",
                        ]
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(orders_to_notify)

                else:
                    # Move file to success_files/current_date folder
                    success_file_path = os.path.join(current_date_folder, file_name)
                    shutil.move(file_path, success_file_path)

        # Count the number of success and rejected files
        success_count = len(os.listdir(current_date_folder))
        rejected_count = len(os.listdir(current_date_rejected_folder))

        # Send email notification
        send_email(incoming_count, success_count, rejected_count)

    else:
        print(f"No incoming files found for {current_date}")


# Run the main process
if __name__ == "__main__":
    process_files()
