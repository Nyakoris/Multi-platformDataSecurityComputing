from werkzeug.wrappers import Request,Response
from werkzeug.serving import run_simple

@Request.application
def hello(request):
    return Response("hello world")


if __name__=='__main__':
    run_simple('localhost',4000,hello)