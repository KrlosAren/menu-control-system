"""
    Celery tasks send menu message
    """

# celery
from Menus.utils import jsonString
from celery import shared_task
from celery.utils.log import get_task_logger

# slack api
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# settings
from core import settings


client = WebClient(token=settings.SLACK_API_TOKEN)
logger = get_task_logger(__name__)


@shared_task
def slack_msg(message, url):
    logger.info('Send slack message')
    menu_url = f'{url}/orders/menu/{message}'
    client = WebClient(token=settings.SLACK_API_TOKEN)
    channel = settings.SLACK_CHANNEL
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=menu_url,
        )
        return jsonString(response)
    except SlackApiError as error:
        return error