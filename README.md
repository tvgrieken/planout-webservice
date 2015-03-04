# PlanOut Webservice

This is a simple webservice for [PlanOut](http://facebook.github.io/planout/) and currenly supports equal distibuted A/B/n tests.
The service features posting a new test, get instant assignment and the logging of success events.



### Posting a new test

Run the server 

```
python api.py
```
Define the variants as in the following JSON format:

``` json
{ 
	"variants" : [
    	    "nameofvariant1", 
      		"nameofvaraint2"
]}
```
Unlimited amount of variants can be defined. 
Post to the following endpoint with the JSON in the request body

```
/v1/assign/exampletestname/someuserid12214
```

Notice the return response with a random assignment:

``` json
{
	"expirment_name": "exampletestname",
	"variant": "nameofvariant1",
	"user_id": "someuserid12214"
}
```

Test names should be lowercase [a-z], user_id can be anything.

### Logging success events
Post events to following endpoint. Events will be logged in a file called 'eventlogger.log' since success events can belong to multiple tests.
```
/v1/log/exampleventname/someuserid12214
```