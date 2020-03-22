require "socket"
require_relative "UserInterface"

class Client
  @@ui = UserInterface.new

  def initialize(port)
    @port = port
  end

  def start
    exitFlag = false

    while !exitFlag
      option = @@ui.mainMenu()

      if option == 1
        socket = TCPSocket.new "localhost", @port

        moviesName = @@ui.getMoviesName()
        movieOption = @@ui.getMovieOption()
        socket.puts "#{movieOption}|#{moviesName}"
        response = socket.gets
        @@ui.displayResponse(response)
        socket.close
        next
      end

      exitFlag = true
    end
  end
end

c = Client.new 8080
c.start
