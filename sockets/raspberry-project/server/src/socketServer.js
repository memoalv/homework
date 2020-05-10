"use-strict"
const net = require("net")
const mongoModel = require("./mongoModel")

class socketServer {
  constructor() {
    this.server = net.createServer((connection) => {
      console.log("connection accepted")

      connection.on("end", () => {
        console.log("connection closed")
      })

      connection.on("data", async (data) => {
        const mongo = new mongoModel()
        const receivedData = JSON.parse(data.toString())

        if (receivedData.type == "tempLog") {
          try {
            await mongo.saveData(receivedData)
            connection.write("1")
          } catch (e) {
            connection.write("0")
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
