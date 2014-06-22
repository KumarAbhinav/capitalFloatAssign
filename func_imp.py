
def apply_modify(jobID,application,associateddict):
    #redisInstance = redis.StrictRedis(host = app.config["SESSION_REDIS_HOST"],port = app.config["SESSION_REDIS_PORT"],db=10)
    if 1: #(request.method == 'POST'):
        #logging.info(request.form)
        #application={
        #    "pid":session["pid"],
        #    "fb_id":session["fb_id"],
        #    "resume_id":request.form.get('resume_id'),
        #    "email": request.form.get('email'),
        #    "mobile": request.form.get('tel'),
        #    "location": request.form.get('location',''),
        #    "job_id": jobID,
        #    "experience": str(request.form.get('experience_year'))+'.'+str(request.form.get('experience_month')),
        #    "industry": request.form.get('industry',0),  # optional
        #    "functional_area": request.form.get('functional_area',0),
        #    "salary":int(request.form.get("salary_lakhs",0))*100000+int(request.form.get("salary_thousands",0))*1000
        #}        
        status, error = validateJobApplicationDetails(application)
        if status == False:
            return jsonify({'body': {"status": False, "message": error}})

        # If Referral.. send that parameter as well
        #if(not request.form.get('referral',None)==None):
        #    try:
        #        application['referral'] = int(request.form.get('referral'))
        #    except Exception, e:
        #        logging.debug('non int referral id is passed. Neglecting this id'+str(e))
        #        pass
        
        # adding the job source coming from
        #if(not request.args.get('jobintro', None) == None):
        #    application['source'] = 2
        #elif(not request.args.get('jobdirect', None) == None):
        #    application['source'] = 1
        #else:
        #    application['source'] = 3

        #Get Application source Params
        #application['app_src_params']=analytics.getApplicationSourceParams()
        if JobApplicationDAO.apply_job.delay(data=application, is_social_bar=False, partner_response=None):
            result = {'status': 200, 'body': {
                #"status": True, "message": "Your application has been submitted.", "location": request.args.get('location', 'job')
                "status": True, "message": "Your application has been submitted.", "location": associateddict.get('location', 'job')
            }}
            #analytics.add_analytics_data(Constants.AN_REDIS_JOB_APPLIED,session.get("fb_id",0))
            analytics.add_analytics_data(Constants.AN_REDIS_JOB_APPLIED,application.get("fb_id",0))
            #if(request.args.get('referrer')):
            if(associateddict.get('referrer')):
                result['body']['referrer'] = associateddict.get('referrer')
            return jsonify(result)
        else:
            return jsonify({'body': {"status": False,"message": "Failed to Apply to Job"}})

        #===================
        is_mobile = 0
        #redisInstance = redis.StrictRedis(host = app.config["SESSION_REDIS_HOST"],port = app.config["SESSION_REDIS_PORT"],db=10)
        if(request.method == 'POST'):
            #logging.info(request.form)
            #application={
        #    "pid":session["pid"],
        #    "fb_id":session["fb_id"],
        #    "resume_id":request.form.get('resume_id'),
        #    "email": request.form.get('email'),
        #    "mobile": request.form.get('tel'),
        #    "location": request.form.get('location',''),
        #    "job_id": jobID,
        #    "experience": str(request.form.get('experience_year'))+'.'+str(request.form.get('experience_month')),
        #    "industry": request.form.get('industry',0),  # optional
        #    "functional_area": request.form.get('functional_area',0),
        #    "salary":int(request.form.get("salary_lakhs",0))*100000+int(request.form.get("salary_thousands",0))*1000
        #}     
            #application={
                #"pid":session["pid"],
                #"fb_id":session["fb_id"],
                #"resume_id":request.form.get('resume_id'),
                #"email": request.form.get('email'),
                #"mobile": request.form.get('tel'),
                #"location": request.form.get('location',''),
                #"job_id": jobID,
                #"experience": str(request.form.get('experience_year'))+'.'+str(request.form.get('experience_month')),
                #"industry": request.form.get('industry',0),  # optional
                #"functional_area": request.form.get('functional_area',0),
                #"salary":int(request.form.get("salary_lakhs",0))*100000+int(request.form.get("salary_thousands",0))*1000,
                #"notification_hash": request.args.get('hash', '')
            #}
            application["is_mobile"]=is_mobile    
            status, error = validateJobApplicationDetails(application, is_mobile)        
            if status == False:
                return 0#jsonify({'body': {"status": False, "message": error}})        
            # If Referral.. send that parameter as well            
            #if(not request.form.get('referral',None)==None):
                #try:
                    #application['referral'] = int(request.form.get('referral'))
                #except Exception, e:
                    #logging.debug('non int referral id is passed. Neglecting this id'+str(e))
                    #pass
            
            #if(not request.args.get('jobintro', None) == None):
                #application['source'] = 2
            #elif(not request.args.get('jobdirect', None) == None):
                #application['source'] = 1
            #elif(not request.args.get('fb_message', None) == None):
                #application['source'] = 3
            #else:
                #application['source'] = 4

            #Get Application source Params
            #application['app_src_params']=analytics.getApplicationSourceParams()
            
            if is_mobile:
                src_params={"mp_asid":24,"mp_astag":"MOBILE"}
                application['app_src_params']= urllib.urlencode(src_params);

            if JobApplicationDAO.apply_job.delay(data=application, is_social_bar=False, partner_response=None):
                result = {'status': 200, 'body': {
                    #"status": True, "message": "Your application has been submitted.", "location": request.args.get('location', 'job')
                    "status": True, "message": "Your application has been submitted.", "location": associateddict.get('location', 'job')
                }}
                #analytics.add_analytics_data(Constants.AN_REDIS_JOB_APPLIED,session.get("fb_id",0))
                analytics.add_analytics_data(Constants.AN_REDIS_JOB_APPLIED,application.get("fb_id",0))
                #if(request.args.get('referrer')):
                if(associateddict.get('referrer')):
                    result['body']['referrer'] = associateddict.get('referrer')
                return 1#jsonify(result)
            else:
                return 0#jsonify({'body': {"status": False,"message": "Failed to Apply to Job"}})