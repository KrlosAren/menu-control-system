"""
    Tasks for menus module

    task send slack message to a specific channel
    the variables comes from .ENV file is the core
    configure your own variables with the slack token and channel

    """

# celery
from django.contrib import messages
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
        return response.data
    except SlackApiError as error:
        return error

