from jenkinsapi.jenkins import Jenkins

# Connect to Jenkins using its URL and API token
jenkins = Jenkins('http://52.50.112.255:8081/', username='expleo', password='http://52.50.112.255:8081/')

# Get the total number of deployments per day
deployments_job_name = 'EasyBuggy'
deployments_job = jenkins.get_job(deployments_job_name)
deployments_count = deployments_job.get_last_build().get_number()

# Get the change fail rate (CFR)
cfr_job_name = 'cfr-job'
cfr_job = jenkins.get_job(cfr_job_name)
cfr_count = cfr_job.get_last_build().get_actions()['totalCount']

# Get the lead time for changes (LT)
lt_job_name = 'lt-job'
lt_job = jenkins.get_job(lt_job_name)
lt_time = lt_job.get_last_build().get_duration() / 60

# Get the mean time to recover (MTTR)
mttr_job_name = 'mttr-job'
mttr_job = jenkins.get_job(mttr_job_name)
mttr_time = mttr_job.get_last_build().get_duration() / 60

# Print the metrics
print('Deployments per day: {}'.format(deployments_count))
print('Change fail rate: {}'.format(cfr_count))
print('Lead time for changes: {} minutes'.format(lt_time))
print('Mean time to recover: {} minutes'.format(mttr_time))
