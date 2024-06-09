<h1>Postmortem </h1>

Upon the release of Holberton School's System Engineering & DevOps project , an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server resulted in 500 Internal Server Errors instead of the expected HTML response.

<h2> Issue Summary </h2>
The Apache web server was returning a 500 Internal Server Error due to a typo in a filename within the WordPress configuration. This prevented the server from correctly locating and loading the necessary file, causing the error.

<h2>Timeline</h2>
00:00 PST: Initial release of the project.

11:30 PST: Problem noticed.

11:45 PST: The typo was identified and corrected.

11:50 PST: The server was verified to be functioning correctly, returning the expected HTML content.

<h2>Root Cause and Resolution </h2>
Root Cause: A typo in the WordPress wp-settings.php file caused Apache to fail in locating the necessary file, resulting in a 500 Internal Server Error. Specifically, the file class-wp-locale.phpp was referenced instead of class-wp-locale.php.
Resolution: The typo in the filename was corrected by removing the trailing 'p', allowing Apache to correctly locate and load the file.

<h2>Corrective and Preventative Measures </h2>
Immediate Fix: Corrected the typo in the wp-settings.php file manually.
Automation with Puppet: Created a Puppet manifest to automate the renaming of the file, ensuring consistency.
