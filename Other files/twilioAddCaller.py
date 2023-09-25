from twilio.rest import Client

class PhoneNumberVerification:
    def __init__(self, account_sid, auth_token, service_sid):
        self.client = Client(account_sid, auth_token)
        self.service_sid = service_sid

    def start_verification(self, phone_number, channel='sms'):
        """
        Start the phone number verification process.
        """
        verification = self.client.verify.services(self.service_sid).verifications.create(
            to=phone_number, 
            channel=channel
        )
        return verification.status

    def complete_verification(self, phone_number, verification_code):
        """
        Complete the phone number verification process.
        """
        verification_check = self.client.verify.services(self.service_sid).verification_checks.create(
            to=phone_number,
            code=verification_code
        )
        return verification_check.status

if __name__ == "__main__":
    # Your Twilio credentials
    ACCOUNT_SID = 'ACd607e2f86a57f692c81867be2f0b351f'
    AUTH_TOKEN = 'acda06ff971cc152136b2355c24b9a11'
    SERVICE_SID = 'your_verify_service_sid_here'

    verifier = PhoneNumberVerification(ACCOUNT_SID, AUTH_TOKEN, SERVICE_SID)
    
    phone_number = input("Enter phone number (format: +1234567890): ")
    verifier.start_verification(phone_number)
    code = input("Enter the verification code you received: ")
    result = verifier.complete_verification(phone_number, code)

    if result == 'approved':
        print("Phone number verified successfully!")
    else:
        print("Failed to verify the phone number.")
