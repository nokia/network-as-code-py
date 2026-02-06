
import { NetworkAsCodeApiClient } from './dist/esm/Client.js'

const client = new NetworkAsCodeApiClient({
  rapidapiHost: "network-as-code.nokia.rapidapi.com",
  apiKey: process.env.API_KEY
})

console.log(await client.location.retrieve({
  device: {
    phoneNumber: "+99999991000"
  },
  maxAge: 60
}))
