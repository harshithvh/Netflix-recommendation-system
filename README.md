# Netflix-recommendation-system
NLP, Machine learning

<img align="left" alt="Visual Studio Code" width="1080px" src="https://i0.wp.com/thecleverprogrammer.com/wp-content/uploads/2020/12/Machine-Learning-Project-on-Netflix-Recommendation-System.png?fit=1280%2C720&ssl=1" />

# About

---

Recommendation algorithms are at the core of the Netflix product. It provides their members with personalized suggestions to reduce the amount of time and frustration to find something great content to watch. Because of the importance of our recommendations, they continually seek to improve them by advancing the state-of-the-art in the field. They do this by using the data about what content our members watch and enjoy along with how they interact with our service to get better at figuring out what the next great movie or TV show for them will be.

# Types

---

The categories under "Trending Now" and "New Releases" are Non-Personalized Recommendation System
<br />
The categories under "Because you watched" are Personalized Recommendation System

<img align="left" alt="Visual Studio Code" width="1080px" src="https://cdn-images-1.medium.com/max/1600/0*baj8e-s1v5hJRm6A." />

# NLP

---

Natural language processing is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data.

<img align="left" alt="Visual Studio Code" width="1080px" src="https://cdn.searchenginejournal.com/wp-content/uploads/2020/08/an-introduction-to-natural-language-processing-with-python-for-seos-5f3519eeb8368.png" />

# #1 Tokenization

---

Tokenization is the process of breaking down sentence or paragraphs into smaller chunks of words called tokens.

# #2 Stop Words Removal

---

On removal of some words, the meaning of the sentence doesn't change, like and, am. Those words are called stop-words and should be removed before feeding to any algorithm. In datasets, some non-stop words repeat very frequently. Those words too should be removed to get an unbiased result from the algorithm.

# #3 Vectorization

---

After tokenization, and stop words removal, our "content" are still in string format. We need to convert those strings to numbers based on their importance (features). We use TF-IDF vectorization to convert those text to vector of importance. With TF-IDF we can extract important words in our data. It assign rarely occurring words a high number, and frequently occurring words a very low number.

## Sources 
* https://www.netflixprize.com/rules.html
* https://www.kaggle.com/netflix-inc/netflix-prize-data
* Netflix blog: https://medium.com/netflix-techblog/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429 (very nice blog)
* Research paper: http://courses.ischool.berkeley.edu/i290-dm/s11/SECURE/a1-koren.pdf 

## Type of Data:
* There are 17770 unique movie IDs.
* There are 480189 unique user IDs.
* There are ratings. Ratings are on a five star (integral) scale from 1 to 5.
* There is a date on which the movie is watched by the user in the format YYYY-MM-DD.

## Built With
*	ipython-notebook - Python Text Editor
*	sklearn - Machine learning library
*	seaborn, matplotlib.pyplot, - Visualization libraries
*	numpy, scipy- number python library
*	pandas - data handling library
