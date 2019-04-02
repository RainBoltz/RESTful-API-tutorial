import tornado.ioloop
import tornado.web
import tornado.autoreload
import os, json
import random

version = 1
subversion = 0

class ItemAHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            #someone sends a request with a data (ex. "data": 8787)...
            param = self.get_argument("data", None)
            print(param)
            
            #TODO: actions here...
            if param:
                message = "OK"
            else:
                self.set_status(400)
                message = "NOT FOUND"
                
            #return a json response 
            output = { "msg": message }
            self.write(json.dumps(output))
            
        except:
            #exception catch
            self.set_status(500)
        
        
        #in the original Tornado tutorial, we render a new page
        #self.render('index.html')
    
    def get(self):
        #GET method
        pass
      
    def push(self):
        #PUSH method
        pass
    def patch(self):
        #PATCH method
        pass
    def delete(self):
        #DELETE method
        pass
        
class ItemBHandler(tornado.web.RequestHandler):
    def get(self):
        #just another api handler
        pass

class TestWebpage(tornado.web.RequestHandler):
    def get(self):
        #testing webpage
        self.render('index.html')
        

if __name__ == "__main__":
    application = tornado.web.Application(
    	handlers=[
            ("/api/v%d.%d/ItemA"%(version, subversion), ItemAHandler),
            ("/api/v%d.%d/ItemB"%(version, subversion), ItemBHandler),
            (r"/", TestWebpage)
        ],
    	template_path=os.path.dirname(__file__),
    	static_path=os.path.join(os.path.dirname(__file__), "assets"),
        debug=True
    )
    
    the_port = 7788
    print('listen on port: %d'%the_port)
    
    application.listen(the_port)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()
