Kaggle Stack Overflow Visualization Competition Entry
======================================================

The idea of this data research is to find trends among all the sites present on Stack Exchange Network. 

I have tried to take into account the various SE sites which are present and how much content is getting generated and how are the users using that content. A major focus of my study is how the stack network has grown since its inception and which sites have significantly contributed towards the growth of the SE Network.

I have tried to visualize the date in terms of motion charts to see how the activity has changed on the SE network for each of the websites.

Comparison of Computer Related and Non Computer Related Sites
--------------------------------------------------------------

In particular I have made a comparitive study of top sites among the 2 kinds of sites on SE network viz. computer science related and non-computer science related.

The interesting realizations have been that the non-cs sites also generate an equal amount of traffic however there are many fluctuations in the same for non cs as compared to the usual cs sites on SE.

Following are some images of the growth of the CS and non CS sites on SE network. [I have only considered the top sites in each category]:

Here are the data for the top Non CS sites on SE Network:

!["Non CS Stack Exchange Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/NonCS_SEMonthGrowth.PNG "Non CS Stack Exchange Montly Growth")

!["Non CS Stack Exchange Average Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/NonCS_SEMonthGrowthAvgScore.PNG "Non CS Stack Exchange Average Score Montly Growth")

!["Non CS Stack Exchange Questions and Answer Posts Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/NonCS_SEMonthGrowthQnA.PNG "Non CS Stack Exchange Questions and Answer Posts Montly Growth")

!["Non CS Stack Exchange Total Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/NonCS_SEMonthGrowthSumScore.PNG "Non CS Stack Exchange Total Score Montly Growth")

Also below are similar data for some of the top CS sites on SE Network:

!["CS Stack Exchange Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/SENetworkCountScoreGrowth.PNG "CS Stack Exchange Montly Growth")

!["CS Stack Exchange Average Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/SENetworkAverageScoreGrowth.PNG "CS Stack Exchange Average Score Montly Growth")

!["CS Stack Exchange Questions and Answer Posts Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/SENetworkQnAGrowth.PNG "CS Stack Exchange Questions and Answer Posts Montly Growth")

!["CS Stack Exchange Total Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/SENetworkSumScoreGrowth.PNG "CS Stack Exchange Total Score Montly Growth")

Data of Stack Exchange Network
-------------------------------

I have also taken a closer look at the data hosted on the stack exchange network related to the density of interaction on its various sister sites.

Here are some info graphics which clearly point out which are the most used websites on the network and how are the various types of interactions divided:

!["Stack Exchange Site Wide Split"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/StackExchangeSiteWiseSplit.png "Stack Exchange Site Wide Split")

The above info graphic tells us that the amount of interactions are more or less same on all sites. Some sites stand out as clear winners in terms of the ratio of the questions asked to answered.

Below is a more comparitive study in terms of '''Questions, Answers, Comments and Tags''' on each of the sites.

!["Stack Exchange Site Wide Split for Questions"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/QuestionsStackExchange.PNG "Stack Exchange Site Wide Split for Questions")

!["Stack Exchange Site Wide Split for Answers"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/AnswersStackExchange.PNG "Stack Exchange Site Wide Split for Answers")

!["Stack Exchange Site Wide Split for Comments"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/CommentsStackExchange.PNG "Stack Exchange Site Wide Split for Comments")

!["Stack Exchange Site Wide Split for Tags"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/TagsStackExchange.PNG "Stack Exchange Site Wide Split for Tags")

Country Based Split of Users for Stack Overflow
-----------------------------------------------

This is something which I feel is useful and is specific to stack overflow as I have tried to map the various countries based on the density of their user activity. The infographic shows that some countries are still not using stack overflow.

!["Stack Overflow Country Wide Split for Users"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/StackOverFlowCountryData.png "Stack Overflow Country Wide Split for Users")

Top Tags on Stack Overflow
--------------------------

Tags are important way of categorizing information on stack exchange sites so here I have tried to visualize the life cycle of the current top tags on  stack overflow:

!["Life Cycle of Top Tags on Stack Overflow"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/TopTagsCountGrowthMonthWise.PNG "Life Cycle of Top Tags on Stack Overflow")

Also here is the total tag count in the current month. A more interesting infographic can be looked at my full code which shows a motion chart detailing how each tag grew on stack overflow.

!["Life Cycle of Top Tags on Stack Overflow"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/raw/master/Images/TopTagsCountBar.PNG "Life Cycle of Top Tags on Stack Overflow")





Installation
------------

* Simply clone the repo onto your machine preferably inside the webroot of your webserver
* If you have python installed you can simply run `python -m SimpleHTTPServer 8080` into the folder where you have downloaded the files and then you can access them on the internet using `http://localhost:8080/FileName`

Other Exciting thing I stumbled upon while creating these visualizations:
-------------------------------------------------------------------------

* UK Univ Statistics using TreeMaps: http://keminglabs.com/ukuni/
* Chord Network Visualization: http://bost.ocks.org/mike/uberdata/

References:
-----------
* Visulizations using d3.js and Google Visualizations
* All data used can be found at this public google spreadsheep: https://docs.google.com/spreadsheet/pub?key=0AipE5c521mI_dEhMUEVRQlJzM3BOT0h2QVJ0Wm9RbUE&output=html
* For querying the data I have used the StackExchange Data Explorer at: http://data.stackexchange.com
* The d3.js visualizations have been created using example given on the d3js examples page at: https://github.com/mbostock/d3/wiki/Gallery
* Tooltip concept taken from: https://gist.github.com/1016860#gistcomment-61316
* The motion charts require the presence of a flash player
* All d3.js charts and google visualizations require the presence of modern browsers which support SVG and HTML5
* Most google visualizations have been build using the examples given at: http://code.google.com/apis/ajax/playground/?type=visualization#motion_chart
* d3 API reference can be accessed at: https://github.com/mbostock/d3/wiki/API-Reference
* Another interesting tool for querying and studying Stack Exchange Network data is: https://github.com/lucjon/Py-StackExchange/blob/master/demo/object_explorer.py
* The treemap strucuture has been taken from: http://mbostock.github.com/d3/ex/treemap.html
* The donut structure has been taken from: http://bl.ocks.org/3888852
* For map color schemes I have used the colors schemes from: http://colorbrewer2.org/

