# ACC Women's Basketball Player Heights

__Question__ - Has average player height changed from the sample years of 2009-2010/2010-2011/2011-2012 to 2017-2018/2018-2019/2019-2020 among women’s basketball teams in the Atlantic Coastal Conference (ACC)?

__Project Setup:__
-Initial thought was to grab data from all ACC teams in 2010 & compare to all teams in 2020.  By comparing all teams I would have the entire population, which would not offer the chance to utilize statistical sampling concepts (bootstrapping & central limit theorem).  Chose to group by several years instead to allow for sampling.  Also would center web scraping on 4 sources (team websites) rather than 10+.

-I wanted to pick teams that tend to consistently select the same caliber prospects annually, so I went with a Power 5 conference in the ACC.  The thought is if I chose a conference that typically has lower tier recruits (which trends toward shorter players), then conference realignment could bring in teams that were dramatically better than the typical team and cause a size increase when it was just a result of an elite school like UConn joining the conference and increasing the height average.  

-My teams will be North Carolina, Miami, NC State, & Duke

-I settled onto these teams because their team websites have rosters for the desired time frames.  Some teams did not have data available for certain years (Florida State, Virginia).

__Null Hypothesis:__
-The average height of players from 2017-2020 is equal to the average height of players from 2009-2012.

__Alternate Hypothesis:__ 
-The average height of players from 2017-2020 is not equal to the average height of players from 2009-2012.

__Analysis Methods:__
The tech stack consists of Python 3, Numpy, Pandas, Beautiful Soup, Scikit-Learn, Matplotlib, HTML, and CSS.

One JSON file, the results of the webscraping, are stored in the data directory.

To prepare the dataset for analyses:

From the src directory of the repo, run the following code:

webscrape.py

parsing.py

__Results:__
There was not enough evidence to reject the null hypothesis that the average height of players from 2017-2020 is equal to the average height of players from 2009-2012.

__Future questions:__
Have other measurables (wingspan, vertical jump, etc.) changed?

What about comparing actual game statistics?

-Have 3pt attempts increased?  Foul rate?  Post touches?  FT rate? Etc.

Is there a difference in height for individual position groups (PG, Wing, Bigs)?




