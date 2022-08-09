# surfs_up

## Overview
With the hopes of opening up a combination surf and ice cream shop in Hawaii, we search for investors. Our primary contact goes by the name W. Avy, and he would like to see an analysis of some local weather data in order to be sure that this is a good investment.

## Results
To determine weather or not this shop would be a good investment, we should see whether the weather would be favorable year round. We took a look at 1,700 temperature readings for the month of June from weather stations across the island over a period of seven years. We also looked at 1,517 temperature readings for the month of December over the same time period.

- The mean temperature for June was ~75°, while the mean temperature for December was only ~71°. While there is a difference, I believe most people would enjoy either of these temperatures.
- The maximum tempuratures observered were 85° for June and 83° for December. It is my opinion that most people would be happy with either of these temperatures as well, especially with some ice cream from our new shop.
- The key difference here is in the minimum temperatures, 64° for June and 56° in December. I know for me personally, 56° would be too cold.

Below is a table of our findings for the month of June, followed by the same table but for December.


June:

![june_tobs_stats](https://user-images.githubusercontent.com/35434608/183603722-ca517915-2742-440c-9de7-4cdfcf80081f.png)


December:

![dec_tobs_stats](https://user-images.githubusercontent.com/35434608/183603782-874a18ea-ec69-4454-8722-eecb1feb88a6.png)


## Summary
While the minimum temperature of 56° in December might indicate a chance of there being a "slow season," we must keep in mind that the mean temperature is still about 71°. As far as temperature is concerned, this location seems to be ideal year round. 

For the sake of being thorough, we could create the same two tables for June and December showcasing the precipitation statistics.

Example of query for June:
```
# rain june
rain_results_june = []
rain_results_june = session.query(Measurement.date, Measurement.prcp).\
        filter(extract('month', Measurement.date) == 6).all()
...
```
and the resulting table:

![june_prcp](https://user-images.githubusercontent.com/35434608/183647188-a9d0dacb-9e08-4a5a-ab26-b8ce3762475c.png)
