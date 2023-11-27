from flask import Flask
from twisted.internet import reactor
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "About Flask"
resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)
if __name__ == "__main__":
    reactor.listenTCP(8080, site)
    reactor.run()

