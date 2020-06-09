import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask, render_template, request, url_for, Response

url='localhost:5000'

app = Flask(__name__, template_folder="templates", static_folder="assets")

# return the home page
@app.route('/',methods=['GET',])
def home():
	return render_template("index.html")

#return the system stats page
@app.route('/system_stats',methods=['GET',])
def system_stats():
"""
This function runs the bash scripts and sends the output to the stats page to their respective areas
and renders the stats.html template. 
"""
	
	uptime= check_output(['./uptime.sh']).decode('utf-8')
	cronjobs= check_output(['./cronjobs.sh']).decode('utf-8')
	currentIPs= check_output(['./currentIPs.sh']).decode('utf-8')
	current_users= check_output(['./current_users.sh']).decode('utf-8')
	disk_space= check_output(['./disk_space.sh']).decode('utf-8')
	env_variables= check_output(['./env_variables.sh']).decode('utf-8')
	processes= check_output(['./processes.sh']).decode('utf-8')
	return render_template("stats.html",
							uptime=uptime,
							cronjobs=cronjobs,
							currentIPs=currentIPs,
							current_users=current_users,
							disk_space=disk_space,
							env_variables=env_variables,
							processes=processes
							)

app.run(debug=True)
