from facebook_app.controllers import jobs
import re
import MySQLdb
import urllib
# Open database connection
db = MySQLdb.connect(host="localhost",user ="root",passwd ="",db = "mp")
cursor = db.cursor()

fin = open('apply11.txt')
while 1:
	str1 = fin.readline()
	if str1:
		if re.search('ImmutableMultiDict',str1) != None:
			application = {}
			a=str1.split('ImmutableMultiDict')
			b  =a[-1]
			c = b.rstrip("'")
			d = eval(c)			
			
			tempdict = {}
			tempdict.update(d)			
			
			application["resume_id"] = tempdict.get('resume_id')
			application["email"] = tempdict.get('email')
			application["mobile"] = tempdict.get('tel')
			application["location"] = tempdict.get('location','')			
			application["experience"] = tempdict.get('experience_year') + '.' + tempdict.get('experience_month') 
			application["industry"] = tempdict.get('industry',0)
			application["functional_area"] = tempdict.get('functional_area',0)
			application["salary"] = int(tempdict.get('salary_lakhs',0))*100000 + int(tempdict.get('salary_thousands',0))*1000

			pid =''
			#pawan !!! below is hardcoded just for testing- after # correct statement is there '10686'
			tempdict['resume_id'] = '10686'
			if tempdict.get('resume_id'):
				query1 = 'select parichay_user_id from resume where resume_id=%d'   %(int(tempdict.get('resume_id')))
							
				try:			   
				   cursor.execute(query1)			   
				   results = cursor.fetchall() 
				   pid = results[0][0]
				except:				
				   print "Error: unable to fetch pid using resume_id "

			if pid:
				pass
			else:	
				#pawan !!! below is hardcoded just for testing- after # correct statement is there	
				tempdict['email'] = 'priankar_p@yahoo.com'		
				fallback_query1 = "select parichay_user_id from parichay_contact_details where contact_email='%s'" %(tempdict.get('email'))			
				
				try:				   
				   cursor.execute(fallback_query1)				   
				   results = cursor.fetchall() 
				   pid = results[0][0]
				except:				
				   print "Error: unable to fetch pid even using contact_email"
			#we get parichay_user_id now
			pid = 3988
			if pid:
				application["pid"] = pid
				fb_id = ''
				####pawan ...below line is to be removed from actual code
				pid = 39838
				query2 = 'select fb_id from parichay_users where parichay_user_id=%d' %(pid)	
							
				try:
					cursor.execute(query2)
					results = cursor.fetchall()
					fb_id = results[0][0]
					if fb_id:
						#fb_id seen stored in applications as string...confirm
						application["fb_id"] = str(fb_id)
					else:
						print "could not fetch fb_id"
				except:				
				   print "Error: unable to fetch fb_id "
				############################
				if(tempdict.get('referral')):				
					application['referral'] = int(tempdict.get('referral'))

				

				############################
				#structure-wise just next line contains job id data
				str2 = fin.readline()
				if str2:
					th = re.search('/jobs/apply/(\d+)',str2)
					if th:
						job_id = th.groups()[0]
						application["job_id"] = job_id						
						a1  = str2.split('&')
						b1 = a1[1:]
						associateddict = {}
						for elem in b1:
							hj = elem.split('=')
							associateddict[hj[0]] = hj[1].strip()
						#print "#####################"
						if(not associateddict.get('jobintro', None) == None):
							application['source'] = 2
						elif(not associateddict.get('jobdirect', None) == None):
							application['source'] = 1
						else:
						    application['source'] = 3
						src_params={}
						for key in ['mp_asid','mp_astag']:
						    if key in associateddict.keys():
						        src_params[key]= associateddict.get(key)

						application_params = urllib.urlencode(src_params);
						application['app_src_params'] = application_params

				#function call should happen like		
				jobs.apply_modify(application["job_id"],application,associateddict)
			else:
				print "could not fetch pid----critical"

	else:
		break
fin.close()
db.close()



