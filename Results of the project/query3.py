import csv
import pickle


def load_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to compute the most common production companies for each genre
def compute_common_companies_per_genre(movies, genres, production_companies):

    genre_company_data = {}

    # Create a mapping of movie IDs to their associated production companies
    movie_companies = {}
    for company_entry in production_companies:
        movie_id = company_entry['id']
        company = company_entry['production_companies']

        if movie_id not in movie_companies:
            movie_companies[movie_id] = []
        movie_companies[movie_id].append(company)

    # Iterate through each genre in the genres table
    for genre_entry in genres:
        genre = genre_entry['genres']
        movie_id = genre_entry['id']

        # Get the companies associated with the movie
        if movie_id in movie_companies:
            companies = movie_companies[movie_id]
        else:
            companies = []

        # Initialize the genre's data if not present
        if genre not in genre_company_data:
            genre_company_data[genre] = {}

        # Count occurrences of each production company
        for company in companies:
            if company not in genre_company_data[genre]:
                genre_company_data[genre][company] = 0
            genre_company_data[genre][company] += 1

    # Organize the results into sorted lists of tuples
    common_companies_per_genre = {}
    for genre, company_data in genre_company_data.items():
        sorted_companies = sorted(company_data.items(), key=lambda x: x[1], reverse=True)
        common_companies_per_genre[genre] = sorted_companies

    return common_companies_per_genre


if __name__ == "__main__":
    # Load the CSV files
    movies = load_csv("movies_table.csv")
    genres = load_csv("genres_table.csv")
    production_companies = load_csv("production_companies_table.csv")

    # Compute the most common production companies for each genre
    common_companies = compute_common_companies_per_genre(movies, genres, production_companies)

    # Save the result to a pickle file
    with open("query3.pkl", "wb") as file:
        pickle.dump(common_companies, file)
