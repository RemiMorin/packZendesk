# Zendesk Integration Pack

This pack allows integration with Zendesk service.

##Actions

###Create ticket

Command:
st2 run packZendesk.create_ticket ticket_title=XXX ticket_description=XXX userName=XXX userEmail=XXX

ChatOps command:
!zendesk create ticket title XXX description XXX username XXX email XXX

###Close ticket

Command:
st2 run packZendesk.close_ticket ticket_id=XXX

ChatOps command:
!zendesk close ticket number XXX

###Update ticket

Command:
st2 run packZendesk.update_ticket ticket_id=XXX comment=XXX

ChatOps command:
!zendesk update ticket XXX comment XXX

###Search

Search string uses the zendesk API:https://developer.zendesk.com/rest_api/docs/core/search

Command:
st2 run packZendesk.search_ticket search_string=XXX

ChatOps command:
!zendesk search ticket XXX


##Installation
st2 run packs.install packs=packZendesk repo_url=https://github.com/RemiMorin/packZendesk.git


##Configuration
edit the file /opt/stackstorm/packs/packZendesk/config.yaml to set the proper zendesk credentials.
###config.yaml
  url: "https://XXX.zendesk.com"
  user: "XXX"
  password: "XXX"


##Setup dev environnement:

clone the repository

in the project repository do the following command to create virtual env and install requirements:

./doit_wrapper.sh -i

you can now run unit tests:

./doit_wrapper.sh -t run_unit_test

all setup!