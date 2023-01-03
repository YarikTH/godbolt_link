"""Library interface"""
from lzstring import LZString
from urllib.parse import unquote, quote, quote_plus

# start that is expected from full godbolt link
url_begin = 'https://godbolt.org/#'

# placeholder that should be replaced with encoded source code
source_placeholder_str = '@place_the_code_here@'


def parse_url_template(url: str) -> str:
    """Parse template url and return its payload
    Full link from godbolt is expected. This link would be used to set up panel layout, compilers, options etc.
    Requirements:
    1. should start with 'https://godbolt.org/#(g|z):' that means that link is not shortened
    2. source panel should be single and contains text @place_the_code_here@
    """

    if not url.startswith(url_begin):
        raise Exception('Full godbolt link is expected')

    payload = url[len(url_begin):]

    if payload.startswith('z:'):
        payload = LZString.decompressFromBase64(unquote(payload[2:]))

    if not payload.startswith('g:'):
        raise Exception('Problem with parsing godbolt url payload')

    if source_placeholder_str not in payload:
        raise Exception(f'{source_placeholder_str} placeholder is expected in godbolt link')

    return payload


def make_godbolt_url_from_payload(payload: str) -> str:
    """Concat godbolt link and given payload"""
    return url_begin + payload


def encode_godbolt_payload(payload: str) -> str:
    """Encode godbolt payload
    Encoding was made in reverse engineering mode without seeing of specification, so it can't be a complete solution
    TODO: find a specification and make encoding properly
    """
    if not payload.startswith('g:'):
        raise Exception('Raw godbolt format is expected')

    return 'z:' + quote(LZString.compressToBase64(payload))


def place_source_code_in_payload(payload: str, encoded_source: str) -> str:
    """Place encoded source into payload instead of placeholder"""
    return payload.replace(source_placeholder_str, encoded_source)


def encode_source_code(src: str) -> str:
    """Encode source code in godbolt format
    Encoding was made in reverse engineering mode without seeing of specification, so it can't be a complete solution
    TODO: find a specification and make encoding properly
    """
    # See https://github.com/compiler-explorer/compiler-explorer/blob/main/static/url.ts

    encoded_src = quote_plus(src, safe="/ :(),*@")

    # TODO: replacing %XX patterns globally is unsafe. It can break escaped % chars.
    #       Should be done using char by char analyzing instead
    encoded_src = encoded_src.replace('%21', '!!').replace('%27', "!'")

    return encoded_src


def make_godbolt_url(url_template: str, source_code: str) -> str:
    """Makes godbolt url from specially prepared template URL and given source code"""
    encoded_source = encode_source_code(source_code)
    payload_template = parse_url_template(url_template)
    payload = place_source_code_in_payload(payload_template, encoded_source)
    encoded_payload = encode_godbolt_payload(payload)
    return make_godbolt_url_from_payload(encoded_payload)
