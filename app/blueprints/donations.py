#     return render_template('donation_form.html')
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Contact, Donation  # Ensure model class names are capitalized

donations_bp = Blueprint('donations', __name__)

@donations_bp.route('/contact', methods=['GET','POST'])
def contact_page():  # Renamed to avoid conflict with the model
    if request.method == 'POST':
        print(f"Request method: {request.method}")
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save to the Contact table
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        # # Redirect to a thank you page
        # return redirect(url_for('donations.thank_you'))

    return render_template('contact.html')

@donations_bp.route('/thank_you')
def thank_you():
    return "Thank you for your message!"

@donations_bp.route('/donate/form', methods=['GET', 'POST'])
def donation_form():
    if request.method == 'POST':
        wallet_address = request.form.get('wallet_address')
        amount = request.form.get('amount')
        message = request.form.get('message')

        # Save to the Donation table
        new_donation = Donation(wallet_address=wallet_address, amount=amount, message=message)
        db.session.add(new_donation)
        db.session.commit()

        # Redirect to a "Thank You" page or another confirmation page
        return redirect(url_for('donations.thank_you'))

    return render_template('donation_form.html')
