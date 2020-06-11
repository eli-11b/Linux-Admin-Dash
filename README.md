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

## The overview shows a nice and clean responsive display. 
<p>
Information about users, IP addresses, disk space, processes and environment variables can are displayed. 
</p>
<img src="images/screenshot-overview.png">
<br>

## The web application is responsive so it will work with different screen sizes.

<img src="images/screenshot1-responsive.png">

## Cron jobs

<p>
    <h3>The application will allow the user to visually:</h3> 	
	<br><h4>Create Cron Job</h4>
	<h4>Backup Cron Jobs</h4>
	<h4>Import Cron Jobs</h4>
	<h4>Export Cron Jobs</h4>
	<h4>Edit Cron Jobs</h4>
	<h4>Stop Cron Jobs</h4>
	<h4>Delete Cron Jobs</h4>

<img src="images/screenshot-cronjobs.png">

</p>


## Future Work

<p> 
All buttons need to be wired. I will have a modal display for the submitting and confirming input and commands when a button is clicked. The cronjobs page is just the UI. Also, remote connectivity and remote machine control will be added to allow for remote administration.
  <br>
  <br>-Add a place for launchctl -list for apple machines
  <br>-Add a place for systemctl --type=service for linux machines
  <br>-Add a place for iostat
  <br>-Add a place for free (memory)
  <br>-Add a place for network monitoring
  
</p>
