class Movies:
    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            idcounter = 0
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                    idcounter += 1
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast,
                            'id': idcounter
                        }
                    )
                    movie_name = None
                    movie_cast = None
                    movie_id = None
                row_idx += 1
                

        if movie_name and movie_cast:
            # Add the last movie to the list
            idcounter += 1
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast,
                    'id': idcounter
                }
            )

if __name__ == "__main__":
    movies = Movies('./movies.txt')