from app import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    bankaccount = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)
    transType = db.Column(db.String(1), nullable=False)  # 'D' hoặc 'C'
    content = db.Column(db.String(255), nullable=False)
    transactionid = db.Column(db.String(100), unique=True, nullable=True)
    transactiontime = db.Column(db.String(100), nullable=True)
    referencenumber = db.Column(db.String(100), nullable=True)
    orderId = db.Column(db.String(19), nullable=True)
    terminalCode = db.Column(db.String(50), nullable=True)
    subTerminalCode = db.Column(db.String(50), nullable=True)
    serviceCode = db.Column(db.String(50), nullable=True)
    urlLink = db.Column(db.String(255), nullable=True)
    sign = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Transaction {self.transactionid}>"
