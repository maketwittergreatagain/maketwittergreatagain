

def main(query):
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  url = "https://www.googleapis.com/customsearch/v1?cx=017576662512468239146:omuauf_lfve&q=%s&key=%s"
  new_url = url % query,api_key
  res = new_url.cse().list(
      q='lectures',
      cx='017576662512468239146:omuauf_lfve',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()
