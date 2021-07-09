<template>
  <div
    class="home"
  >
    <h1>All-in-One Travel Planner</h1>
    <p>Welcome to your all-in-one travel planner,
      where you can check the latest updates on travel restrictions,
      search for flights,
      sign up for alerts which might affect your travel plans,
      and more!</p>

    <FlightSearch :countries=this.countries />

    <TravelAllowances :countries=this.countries />
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import FlightSearch from '@/components/FlightSearch'
import TravelAllowances from '@/components/TravelAllowances'

const backendPath = process.env.VUE_APP_ROOT_API

export default {
  name: 'Home',
  data () {
    return {
      countries: []
    }
  },
  components: { FlightSearch, TravelAllowances },
  methods: {
    getCountries () {
      const path = `${backendPath}/countries`
      axios.get(path)
        .then((res) => {
          this.countries = res.data.countries
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    }
  },
  created () {
    this.getCountries()
  }
}
</script>
