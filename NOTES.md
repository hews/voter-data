See also:

- http://www.cleveland.com/datacentral/index.ssf/2012/11/barack_obama_won_big_cuyahoga.html?appSession=20724816959489532556425073346327911537640316275916168622255190561507575699273089288924838203228609929312921238533585650475971281
- https://developers.google.com/civic-information/
- http://www.reuters.com/article/us-usa-votingrights-ohio-insight-idUSKCN0YO19D (fun test to run: strike all voters who have not voted in x years)
- http://www.cleveland.com/open/index.ssf/2016/04/ohio_secretary_of_state_jon_hu_6.html
- http://www.wlwt.com/news/three-changes-in-ohios-voting-rules-from-2012-to-2016/38020054
- https://www.census.gov/geo/maps-data/data/tiger-cart-boundary.html
- https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html

**Ideas**:

- check for parallel redis use… 
- do a profile of different parallelization rules for loading data 
  (multiple huge CSVs) into a redis store, followed by a big ETL to a 
  SQL store…
- testing should include a “fingerprinting” hash of the data created by
  Scrapy…
- Market Model of media markets? Data?

**Labs Ideas**:

1.  Coalesce data concerning the area: voter lists and demographics.
    Build a *base voter model* according to some foreseen needs. 
    **Model** 1.
2.  Collate the data and build a database of voters in MariaDB. 
    **Pipeline (ETL)** 1.
3.  Create an *organization model* to manage the precincts: captains, 
    managers, volunteers, events. Build and enter the data from a series
    of spreadsheets. **Model** 2 and **pipeline (ETL)** 2.
4.  Create a web app to allow the campaign to update their organization.
    **Web and data entry** 1.
5.  Begin to gather canvassing rolls from your various precinct captains,
    and integrate them in to the Voter & Organization databases.
    **Model** 3 will be a *voter-outreach model*, with updated 
    information. **Pipeline to two dbs (voters and org, ETL)** for 
    in-person (3) and phone (4).
6.  Create a web app to allow data entry for canvassing. 
    **Web and data entry** 2, and **pipeline (CEP)** 5.
7.  Create a dashboard about the canvassing operation, with targets and 
    history. **Model** 3, **Web and data entry** 3 and 
    **Pipeline (CEP)** 6.
8.  Create an analysis of precincts to determine relative org performance. 
    Metrics include contacts per day by type and by manager, top 
    contacters by type, best hours by neighborhood, voter profile, and 
    type, clusters of undecideds, issues by voter profile, etc. Print 
    out and push metrics to different store. **Pipeline (ETL)** 7 and
    **analysis & reporting** 1.
9.  Experiment with an analysis about what voters to target, and how.
    Merge data from the *voter-outreach model* and some analysis based on
    demographic/political data. Think about undecideds, unregistered,
    likely, propensity to vote for candidate, etc. Create a 
    *voter-target model* and update/migrate the database and web apps.
    **Analysis & reporting** 1, **model** 4, **pipeline (ETL)** 8,
    etc.
10. Redo the dashboard according to the new *voter-target* and 
    *organization-performance* models. Create a system where the 
    dashboard and metrics are updated continuously as the canvases come
    in. Etc.
11. Analyze targets and performance and plan upcoming activities: 
    simple canvas, sway canvas / VIP visit, phone blitz, house meeting 
    (get volunteers), ad buy. Etc.
12. GOTV (constant updates and new lists)...

**Extras**:

1.  Scrape data from the OH Secretary of State's website, given a starter
    Scrapy crawler (based on the working version here).
2.  Do all of the above, but for all of OH with the scraped lists.

- …

**Ohio District Maps**

<!-- (m-fers) -->

http://www.cleveland.com/datacentral/index.ssf/2011/09/ohios_new_congressional_distri.html

Also:

http://www.cleveland.com/datacentral/index.ssf/2010/11/ohio_gop_made_2002_congression.html
