from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.autoreload
import json
from experiments import UniversalExperiment 

VERSION = 'v1'
 
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': VERSION,
                     'last_build':  date.today().isoformat() 
                     }
        self.write(response)
 
class ExperimentHandler(tornado.web.RequestHandler):
    def post(self, exp, user_id):
        data = json.loads(self.request.body)
        e = UniversalExperiment()
        response = { 
                     'expirment_name': exp,
                     'user_id' : user_id,
                     'variant' : e.run(exp, user_id, data)
                      }
        self.write(response)

class ExperimentLogHandler(tornado.web.RequestHandler):
    def post(self, log_event, user_id):
        data = json.loads(self.request.body)
        e = UniversalExperiment()
        e.log(log_event, user_id, data)
        response = { 
                     'log_event': log_event,
                     'user_id' : user_id,         
                      }
        self.write(response)

 
application = tornado.web.Application([
    
    (r"/"+VERSION+"/assign/([a-z]+)\/(.*)", ExperimentHandler), # submit testname and userid, post variants in body
    (r"/"+VERSION+"/log/([a-z]+)\/(.*)", ExperimentLogHandler), # submit testname and userid, post variants in body
    (r"/version", VersionHandler)

])
 
if __name__ == "__main__":
    tornado.autoreload.start()
    tornado.autoreload.watch('api.py')
    application.listen(10000)
    tornado.ioloop.IOLoop.instance().start()