from flask import Blueprint, request, jsonify
import jwt
import time
import base64
from flasgger import swag_from
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from app.models import Transaction
from app import db


blueprint = Blueprint('auth', __name__)

VALID_USERNAME = 'customer-phongtroabc-user25247'
VALID_PASSWORD = 'Y3VzdG9tZXItcGhvbmd0cm9hYmMtdXNlcjI1MjQ3'
SECRET_KEY = 'secret'

# API để tạo token
@blueprint.route('/vqr/api/token_generate', methods=['POST'])
def generate_token():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Basic '):
        return jsonify({"error": "Authorization header is missing or invalid"}), 400

    base64_credentials = auth_header.split(' ')[1]
    credentials = base64.b64decode(base64_credentials).decode('utf-8')
    username, password = credentials.split(':')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        issued_at = int(time.time())
        expiration_time = issued_at + 300
        payload = {
            'username': username,
            'iat': issued_at,
            'exp': expiration_time
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS512')

        return jsonify({
            "access_token": token,
            "token_type": "Bearer",
            "expires_in": 300
        })
    else:
        return jsonify({"error": "Invalid credentials"}), 401


#######################################################################################################


@blueprint.route('/bank/api/transaction-sync', methods=['POST'])
def transaction_sync():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "INVALID_AUTH_HEADER", "message": "Authorization header is missing or invalid"}), 401

    token = auth_header.split(' ')[1]

    if not validate_token(token):
        return jsonify({"error": "INVALID_TOKEN", "message": "Invalid or expired token"}), 401

    data = request.json


    try:
        new_transaction = Transaction(
            bankaccount=data.get('bankaccount'),
            amount=data.get('amount'),
            transType=data.get('transType'),
            content=data.get('content'),
            transactionid=data.get('transactionid'),
            transactiontime=data.get('transactiontime'),
            referencenumber=data.get('referencenumber'),
            orderId=data.get('orderId'),
            terminalCode=data.get('terminalCode'),
            subTerminalCode=data.get('subTerminalCode'),
            serviceCode=data.get('serviceCode'),
            urlLink=data.get('urlLink'),
            sign=data.get('sign')
        )

        print(f"Transaction: {new_transaction.__dict__}")


        return jsonify({
            "error": False,
            "errorReason": None,
            "toastMessage": "Transaction processed successfully",
            "object": {"reftransactionid": new_transaction.id}
        }), 200

    except Exception as e:
        return jsonify({"error": True, "errorReason": "TRANSACTION_FAILED", "toastMessage": str(e), "object": None}), 400


# Hàm xác thực JWT
def validate_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS512"])
        return True
    except (ExpiredSignatureError, InvalidTokenError):
        return False
