"""
This module translates english to french and vice versa
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-09-27',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    This function translates english to french.
    It will return a dictionary
    """
    #write the code here
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """
    This function translates french to english.
    It will return a dictionary
    """
    #write the code here
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()["translations"][0]["translation"]
    return english_text
