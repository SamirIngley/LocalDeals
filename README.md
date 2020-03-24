LocalDeals: The best price at the nearest location! 

Looks up a user inputted product on the websites of businesses within a specified radius around your coordinates.
Aggregates the prices and displays them in order for you. 
:) happy shopping

Smaller businesses with well-maintained websites get more visibility. 


NOTE: some websites recognize a bot is using their site and will deny access.
I am trying a work around using random mouse clicks and slower speed of typing. 

Flaws:
0. selenium is used to test websites, when testing a website you generally have all the information about where you're supposed to go, and how things are labeled. Websites do not use standard labelling for their browser html. I'm, however, not testing websites, I'm searching them blindly - this makes it a little more difficult to manipulate and more error prone, I therefore have to try lots of different methods until one fits. If you know of any better methods let me know!
1. Not technically, necessarily, the cheapest because it only checks the first few results on the website and does not sort the results on each website. 
2. only businesses with websites get searched
3. only if my code is able to find and access the search box of the website, granted I'm not denied access for being a bot. 


Functionality Progress:
- [x] Get user's coordinates and product, used ajax to send them from JS -> Python
- [x] Validate Google API, Keys hidden
- [x] Pass parameters to Google API, and return business details
- [x] Return list of websites from all locations
- [x] Access websites and search product, used Selenium
- [ ] Parse info on website for product prices, I have the html as a string but Regex not working yet :(
- [ ] Collect prices and sort in ascending order
- [ ] Return list to user
