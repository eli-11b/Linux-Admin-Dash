import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask, render_template, request, url_for, Response
import getpass
import webbrowser as wb
import os

app = Flask(__name__, template_folder="templates", static_folder="assets")



@app.route('/',methods=['GET',])
def home():
	""" This function renders the index template"""

	return render_template("index.html")


#System Statistics
@app.route('/system_stats',methods=['GET',])
def system_stats():
	""" This function renders the system statistics template and passes the variables to the front end. """

	user=getpass.getuser()
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
							processes=processes,
							)

#Restart Machine
@app.route('/restart_machine', methods=['POST',])
def restart_machine():
	""" this function restarts the machine after confirming in the restart modal, for linux machines adjust the sudoers file
		username ALL=NOPASSWD:/sbin/reboot	to allow reboots without password but still running sudo
	"""
	reboot= check_output(['./reboot.sh']).decode('utf-8')
	return reboot
								
#Cron Jobs
@app.route('/cronjobs',methods=['GET',])

def cronjobs():
	""" This function renders the cronjobs template."""
	return render_template("cronjobs.html")

app.run(host='0.0.0.0',debug=True)