**On hold as I didnn't expect the lineup to come out 6 weeks earlier than previous lineup revials**
# Lineup_Predictor_Model.py
basic script updated to this past lineup (2019). 
-Developed a Python Script using Pandas to count the number of appearances of artists performing at Electric Daisy Carnival (Las Vegas) from 2015 through 2019. From there I took the results and imported the results into Tableau to create visualizations.

- Currently working on condition statements to increase accuracy and performance.
Used https://www.reddit.com/r/electricdaisycarnival/comments/amlt6o/last_four_lineups_from_edc_ordered_by_of/ Pandas script as a baseline before adding in updated timeline and criteria.
Adding in statements tracking artists who have played at events run by Insomniac Events (Electric Forest, Countdown NYE, Beyond Wonderland, ETC.) to find patterns in artists who reoccure throughout the year, leading up to EDC Las Vegas.
Also looking to find trends of artists who gain bigger slots/headlining times throughout the year among different festivals and events. 


Updates: 
- Currently working on IF statements and loops for the following criteria:

- Radius Clause: A form of non-compete clause used in the live music industry, in which a tour promoter stipulates that a performer, for a certain length of time prior to or following an appearance at a concert or festival, must not hold concerts at other locations within a certain radius of the city where they are to perform. In essence, it gives the promoter a form of territorial exclusivity, ensuring that the performer does not book concerts with competing promoters and venues in nearby areas, which can undermine ticket sales for their main event. (Wikipedia)
- If an artist has played at an insomniac curated show since January 1st (Does not include festivals). 
- Social Media Presence: Example --> Artist_A posts a song on SoundCloud. Insomniac Events --> Shares/Reposts the song. 
Higher reasoning to add Social Media presence: Anytime Insomniac Events, EDC Las Vegas, Pasquale Rotella, Insomniac Sub-brands: BassRush, BassCon Factory 93, Dreamstate or HARD events share/like or interact with artists. 
- Easy one: Leaks of information or artists simply stating they are attending. 


- Another important criteria that causes some challenges are "B2B" and Alias sets:
- When two artists play in the same set = B2B. 
- Aliases of artists, for example: Svdden death playing a set, but having a VOYD set or Zhu playing a set and having a BLACKLIZT set. 
- Also Tchami X Malaa No Redemption... falls into B2B Criteria. 

These kinds of sets can some times avoid radius clause. 
