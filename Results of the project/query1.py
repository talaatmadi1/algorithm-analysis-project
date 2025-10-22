import csv
import pickle

name_rating_dict = dict() 
result_dict = dict() 

with open("movies_table.csv", mode="r") as csvfile: 
    reader = csv.DictReader(csvfile) 
   
    for row in reader: 
        rating = float(row['vote_average']) 
        id = row['id'] 
       
        if id not in name_rating_dict: 
            name_rating_dict[id] = {"genre/s":[], "rating": [rating]} 
        else: 
            name_rating_dict[id]["rating"].append(rating) 

with open("genres_table.csv", mode="r") as csvfile: 
    reader = csv.DictReader(csvfile) 
   
    for row in reader: 
        genre = row['genres'] 
        id = row['id'] 
       
        if id not in name_rating_dict: 
            name_rating_dict[id] = {"genre/s":[genre],"rating": []} 
        else: 
            name_rating_dict[id]["genre/s"].append(genre) 
        
        if genre not in result_dict: 
            result_dict[genre] = {(1, 2):0,(2, 3):0,(3, 4):0,(4, 5):0,(5, 6):0,(6, 7):0,(7, 8):0,(8, 9):0,(9, 10):0} 




for movie_id, details in name_rating_dict.items(): 
    for rating in details['rating']: 
        for genre in details['genre/s']: 
            for (start, end), count in result_dict[genre].items(): 
                if start <= rating < end: 
                    result_dict[genre][(start, end)] += 1 
         
with open("query1.pkl", "wb") as f:
    pickle.dump(result_dict, f)