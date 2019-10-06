import os
import stripe
from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required, current_user
from genai.models import User
from genai import db, login_manager

blueprint = Blueprint('account', __name__, url_prefix='/account')

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@blueprint.route('/', methods=['GET'])
@login_required
def index():
    return render_template('account/index.html')

@blueprint.route('/public-key', methods=['GET'])
@login_required
def get_public_key():
    return jsonify({'publicKey': os.getenv('STRIPE_PUBLIC_KEY')})

@blueprint.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
    domain_url = os.getenv('DOMAIN')
    plan_id = os.getenv('STRIPE_SUBSCRIPTION_PLAN_ID')

    # Customer is only signing up for a subscription
    checkout_session = stripe.checkout.Session.create(
        success_url=domain_url + "/account/success",
        cancel_url=domain_url + "/account",
        payment_method_types=["card"],
        subscription_data={
            "items": [{"plan": plan_id}],
            "trial_period_days": 7
        },
    )
    return jsonify({'checkoutSessionId': checkout_session['id']})

@blueprint.route('/success')
@login_required
def success():
    current_user.is_subscribed = True
    db.session.commit()
    return render_template('account/index.html')
