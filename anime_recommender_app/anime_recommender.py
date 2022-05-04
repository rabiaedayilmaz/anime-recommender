import pandas as pd
import random

class AnimeRecommender:
    def __init__(self, data_path, anime_search):
        self.app_data = pd.read_csv(data_path, index_col=0)
        self.in_db = True
        # print(self.app_data.head())

        # anime to query
        self.anime_search = anime_search

        self.w, self.h = self.app_data.shape[0], self.app_data.shape[1]
        self.anime_names = self.app_data["AnimeName"]
        self.cluster_type = self.app_data["ClusterType"]

    def search_cluster(self):
        if self.anime_search != "":
            anime = self.app_data[self.anime_names.apply(lambda x: x.lower()) == self.anime_search.lower()]
            name, cluster = anime["AnimeName"], anime["ClusterType"]
            #print(name, "\n", cluster)
            # because cluster is series object, make it integer
            try:
                to_recommend = self.app_data[self.cluster_type == int(cluster)]
            except:
                self.in_db = False
                to_recommend = "This anime is not in database :("
            return to_recommend

    def recommend(self, animelist):
        if self.in_db:
            random_int = random.randint(0, animelist.shape[0])
            recommendation = animelist.iloc[random_int]
        else:
            recommendation = "This anime is not in database :("

        return recommendation, self.in_db
