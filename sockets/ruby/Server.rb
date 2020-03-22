require "socket"
require_relative "Model"

class Server
  @@model = Model.new

  def initialize(port)
    @server = TCPServer.new port
  end

  def start
    loop do
      client = @server.accept
      query = client.gets
      res = @@model.queryMovie(query)
      client.puts res
      client.close
    end
  end
end

s = Server.new 8080
s.start
