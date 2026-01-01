from abc import ABC , abstractmethod
# AbstractStrategies
class UpiPayment(ABC):
    @abstractmethod
    def pay(self):
        pass
class CreditCardPayment(ABC):
    @abstractmethod
    def pay(self):
        pass
class DebitCardPayment(ABC):
    @abstractmethod
    def pay(self):
        pass

# ConcreteStrategies

# UPI Payments
class PhonepeUpi(UpiPayment):
    def pay(self):
        print("Payment done via Phonepe")
class GooglePayUpi(UpiPayment):
    def pay(self):
        print("Payment done via GooglePay")
class PaytmUpi(UpiPayment):
    def pay(self):
        print("Payment done via Paytm")  
# CreditCardPayments
class IcicCreditCard(CreditCardPayment):
    def pay(self):
        print("Payment done via Icici Credit Card")
class FlipkartAxisCreditCard(CreditCardPayment):
    def pay(self):
        print("Payment done via Flipkart Axis Credit Card")
class UniPayCreditCard(CreditCardPayment):
    def pay(self):
        print("Payment done via UniPay Credit Card")
# DebitCardPayments
class HdfcDebitCard(DebitCardPayment):
    def pay(self):
        print("Paying Via Hdfc Debitcard")
class IdfcDebitCard(DebitCardPayment):
    def pay(self):
        print("Paying Via Idfc Debitcard")
class SbiDebitCard(DebitCardPayment):
    def pay(self):
        print("Paying Via Sbi Debitcard")
 
        
        
# Context
class PaymentSystem:
    
    def __init__(self ,Upipayment:UpiPayment,CreditCardpayment:CreditCardPayment,DebitCardpayment:DebitCardPayment):
        self.upipayment = Upipayment
        self.creditcardpayment = CreditCardpayment
        self.debitcardpayment = DebitCardpayment
        
    def upi(self):
         self.upipayment.pay()
     
    def creditCard(self):
        self.creditcardpayment.pay()
    
    def debitCard(self):
        self.debitcardpayment.pay()
    

    # ---- Runtime/Dynamic Strategy Switchers ----
    
    # Setters
    def set_upi_payment(self, upi_payment: UpiPayment):
        """Change the UPI payment method at runtime"""
        self.upi_payment = upi_payment
        
    def set_credit_card_payment(self, credit_card_payment: CreditCardPayment):
        """Change the Credit Card payment method at runtime"""
        self.credit_card_payment = credit_card_payment
        
    def set_debit_card_payment(self, debit_card_payment: DebitCardPayment):
        """Change the Debit Card payment method at runtime"""
        self.debit_card_payment = debit_card_payment

        


# Client Code
# Initial Payment Methods
payvia = PaymentSystem(
    PhonepeUpi(),
    IcicCreditCard(),
    SbiDebitCard()
)

payvia.upi()
payvia.creditCard()
payvia.debitCard()

print("\n--- Changing payment methods dynamically ---\n")

# Change strategies at runtime
payvia.set_upi_payment(GooglePayUpi())
payvia.set_credit_card_payment(FlipkartAxisCreditCard())
payvia.set_debit_card_payment(HdfcDebitCard())

# After switching
payvia.upi()
payvia.creditCard()
payvia.debitCard()



# SRP would be violated if your PaymentSystem started doing things like:

    # Validating card details.

    # Talking to APIs (like Razorpay or Stripe).

    # Logging transactions.
    
    # Calculating discounts.

    # Managing users or order history.