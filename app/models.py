from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bankaccount = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transType = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=True)
    transactionid = db.Column(db.String(100), unique=True, nullable=False)
    transactiontime = db.Column(db.DateTime, nullable=False)
    referencenumber = db.Column(db.String(100), nullable=True)
    orderId = db.Column(db.String(100), nullable=True)
    terminalCode = db.Column(db.String(100), nullable=True)
    subTerminalCode = db.Column(db.String(100), nullable=True)
    serviceCode = db.Column(db.String(100), nullable=True)
    urlLink = db.Column(db.Text, nullable=True)
    sign = db.Column(db.Text, nullable=True)
