# Linux-Admin-Dash
<p>
Program will give the user system statistics information. Each piece of information is separated so that it is easier to read.
The other tabs will allow for viewing and editing cron jobs and database information. 
</p>

<p>
To run:
  <br> 1)Download folder
  <br> 2)Run app.py with python3
  <br> 3)open browser to <strong>localhost:5000</strong>
</p>

# System Statistics Page

### The overview shows a nice and clean responsive display. 
<p>
Information about users, IP addresses, disk space, processes and environment variables can are displayed. 
</p>
<img src="images/screenshot-overview.png">
<br>

### Modals for confirmation and setting changes. 
<p>When you press the <strong>restart</strong> button.</p> 
<img src="images/screenshot-modal.png">
<p>  When you press <strong>release</strong> IP</p>
<img src="images/screenshot-modal-releaseip.png">
<p>  When you press <strong>renew</strong> IP</p>
<img src="images/screenshot-modal-renewip.png">
<p>  When you press <strong>kill</strong> to kill a process</p>
<img src="images/screenshot-modal-killprocess.png">








# Cron jobs

<p>
  <h3>The application will allow the user to visually:</h3>

  <h4>Monitor existing cron jobs</h4>	
  <img src="images/screenshot-cronjobs.png">
	<h4>Create Cron Job</h4>
  <img src="images/screenshot-modal-newcronjob.png">
	<h4>Backup Cron Jobs</h4>
  <img src="images/screenshot-modal-backupcronjob.png">
	<h4>Import Cron Jobs</h4>
  <img src="images/screenshot-modal-importcronjob.png">
	<h4>Export Cron Jobs</h4>
  <img src="images/screenshot-modal-exportcronjob.png">
	<h4>Edit Cron Jobs</h4>
  <img src="images/screenshot-modal-editcronjob.png">
	<h4>Stop Cron Jobs</h4>
  <img src="images/screenshot-modal-stopcronjob.png">
	<h4>Delete Cron Jobs</h4>
  <img src="images/screenshot-modal-deletecronjob.png">



</p>


# Future Work

<p> 
 I will have a modal display for the submitting and confirming input and commands when a button is clicked. 
  <br>Remote connectivity and remote machine control will be added to allow for remote administration.
  <br>-Unified color pallete.
  <br>-Add a place for launchctl -list for apple machines
  <br>-Add a place for systemctl --type=service for linux machines
  <br>-Add a place for iostat
  <br>-Add a place for free (memory)
  <br>-Add a controls for disk work in disk space section.
  <br>-Add a place for network monitoring
  <br>-Add logging.
  <br>-Add settings page
  <br>Home page
  
</p>
