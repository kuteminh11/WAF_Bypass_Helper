import re

from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOW


def tamper(payload, **kwargs):
    """
    Replaces space character after SQL statement with a valid random blank character.
    Afterwards replace character = with LIKE operator

    Requirement:
        * Blue Coat SGOS with WAF activated as documented in
        https://kb.bluecoat.com/index?page=content&id=FAQ2147

    Tested against:
        * MySQL 5.1, SGOS

    Notes:
        * Useful to bypass Blue Coat's recommended WAF rule configuration

    >>> tamper('SELECT id FROM users WHERE id = 1')
    'SELECT%09id FROM%09users WHERE%09id LIKE 1'
    """

    def process(match):
        word = match.group('word')
        if word.upper() in kb.keywords:
            return match.group().replace(word, "%s%%09" % word)
        else:
            return match.group()

    retVal = payload

    if payload:
       # i dont know what is KB
       #  retVal = re.sub(r"\b(?P<word>[A-Z_]+)(?=[^\w(]|\Z)", lambda match: process(match), retVal)
        retVal = re.sub(r"\s*=\s*", " LIKE ", retVal)
        retVal = retVal.replace("%09 ", "%09")
        retVal = 'it is blueoat - Need help!!!'

    return retVal