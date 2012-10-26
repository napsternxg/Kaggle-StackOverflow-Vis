Kaggle Stack Overflow Visualization Competition Entry
======================================================

The idea of this data research is to find trends among all the sites present on Stack Exchange Network. 

I have tried to take into account the various SE sites which are present and how much content is getting generated and how are the users using that content. A major focus of my study is how the stack network has grown since its inception and which sites have significantly contributed towards the growth of the SE Network.

I have tried to visualize the date in terms of motion charts to see how the activity has changed on the SE network for each of the websites.

In particular I have made a comparitive study of top sites among the 2 kinds of sites on SE network viz. computer science related and non-computer science related.

The interesting realizations have been that the non-cs sites also generate an equal amount of traffic however there are many fluctuations in the same for non cs as compared to the usual cs sites on SE.

Following are some images of the growth of the CS and non CS sites on SE network. [I have only considered the top sites in each category]:

Here are the data for the top Non CS sites on SE Network:

!["Non CS Stack Exchange Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/NonCS_SEMonthGrowth.PNG "Non CS Stack Exchange Montly Growth")

!["Non CS Stack Exchange Average Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/NonCS_SEMonthGrowthAvgScore.PNG "Non CS Stack Exchange Average Score Montly Growth")

!["Non CS Stack Exchange Questions and Answer Posts Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/NonCS_SEMonthGrowthQnA.PNG "Non CS Stack Exchange Questions and Answer Posts Montly Growth")

!["Non CS Stack Exchange Total Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/NonCS_SEMonthGrowthSumScore.PNG "Non CS Stack Exchange Total Score Montly Growth")

Also below are similar data for some of the top CS sites on SE Network:

!["CS Stack Exchange Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/SENetworkCountScoreGrowth.PNG "CS Stack Exchange Montly Growth")

!["CS Stack Exchange Average Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/SENetworkAverageScoreGrowth.PNG "CS Stack Exchange Average Score Montly Growth")

!["CS Stack Exchange Questions and Answer Posts Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/SENetworkQnAGrowth.PNG "CS Stack Exchange Questions and Answer Posts Montly Growth")

!["CS Stack Exchange Total Score Montly Growth"](https://github.com/napsternxg/Kaggle-StackOverflow-Vis/blob/master/Images/SENetworkSumScoreGrowth.PNG "CS Stack Exchange Total Score Montly Growth")






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

