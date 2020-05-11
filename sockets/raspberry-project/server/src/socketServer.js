"use-strict"
const net = require("net")
const mongoModel = require("./mongoModel")

class socketServer {
  constructor() {
    this.server = net.createServer((connection) => {
      console.log("[Connection accepted]")

      connection.on("end", () => {
        console.log("[Connection closed]")
      })

      connection.on("data", async (data) => {
        const mongo = new mongoModel()
        const receivedData = JSON.parse(data.toString())

        if (receivedData.type == "tempLog") {
          const response = {}
          try {
            await mongo.saveData(receivedData)

            response.status  = 1
            response.message = "Success"
            connection.write(JSON.stringify(response))
          } catch (e) {
            response.status  = 0
            response.message = "An error ocurred while trying to save the data"
            connection.write(JSON.stringify(response))
          } finally {
            // close client's connection
            connection.pipe(connection)
          }
        }
      })
    })
  }

  listen(port) {
    this.server.listen(port, () => {
      console.log(`Server listening on port ${port}`)
    })
  }
}

module.exports = socketServer
