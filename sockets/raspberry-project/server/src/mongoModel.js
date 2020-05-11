"use-strict"

const mongodb = require("mongodb")
const assert = require("assert")
const { v4: uuidv4 } = require("uuid")

class mongoModel {
  constructor() {
    this.url = "mongodb://127.0.0.1:27017"
    this.dbName = "sensorLog"
    this.client = mongodb.MongoClient(this.url, { useUnifiedTopology: true })
  }

  saveData({ temp, hum }) {
    return new Promise((resolve, reject) => {
      this.client.connect((err, client) => {
        assert.equal(null, err)

        const db = this.client.db(this.dbName)
        const newDocument = {
          uuid: uuidv4(),
          timestamp: new Date(),
          temperature: this.parseValue(temp),
          humidity: this.parseValue(hum),
        }

        db.collection("climate").insertOne(newDocument, (err, res) => {
          try {
            assert.equal(null, err)
            assert.equal(1, res.insertedCount)
            resolve(true)
          } catch (error) {
            reject(false)
          }
          finally {
            client.close()
          }
        })
      })
    })
  }

  parseValue(val) {
    return parseFloat(val)
  }
}

module.exports = mongoModel
