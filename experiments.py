from planout.ops.random import *
from planout.experiment import SimpleExperiment

class UniversalExperiment(object):
  
   def run(self, exp, user_id, data):
   		NamedExperiment = SimpleExperiment
		NamedExperiment.name = exp
	
		class Experiment(NamedExperiment):
  			def assign(self, params, user_id):

				 params.version = UniformChoice(
     			 	choices=data['variants'],
      			 	unit=user_id)
		
  		f = Experiment(user_id=user_id)
  		return f.get('version')
   def log(self, log_event, user_id, data):
   		ExperimentLogger = SimpleExperiment
		ExperimentLogger.name = 'eventlogger'
	
		class Experiment(ExperimentLogger):
  			def assign(self, params, user_id):
  				pass
		
  		f = Experiment(user_id=user_id)
  		f.log_event(log_event)
  		
		