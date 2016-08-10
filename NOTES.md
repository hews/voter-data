See also:

- http://www.cleveland.com/datacentral/index.ssf/2012/11/barack_obama_won_big_cuyahoga.html?appSession=20724816959489532556425073346327911537640316275916168622255190561507575699273089288924838203228609929312921238533585650475971281
- https://developers.google.com/civic-information/
- http://www.reuters.com/article/us-usa-votingrights-ohio-insight-idUSKCN0YO19D (fun test to run: strike all voters who have not voted in x years)
- http://www.cleveland.com/open/index.ssf/2016/04/ohio_secretary_of_state_jon_hu_6.html
- http://www.wlwt.com/news/three-changes-in-ohios-voting-rules-from-2012-to-2016/38020054
- https://www.census.gov/geo/maps-data/data/tiger-cart-boundary.html
- https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html

Project:

check for parallel redis use… do a profile of different parallelization rules for loading data (multiple huge CSVs) into a redis store, followed by a big ETL to a SQL store.

testing should include a “fingerprinting” hash of the data… (https://github.com/puleos/object-hash) for testing?

—

A series of data pipelines, strung together by data services.

All involve an election: Vote 2016!

You are on the data team for some candidate in a primary, and your district is NE Ohio (or all of Ohio)...

http://scrapy.org/
http://boe.cuyahogacounty.us/en-US/citydownloads.aspx

1. Coalesce data concerning the area: voter rolls, leftover data from previous cycle, census data, and polls, to build a Base Voter Model for it all MariaDB. Pipeline (ETL) 1.

2. Create an Organization Model to manage the precincts: captains, managers, volunteers, events.

2. Begin to gather canvassing rolls from your various precinct captains, and integrate them in to the Base Voter Model. Pipeline (ETL) 2/3 for in-person or phone.

Market Model of media markets?

3. Create a dashboard about the canvassing operation, with targets and history. Pipeline (CEP) 4.

4. Create an analysis of precincts to determine relative performance. Metrics include contacts per day by type and by manager, top contacters by type, best hours by neighborhood, voter profile, and type, clusters of undecideds, issues by voter profile, etc. Print out and push metrics to different store. Pipeline (Analysis & ETL) 5.

5. Create a system where the dashboard and metrics are updated continuously as the canvases come in.

6. Merge metrics and Base Model to plan upcoming activities: simple canvas, sway canvas / VIP visit, phone blitz, house meeting (get volunteers), ad buy. Pipeline (Analysis & ETL) 6.

7. GOTV (constant updates and new lists)...

- voter rolls
- geodata (city, county, township shape files, and maps)
- election data and civic data (geodata about political divisions) for 2 previous general elections, and most recent midterm
- census / demographic data
- cook partisan voter index
- polls and polling data for the 2016 election (538)
- issues models and data?
- …
