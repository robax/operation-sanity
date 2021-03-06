##Welcome to Operation Sanity!

Operation Sanity is a set of behavior driven development tests for <a href="https://github.com/iPlantCollaborativeOpenSource/atmosphere">Atmosphere</a> implemented using <a href="https://github.com/behave/behave">Behave</a>, <a href="https://github.com/ggozad/behaving">Behaving</a>, and <a href="https://github.com/vishalm/behave-parallel">Behave-parallel</a>.

This repo provides tests for:

* Creating and deleting projects
* Launching all 5 featured images on all 3 providers
* Ensuring those instances launch 
* Reporting and deleting featured images
* Creating, reporting, and deleting volumes
* Creating and deleting links
* Testing web shell operation 
* Submitting resource request ticket
* Submitting Atmosphere feedback

##How to run:

###Installation: 
1. Ensure you have firefox 46 installed (47+ won't work)
1. Clone this repo
1. Go to root of the project
1. Create a virtual env 

* `virtualenv env`
* `source env/bin/activate`
* `pip install -r requirements.txt`

Additionally, you'll also need to add these lines to your ~/.bash_profile:  
`export SANITYUSER=myAtmoUsername`  
`export SANITYPASS=myAtmoPassword`  
`export SANITYURL="https://atmo.iplantcollaborative.org"`  
The URL can be any installation of Atmosphere.


Then source it:  
`source ~/.bash_profile`

###Run tests:
The test suite has been configured to be run using:  
`time bash run.bash 2`  
where 2 is the max number of processes you want run.

Alternatively, the script can be used as a guidebook for running each step of the test suite individually. Open run.bash in a text editor and manually copy each step into the command line. You'll have to manually change the `$PROCESSES` variable to the number of processes you want to run, usually 2-4.

###Reference:
To run a single feature:  
`behave launch.feature`

To run multiple scenarios in parallel (good for outlines):  
`behave --processes 4 --parallel-element scenario`

To run multiple features in parallel:  
`behave --processes 4 --parallel-element feature`

To run a single scenario:  
`behave -n "Attach a volume"`

To run a single scenario within an outline:
`behave features/launch.feature:38`  
where 38 is the line number.

## FAQ:

**Q.** The script breaks after a "This application is not authorized to use CAS" page loads after logging in.  
**A.**  Restart your tests. I'm not sure why this happens.

**Q.** I get an error:  
`Instance could not be launched 504:`
`Multiple connection attempts to the provider`
`29ee80ff-ab20-441e-a752-da682e1d40e3 have failed. `
`Please try again later.`  
**A.** This usually happens when you run the script with 4 or more processes. Try re-running run.bash with an argument of 2.

**Q.** My tests are erroring out with:
`Element is not clickable at point (764.683349609375, 25). Other element would receive the click: <div style="display: block;" class="modal fade in" data-reactid=".2"></div>`  
**A.** This is caused by a modal that says: `Looks like you have some resources that aren't in a project!`  This happens when you leave the page soon after launching an instance, or you delete a project soon after deleting an instance within that project. If the problem persists you can add `I wait for 30 seconds` steps after launching or deleting an instance.

**Q.** Why not use personas?  
**A.** Behave-parallel doesn't have `context.execute_steps` implemented, which personas make heavy use of. This is also why some steps in steps.py are enormous.

##To do:
- test ssh functionality in test.feature using paramiko