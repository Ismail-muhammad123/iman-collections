from django.core import mail
from order.models import Order, OrderItem
from django.conf import settings


def get_new_order_notification_email(
    product: OrderItem,
    connection,
):
    subject = "You Have a New Order"
    seller_email = product.seller.email
    order_details_link = ""
    from_address = settings.EMAIL_FROM_ADDRESS
    body = f"""
            Your have recieved a new order for {product.quantity} {product.product.name}(s).
            <a href="{order_details_link}" >Click Here</a> to open the order details. 
        """
    if subject and body and from_address:
        return mail.EmailMessage(subject, body, from_address, [seller_email])
    else:
        return None


def get_new_order_confirmation_email_message(order: Order):
    from_address = settings.EMAIL_FROM_ADDRESS
    subject = "New Order Recieved"
    customer_email = order.email
    order_details_link = ""
    body = f"""
            Your new order has been recieved and is being processed. .
            <a href="{order_details_link}" >Click Here</a> to open the order details.
            Thank You for doing business with us. 
        """
    if subject and body and from_address:
        return mail.EmailMessage(subject, body, from_address, [customer_email])
    else:
        return None


def send_order_notifications(order: Order):
    mail_connection = mail.get_connection()
    sold_products = order.order_items.all()
    mail_messages = []
    for item in sold_products:
        mssg = get_new_order_notification_email(item, mail_connection)
        if mssg is not None:
            mail_messages.append(mssg)

    customer_mssg = get_new_order_confirmation_email_message(order)
    if customer_mssg:
        mail_messages.append(customer_mssg)

    mail_connection.send_messages(mail_messages)
