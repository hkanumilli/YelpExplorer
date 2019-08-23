# Yelp Explorer

Interactive query tool for Yelp data. Built using Bokeh and the Yelp Fusion API. 

A credibility metric was introduced that combines a business's rating and review count ensuring that a 5-star establishment with 1000 reviews gets more weight than a 5-star establishment with 20 reviews. 

To run:
1. Clone and download repository.
2. Update `query.py` to include your API KEY.
3. Start Bokeh server: `bokeh serve --show main.py`

The application should open in your browser as `http://localhost:5006/main`.

Below is an example of what running the program looks like. 

![Image description](https://github.com/hkanumilli/YelpExplorer/blob/master/testExample.png)
