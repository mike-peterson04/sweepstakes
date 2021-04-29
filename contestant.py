import yagmail
import mailer


class Contestant:

    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.registration_number = registration_number
        self.email = email

    def notify (self, is_winner):

        yagmail.register(mailer.manager_email,mailer.manager_password)
        if is_winner:
            message = "Congratulations you won the sweepstake"
        else:
            message = "I am sorry you didn't win the sweepstake"
        mail_client = yagmail.SMTP("mpetersondcc@gmail.com")
        mail_client.send(
            to = self.email,
            subject = "Sweepstake winner",
            contents = message
        )
