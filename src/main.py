import asyncore
import logging
import smtpd

import dynaconfig
import telegram_sender

SMTP_HOSTNAME = dynaconfig.settings["SMTP"]["HOSTNAME"]
SMTP_PORT = dynaconfig.settings["SMTP"]["PORT"]


class FrontierSMTPServer(smtpd.SMTPServer):

    def process_message(
        self, peer, mailfrom, rcpttos, data, mail_options=None, rcpt_options=None
    ):
        logging.info(f"Receiving connection from: {peer} - message length: {len(data)}")
        logging.info(f"Message addressed from {mailfrom} to {rcpttos}")
        logging.info(data)
        telegram_sender.send_mail_to_telegram(data)
        # TODO smtp parsing


if __name__ == "__main__":
    # TODO check if hostname has to be 0.0.0.0 because of docker launch
    server = FrontierSMTPServer((SMTP_HOSTNAME, SMTP_PORT), None)

    asyncore.loop()
