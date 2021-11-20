# Surfs Up “Surf and Shake Shop ” Weather analysis
## Analysis Overview
While on vacation last year in Hawaii I discovered a new found passion for surfing. The trip was such a positive experience that I want to move to Hawaii permanently. I have the idea that could merge my passion for surfing with my passion for ice cream and open a surf and shake shop that would allow me to live out the rest of my days following my passions. I have savings to invest in the shop but I will need a strong investor to  back me to get the shop off the ground. I have created a strong business plan and pitched my idea to an investor who shares my passion for surfing, his name is W. Avy. W. Avy thinks my business plan is sound but is concerned about the weather. He asked that I do some follow up analysis on the weather for the island of Oahu where I intend to open my shop. He provided me a data set to do my analysis and specifically concerned with the months of June and December. 
## Resources
-	Data Source: Hawaii.sqlite
-	Software: SQLite, Python, Flask, Jupyter Notebook

## Results

### June Temperature Analysis 

The first step in our analysis was to review the temperatures for the month of June and generate general statistics for the temperatures during that month. 
The below table shows the statistics for June temperatures:

!Insert June Temp Table

### December Temperature Analysis  
The second step in our analysis was to review the temperatures for month of December and again generate general statistics for the temperatures during that month. 
The below table shows the statistics for December temperature: 

!Insert December Temp Table

### June Precipitation Analysis 

To get a better picture of the overall weather we also did some analysis on the precipitation for the month of June. We mirrored the statics format that we completed for the temperature analysis 
This table shows the precipitation statistics for June: 
!Insert June Precip 

### December Precipitation Analysis 

Again, we mirrored the June precipitation analysis for the month of December. 
This table shows the precipitation statistics for the month of December. 

!Instert Dec Precp 

### Weather Differences Between June and December 

After we completed the temperature and precipitation analysis for the months of June and December we noticed a few key differences. We created comparison tables so that we can easily review and compare the statistics for each month. 
The table below shows the temperature statistics for both June and December:
 
!Insert Temp Comp Table

When reviewing the above table, there are some key differences in the data.
-	The average recorded temperature is slightly higher in the month of June at approximately  75 degrees in contrast the average recorded temperature in December is 71 degrees. 
-	Based on our statistical results June seams to have a more normal distribution of temperatures with a smaller std measure than December.
o	Overall it is clear to see that June has much more consistent temperatures and that there is more variability in the temperatures in the month of December. 
-	When reviewing the min, max it is clear that the temperature range in the month of December is greater. 
## Summary 

After reviewing the data in our analysis and highlighting the differences between June and December I would still feel that December is a good month for both surfing and shake sales. The average temperatures vary only by about 4 degrees which are still near ideal for recreation. Contrasting these two months may also highlight that throughout the year the temps and precipitation are very consistent. 
While temperature is a very important factor to consider in this analysis, so is the amount of precipitation for each month. We created two additional queries to review the precipitation in each month as described in our results and we also created a similar table to contrast the precipitation for the months of June and December. 
The below table contrasts the precipitation statistics for each month: 

!Insert the Precip comp table

When we review the above table there are a few key elements that we want to highlight. 
-	Overall, it appears that there is a higher average rainfall in the month of December. This could be due to the fact there is a high variance in the std. measure and a recorded max of 6.42, the statistics also show that when it does rain in December the  amount is greater than in the month of June. 
