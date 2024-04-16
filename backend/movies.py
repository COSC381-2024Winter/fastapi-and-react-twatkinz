class Movies:
    def __init__(self, movies_file):
        self._movies = []
        self._idcounter = 0

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx % 3 == 0:
                    movie_name = line.rstrip()
                elif row_idx % 3 == 1:
                    movie_cast = line.rstrip().split(',')
                elif row_idx % 3 == 2:
                    self._idcounter += 1
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast,
                            'id': self._idcounter
                        }
                    )
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie to the list
            self._idcounter += 1
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast,
                    'id': self._idcounter
                }
            )


    def add_movie(self, title, cast):
        self._idcounter += 1
        new_movie = {
            'name': title,
            'cast': cast,
            'id': self._idcounter
        }
        self._movies.append(new_movie)
        return new_movie



if __name__ == "__main__":
    movies = Movies('./movies.txt')
    movies.add_movie("New Movie", ["Actor1", "Actor2"])
