![](https://github.com/cuteopamp/anime-recommender/blob/main/readme_files/tantan.jpg?raw=true)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

The main goal of this app is to recommend animes to users.

![Anime Recommender on Action](https://github.com/cuteopamp/anime-recommender/blob/main/readme_files/AnimeRecommenderLive.gif?raw=true)
|:--:|
| *Anime Recommender on Action* |

![Menu Screen](https://github.com/cuteopamp/anime-recommender/blob/main/readme_files/menu_ss.png?raw=true)
|:--:|
| *Menu Screen* |

![Option Screen](https://github.com/cuteopamp/anime-recommender/blob/main/readme_files/option_ss.png?raw=true)
|:--:|
| *Option Screen* |

![Result Screen](https://github.com/cuteopamp/anime-recommender/blob/main/readme_files/resuls_ss.png?raw=true)
|:--:|
| *Result Screen* |


## Getting Started

List of some packages that are necessary: pygame for game app, numpy and pandas for data processing, sklearn for machine learning techniques and random, itertools as auxiliary.

### Prerequisites

 * pygame
  ```
  pip install pygame
  ```
 * numpy
  ```
  pip install numpy
  ```
 * pandas
  ```
  pip install pandas
  ```
 * sklearn
  ```
  pip install sklearn
  ```
 * random
  ```
  pip install random
  ```
 * itertools
  ```
  pip install itertools
  ```
### Usage
* You can download directly [anime_recommender_app folder](https://github.com/cuteopamp/anime-recommender/tree/main/anime_recommender_app) and run main.py file. Even edit it. Maybe, like me, you can get your next anime to watch :)
* Or you can just [download the game](https://cuteopamp.itch.io/anime-recommender) and run main.exe without any setup.

## Roadmap
In order to recommend anime, firstly, one should analyze and process the data by using some machine learning techniques.

But, you need data to process. I used the dataset: [Anime Recommendations Database from Kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database) which is gathered by using myanimelist.net API. It is updated 5 years ago. My dumbness. Because of that, most recent animes aren't in the dataset, like my favourite anime: Demon Slayer. (But there are a lot of hentai lol)

Therefore, currently three approaches are followed: 
* [recommendation by the rate of common tags](https://github.com/cuteopamp/anime-recommender/blob/main/recommender/anime_recommender_by_tags.ipynb)
    * user enters tags that s/he is interested in
    * then it recommends animes by common tags 
* [recommendation by clustering using KMeans and PCA](https://github.com/cuteopamp/anime-recommender/blob/main/recommender/pca_anime_clustering.ipynb)
    * there are clusters formed by user data
    * cluster is recommended which is relevant her/his taste
* [recommendation by clustering using KMeans and t-SNE](https://github.com/cuteopamp/anime-recommender/blob/main/recommender/tsne_anime_recommender.ipynb)
    * there are clusters formed by user data
    * cluster is recommended which is relevant her/his taste

**I chose the result of t-SNE dimensionality reduction and K-Means techniques for my app data.**

* Then, a game is created by using pygame to interact with user easily and aesthetically.

## Acknowledgments
[Anime Recommendations Database from Kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

<!-- CONTACT -->
## Contact

For any further ideas, suggestion, critics or just comments, please reach me out! I'd like to be happy to hear them.

R.E.Y. - [@cuteopamp](https://twitter.com/cuteopamp) - edayilmxz@outlook.com

Project Link: [https://github.com/cuteopamp/anime-recommender](https://github.com/cuteopamp/anime-recommender)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
P.S. to me, next time ask yourself whether you are on nuts or not, if you want to process anime data. There are so many hearts, stars and notes etc. in the name of animes. If there are multiple heart, it is probably hentai btw. Using movies dataset might be enjoyable. And check the date of dataset next time. 
