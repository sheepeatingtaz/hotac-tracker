# Heroes of the Aturi Cluster - Campaign Tracker
Campaign Tracker for Heroes of The Aturi Cluster (http://dockingbay416.com/campaign/)

## My Plans
These are grandiose plans, and I imagine I will add more features to this wish list as time goes on! The first 'usable' release will contain the bare minimum to create a user, pilot, squadron campaign and run a mission.

## Users
Each user can have many Pilots. Pilots can be active in many campaigns

## Pilots
Each user can have many pilots, storing name, call-sign, ship type, purchased upgrades (using a scaled back logic like popular squadron builders)
Each pilot can configure several loadouts depending on Pilot Skill and ship type which can be activated for missions

## Squadrons
Each user can be a member of many squadrons, and can be an Officer (admin rights for the squadron) or Pilot (general member). Officers can invite other Pilots, and promote them to OFficers. Squadrons can be open to anyone or invite only.

## Campaigns
Each squadron can have many campaigns, officers can create new campaigns. 
On creating a campaign, the creator (Campaign Commander) chooses standard (all 5 story arcs) or short (3 story arcs, randomly selected or creator choice) and whether to include the introductory mission.
When a campaign is in progress, the system can select the next mission (as per the HotAC rules guide) or the Campaign Commander can select. 

## Missions
Missions have 4 screens, 'Briefing', a 'Pilot' screen and a 'Control' screen, and finally 'Debrief'

### Briefing
Displays the mission briefing as per the HotAC campaign guide, including setup map.
Can optionally display the Enemy AI (adjusted for the number of pilots taking part), depending on the choice of the campaign commander

### Pilot Screen
Details the Current mission status:
* Current Turn (Campaign Commander has a button to increment)
* Kill Stats, by ship type (automatically adding ship types as they appear in the setup guide as per the turn you are on)
* Damage Dealt incrementer
* Other XP features, as determined by the mission (e.g. Protect Action)
* End Mission button for Campaign Commander

### Control Screen
Shows an up-to-date summary of all pilots and enemy ships in play

### Debrief
Like the control screen, but the Campaign Commander can log victory status and assign mission bonus XP (from the campaign guide)

## About the code
I'm writing this in Django, because I like it. It currently is using a sqlite db, because I'm still testing, but it will run with any database that Django supports. I will be using Django Channels for the live updates in missions, so to deploy you will eventually need a redis server too.
When the first alpha version is ready, I will run from a free Heroku instance, and will therefore update the repository & instructions on how to do so.

## Contributing
Yes please! This is a hobby. I love playing X-wing, and I love experimenting in code, so this will eventually help me with both. I am aware of my shortfalls (especially in UX/UI) and welcome any help that people want to give.
A snazzy name would be good too!

## Disclaimer
I have not had permission (nor have I sought it) from the folks who create Heroes of the Aturi Cluster to do this - I am doing it as a fan of the campaign they have created. Hopefully they won't mind, but obviously it's their creation, so if they tell me to take it down at any point I will. 