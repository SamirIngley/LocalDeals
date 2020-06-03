LocalDeals: The best price at the nearest location! 

Note: progress is on halt due to the fact that every website has a whole new set of html to parse and creating explicit code for each possibility is inefficient. Creating a ML algorithm to learn where the search box is on any given website would be ideal... so the project is on hold for now. 

Looks up a user inputted product on the websites of businesses within a specified radius around your coordinates.
Aggregates the prices and displays them in order for you. 
:) happy shopping

* Smaller businesses with well-maintained websites get more visibility. 

NOTE: some websites recognize a bot is using their site and will deny access.
I am trying a work around using random mouse clicks and slower speed of typing. 
*******************
Install
1. Clone or Download the repository
2. Install the requirements.txt
3. Remember to click 'yes' when your browser asks to use your location
4. If you're using windows - make sure in scraper.py the browser variable can grab your username path
5. Have your Google API key stored as an enviroment variable labeled GOOGLE_API_KEY=[your key]
6. 

******************

Flaws:
0. selenium is used to test websites, when testing a website you generally have all the information about where you're supposed to go, and how things are labeled. Websites do not use standard labelling for their browser html. I'm, however, not testing websites, I'm searching them blindly - this makes it a little more difficult to manipulate and more error prone, I therefore have to try lots of different methods until one fits. If you know of any better methods let me know!
1. Not technically, necessarily, the cheapest because it only checks the first few results on the website and does not sort the results on each website. 
2. only businesses with websites get searched
3. only if my code is able to find and access the search box of the website, granted I'm not denied access for being a bot. 


Functionality Progress:
- [x] Get user's coordinates and product, used Ajax to send them from JS -> Python
- [x] Validate Google API, Keys hidden in environment variables
- [x] Pass parameters to Google API, and return business details
- [x] Compile list of websites from all businesses
- [x] Access websites and search product, used Selenium
- [ ] Parse info on website for product prices, I have the html as a string but Regex not working yet :(
- [ ] Collect prices and sort in ascending order
- [ ] Return list to user
