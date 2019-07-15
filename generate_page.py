import dominate
from dominate.tags import *

from urllib import parse

base_url = "https://www.zazzle.com/api/create/"
store_id = "at-238377813278186853"

image_url = "https://raw.githubusercontent.com/TheRobotCarlson/styled-images/master/test1_at_iteration_9.png"

url_params = {
    "ax": "Linkover",
    "pd": "239612743668341078",
    "ed": "true",
    "ic": "",
    "t_image1_iid": image_url
}

query_url = \
    base_url + \
    store_id + \
    "?" + \
    parse.urlencode(url_params)

print(query_url)

doc = dominate.document(title='Jump to page')

# with doc.head:
#     link(rel='stylesheet', href='style.css')
#     script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in ['home', 'about', 'contact']:
            li(a(i.title(), href='/%s.html' % i))
    with a(href = query_url):
        img(src=image_url)
    with div():
        attr(cls='body')
        p('Lorem ipsum..')

with open("index.html", "w") as f:
    f.write(doc.render())

print(doc)
