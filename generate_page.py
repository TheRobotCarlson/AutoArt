import dominate
from dominate.tags import *

from urllib import parse
import glob


def get_url(image_name):
    base_url = "https://www.zazzle.com/api/create/"
    store_id = "at-238377813278186853"

    _image_url = "https://raw.githubusercontent.com/TheRobotCarlson/styled-images/master/" + image_name

    url_params = {
        "ax": "Linkover",
        "pd": "168818644649310760", # product id
        "ed": "true",
        "ic": "",
        "tc": "",
        "image1": _image_url
    }

    _query_url = \
        base_url + \
        store_id + \
        "?" + \
        parse.urlencode(url_params)

    return _query_url, _image_url


doc = dominate.document(title='Jump to page')

# with doc.head:
#     link(rel='stylesheet', href='style.css')
#     script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in ['home', 'about', 'contact']:
            li(a(i.title(), href='/%s.html' % i))

    with div(id="images"):

        for i in glob.glob("images/*iteration_9.png"):
            query_url, image_url = get_url(i.replace("\\", "/"))

            with a(href=query_url, target="_blank"):
                img(src=image_url)

        for i in glob.glob("images/*iteration_6.png"):
            query_url, image_url = get_url(i.replace("\\", "/"))

            with a(href=query_url, target="_blank"):
                img(src=image_url)

        for i in glob.glob("images/*iteration_3.png"):
            query_url, image_url = get_url(i.replace("\\", "/"))

            with a(href=query_url, target="_blank"):
                img(src=image_url)

    with div():
        attr(cls='body')
        p('Lorem ipsum..')

with open("index.html", "w") as f:
    f.write(doc.render())

print(doc)
