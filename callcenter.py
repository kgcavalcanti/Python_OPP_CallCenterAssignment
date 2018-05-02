from datetime import datetime
import itertools
class Call(object):
	newid = itertools.count().next
	def __init__(self, caller_name, caller_phone, reason):
		self.id = CallCenter.newid()
		self.caller_name = caller_name
		self.caller_phone = caller_phone
		self.timeCall = datetime.now().strftime('%Y/%m/%d %I:%M %p')
		self.reason = reason
		self.call = {
			'id': self.id,
			'caller_name': self.caller_name,
			'caller_phone': self.caller_phone,
			'timeCall': self.timeCall,
			'reason': self.reason,
		}
	def display(self):
		print ""
		print "ID : {}".format(self.call['id'])
		print "Caller's Name : {}".format(self.call['caller_name'])
		print "Caller's Phone : {}".format(self.call['caller_phone'])
		print "Time of call : {}".format(self.call['timeCall'])
		print "Reason for call : {}".format(self.call['reason'])
		return self

class CallCenter(Call):
	def __init__(self, caller_name, caller_phone, reason):
		super(CallCenter,self).__init__(caller_name, caller_phone, reason)
		self.calls = []
		self.queue = len(self.calls)


	def add(self):
		self.calls.append(self.call)
		print self.calls
		return self

	def remove(self):
		self.calls.pop(0)
		print self.calls
		return self

	def info(self):
		for x in self.calls:
			print ""
			print "Caller's Name : {}".format(x['caller_name'])
			print "Caller's Phone : {}".format(x['caller_phone'])
			print "The queue now has {} postions".format(len(self.calls))
		return self

call1 = CallCenter("katia","12345678", "bla bla")
call2 = CallCenter("DJ", "12345678", "doesn't work")
call3 = CallCenter("Dejalma", "12345678", "broken")
call1.add()
call2.add()


