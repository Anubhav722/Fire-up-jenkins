import datetime
import unittest
today = datetime.datetime.now()
def dated(replace_date):
	x=[]
	two_days_ago = replace_date - datetime.timedelta(days=2)
	t1 = str(replace_date.date().day) + str(replace_date.strftime('%B')[0:3]) + '_old'
	x.append(t1.lower())
	t2 = str(two_days_ago.date().day) + str(two_days_ago.strftime('%B')[0:3]) + '_new'
	x.append(t2.lower())
	return x
	
class TestDateMethods(unittest.TestCase):
	
	def tests(self):
		replace_date = today.replace(day=15, month=1)
		x=dated(replace_date)
		self.assertEqual('15jan_old', x[0])
		self.assertEqual('13jan_new', x[1])
		
		replace_date = today.replace(day=15, month=2)
		x=dated(replace_date)
		self.assertEqual('15feb_old', x[0])
		self.assertEqual('13feb_new', x[1])
		
		replace_date = today.replace(day=15, month=3)
		x=dated(replace_date)
		self.assertEqual('15mar_old', x[0])
		self.assertEqual('13mar_new', x[1])
		
		replace_date = today.replace(day=15, month=4)
		x=dated(replace_date)
		self.assertEqual('15apr_old', x[0])
		self.assertEqual('13apr_new', x[1])
		
		replace_date = today.replace(day=15, month=5)
		x=dated(replace_date)
		self.assertEqual('15may_old', x[0])
		self.assertEqual('13may_new', x[1])
		
		replace_date = today.replace(day=15, month=6)
		x=dated(replace_date)
		self.assertEqual('15jun_old', x[0])
		self.assertEqual('13jun_new', x[1])
		
		replace_date = today.replace(day=15, month=7)
		x=dated(replace_date)
		self.assertEqual('15jul_old', x[0])
		self.assertEqual('13jul_new', x[1])
		
		replace_date = today.replace(day=15, month=8)
		x=dated(replace_date)
		self.assertEqual('15aug_old', x[0])
		self.assertEqual('13aug_new', x[1])
		
		replace_date = today.replace(day=15, month=9)
		x=dated(replace_date)
		self.assertEqual('15sep_old', x[0])
		self.assertEqual('13sep_new', x[1])
		
		replace_date = today.replace(day=15, month=10)
		x=dated(replace_date)
		self.assertEqual('15oct_old', x[0])
		self.assertEqual('13oct_new', x[1])
		
		replace_date = today.replace(day=15, month=11)
		x=dated(replace_date)
		self.assertEqual('15nov_old', x[0])
		self.assertEqual('13nov_new', x[1])
		
		replace_date = today.replace(day=15, month=12)
		x=dated(replace_date)
		self.assertEqual('15dec_old', x[0])
		self.assertEqual('13dec_new', x[1])
		
if __name__ == '__main__':
    unittest.main()

