import logging

import requests

import dynaconfig

API_TOKEN = dynaconfig.settings["TELEGRAM"]["API_TOKEN"]
API_URL = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
CHAT_ID = dynaconfig.settings["TELEGRAM"]["CHAT_ID"]


def send_mail_to_telegram(message):
    """
    Send messages from mail to telegram
    :param message:
    :return:
    """
    try:
        response = requests.post(
            API_URL,
            json={
                "chat_id": CHAT_ID,
                "text": message,
            },
        )
        if response.status_code == 200:
            logging.info(
                f"Sent: {response.reason}. Status code: {response.status_code}"
            )
        else:
            logging.error(
                f"Not sent: {response.reason}. Status code: {response.status_code}"
            )
    except Exception as err:
        logging.error(err)


if __name__ == "__main__":
    pass
