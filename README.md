# ACC Women's Basketball Player Heights

[__December 2019 Galvanize Data Science Immersive__](https://www.galvanize.com/austin)

__Question__ - Has average player height changed from the sample years of 2009-2010/2010-2011/2011-2012 to 2017-2018/2018-2019/2019-2020 among women’s basketball teams in the Atlantic Coastal Conference (ACC)?

__Project Setup:__
-Initial thought was to grab data from all ACC teams in 2010 & compare to all teams in 2020.  By comparing all teams I would have the entire population, which would not offer the chance to utilize statistical sampling concepts (bootstrapping & central limit theorem).  Chose to group by several years instead to allow for sampling.  Also would center web scraping on 4 sources (team websites) rather than 10+.

-I wanted to pick teams that tend to consistently select the same caliber prospects annually, so I went with a Power 5 conference in the ACC.  The thought is if I chose a conference that typically has lower tier recruits (which trends toward shorter players), then conference realignment could bring in teams that were dramatically better than the typical team and cause a size increase when it was just a result of an elite school like UConn joining the conference and increasing the height average.  

-My teams will be North Carolina, Miami, NC State, & Duke

-I settled onto these teams because their team websites have rosters for the desired time frames.  Some teams did not have data available for certain years (Florida State, Virginia).

__Hypothesis:__
Null - The average height of players from 2017-2020 is equal to the average height of players from 2009-2012.

Alternate - The average height of players from 2017-2020 is not equal to the average height of players from 2009-2012.

__Analysis methods:__
The tech stack consists of Python 3, Numpy, Pandas, Beautiful Soup, Scikit-Learn, Matplotlib, HTML, and CSS.

One JSON file, the results of the webscraping, are stored in the data directory.

ted-main.csv has the metadata for 2638 TED Talks- all talks featured on TED.com from 2006 through 2017. transcripts.csv contains the transcripts for 2542 talks - the transcripts are not available for every talk.

Four text transcript files are also stored in the data directory. These transcripts cannot be stored in a CSV because they are larger than the 32,767 character limit for a cell.

To prepare the dataset for analyses:

From the src directory of the repo, run the following code:

python assemble.py

python annotate.py

python process-text.py

These scripts:

join large transcripts to dataframe for analysis
drop rows with missing transcripts
remove talks centered around music performances
remove talks with more than 1 speaker
create features like 'applause', 'laughter' from transcript
normalize ratings counts to account for number of times the talk has been viewed
divide transcripts into halves and quarters
add results of LIWC analysis and create emotion word change features
Edits to transcripts were done by script and by hand to remove question and answer sections and conversations with multiple speakers.

If structural changes to the cleaning and feature engineering are required, rerun the results of annotate.py, the dataset in all_after_annotate.xls, through LIWC module to produce per document word category ratios. A license with LIWC is required and is available at liwc.net.

After running the 3 scripts above, you have a final dataset all_with_liwc_segmented.xls with features ready for statistical models (93.5 MB).

For all the following analyses, the response variable is set in the settings.py file, on line 3, under the variable name "TARGET".

For response variables, you might choose from 'norm_persuasive', 'norm_inspiring', 'views', 'comments', or 'applause'.

To fit a decision tree, and see the top feature importances, run:

python predict-decision-tree.py

To fit a random forest regressor and see the top feature importances, run:

python predict-random-forest.py

To build a linear regression model with most important features from the previous steps as predictors, run:

python predict-linear.py

To explore the 10 primary components in TED Talks using non-negative matrix factorization to perform clustering, run:

python clustering.py

To train a classifier model to predict 'persuasive' and 'non-persuasive' texts, run:

python classification.py

You can also access this classifier tool by visiting theodorespeaks.com, scrolling down, and inputting your own text into the text box and hitting "Submit". The page will reload with a "Persuasive" or "Non-Persuasive" prediction with a probability beside the text box.

To find a similar TED speaker based on Euclidean distance and linguistic feature similarity to a speaker you specify, change the SPEAKER_FULL_NAME variable in line 11 and run:

python distance.py

You can also access this "Find a Similar Speaker" tool by visiting theodorespeaks.com, scrolling down, and inputting a speaker's full name into the text box and hitting "Submit".

__Future questions:__
Have other measurables (wingspan, vertical jump, etc.) changed?

What about comparing actual game statistics?

-Have 3pt attempts increased?  Foul rate?  Post touches?  FT rate? Etc.

Is there a difference in height for individual position groups (PG, Wing, Bigs)?




