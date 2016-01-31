import re
import requests


endpoints = {
    'twitter': {
        'scheme': 'http*://twitter.com/*/status/*',
        'endpoint': 'https://api.twitter.com/1/statuses/oembed.json',
        'example': 'https://twitter.com/dangayle/status/284836686171627521'
    }
}


def get_endpoint(url):
    """Get oembed endpoint for a url."""

    for key, values in endpoints.iteritems():

        re_values = str(
            values['scheme']).replace('.', '\.').replace('*', '.*?')
        values['scheme'] = re.compile(re_values)

        if values['scheme'].match(url):
            return values['endpoint']


def get_oembed(url, endpoint, width=800, format="json"):
    """Make oembed request to provider."""

    params = {
        'url': url,
        'width': width,
        'format': format
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None


def gist(url, endpoint):
    return {'html': endpoint.format(url)}


def route(url):
    """Route url to proper embed method."""

    route = None
    e = get_endpoint(url)
    if e == endpoints['gist']['endpoint']:
        route = gist(url, e)
    else:
        route = get_oembed(url, e)
    return route


def oembed(url):
    """Return html from embed request."""

    response = route(url)
    return response['html'].encode('utf-8') if response else url
