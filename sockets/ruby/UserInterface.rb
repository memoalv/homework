class UserInterface
  def initialize
    @options = [
      "Genre",
      "Lead studio",
      "Audience score %",
      "Profitability",
      "Rotten tomatoes %",
      "Worldwide gross",
      "Year",
    ]
    @movie  = ""
    @option = 0
  end

  def mainMenu
    invalidOption  = true
    selectedOption = nil

    while invalidOption
      puts "\t*** Sockets in ruby ***\n"
      puts "Please select an option."
      puts "[1] Make a query about a movie"
      puts "[2] exit"
      puts "Option: "
      selectedOption = gets

      selectedOption = selectedOption.to_i

      if selectedOption < 1 or selectedOption > 2
        puts "Invalid option selected."
        sleep 2
        next
      end
      invalidOption = false
    end

    selectedOption
  end

  def getMoviesName
    puts "Please specify the movie you want to make a query about: "
    @movie = gets
    @movie
  end

  def getMovieOption
    invalidOption = true
    selectedOption = nil

    while invalidOption
    
      puts "Please specify the attribute of the movie you need."
      i = 1
      @options.each do |option| 
        puts "[#{i}] #{option}"
        i += 1
     end
      puts "Option: "
      selectedOption = gets

      selectedOption = selectedOption.to_i

      if selectedOption < 1 or selectedOption > 7
        puts "Invalid option selected."
        sleep 2
        next
      end
      invalidOption = false
    end
    @option = selectedOption - 1
    selectedOption
  end

  def displayResponse(res)
    splitRes = res.split("|")

    success = splitRes.first.to_i == 0 ? false : true

    if success
      puts "The #{@options[@option]} for the movie #{@movie.chomp} is: #{splitRes.last}\n\n"
    else
      puts "The #{@options[@option]} for the movie #{@movie.chomp} was not found.\n\n"
    end

  end
end
