# cssq

Filter HTML with a CSS query. Because regular expressions on HTML output is never good. And one-liner scraping is awesome.

You can pass standard input or you can use a URI in the arguments to `cssq`. Note however it is probably in most cases to copy a `curl` or similar command and pipe to `cssq` to let cURL handle all the heavy lifting (cookies, data, request method, etc).

If you pass a URI to `cssq` the request is made via GET method and nothing beyond this is supported such as authentication or cookies.

# Examples

## Use a URL

```bash
cssq 'http://www.google.com' 'style'
```

Output (truncated):

```
<style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{p...
```

Note that if only one matching element is found, that element is printed (index 0). If more than one element is found, a set of strings is printed in JSON format.

If JSON is printed, you may want to consider piping to `jq` for even more complex filtering. Example getting the first element:

```bash
./cssq 'https://stackoverflow.com/' 'li' | jq .[0]
```

Output (truncated):
```
"<li>\n                        <div class=\"related-links\">..."
```

## Piping from cURL

You may want to do this to get *your* content as opposed to the general anonymous user. For example, your favourites list on YouTube.

To do this easily in Chrome, open the Developer Tools then view the Network tab. Go to your Favourites page and then under the list of downloaded items the first item should be the page itself. You can right-click this item and choose *Copy as cURL* (note the command may be long. Then paste that into your terminal and pipe it to `cssq`. You will see a set of `<a>` tags, JSON encoded.

```bash
curl 'https://www.youtube.com/playlist?list=****' \
    -H 'pragma: no-cache' \
    -H 'dnt: 1' \
    ...  | cssq '#pl-video-table .pl-video-title-link'
```
