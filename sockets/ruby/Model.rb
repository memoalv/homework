require "csv"

class Model
  @@movies = []

  def initialize()
    loadMovies()
  end

  def loadMovies()
    moviesCSV = CSV.read("movies.csv")

    loopIndex = 0
    @@movies = []
    for row in moviesCSV
      loopIndex += 1
      if loopIndex == 1
        next # skip to the next iteration
      end
      # push every movie into array
      @@movies << row
    end
  end

  def queryMovie(payload)
    splitPayload = payload.split("|")

    if splitPayload.length < 1 and splitPayload.length > 2
      return "0|"
    end

    # first, last == splitPayload[0], splitPayload[-1]
    opCode = splitPayload.first.to_i
    moviesName = splitPayload.last.to_s

    if opCode < 1
      return "0|"
    end
    movie = getMoviesData(moviesName)
    if movie
      return "1|#{movie[opCode]}"
    end
    "0|" # ruby always returns the last evaluated expression
  end

  def getMoviesData(moviesName)
     @@movies.each do |movie|
      m1 = movie[0].upcase
      m2 = moviesName.upcase
      if m2.include? m1
        return movie
      end
    end
    false
  end

  # declare private methods, public methods need to be called with the 'self' prefix
  private :loadMovies, :getMoviesData
end

# m = Model.new
# m.queryMovie("1|wall-e")