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

    <SignedInUser :countries=this.countries />

    <h2 style="display: inline-block;">Travel Allowances</h2>
    <b-button
        href @click.prevent="signUpAlerts"
        variant="outline-danger"
        style="float: right;
              vertical-align:top;">Sign up for alerts to changes</b-button>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Countries</th>
          <th scope="col">Vaccinated</th>
          <th scope="col">Non-Vaccinated</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(country, index) in countries" :key="index">
          <td>{{ country.name }}</td>
          <td>{{ country.vaccinated }}</td>
          <td>{{ country.non_vaccinated }}</td>
        </tr>
      </tbody>
    </table>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import SignedInUser from '@/components/SignedInUser'

const backendPath = process.env.VUE_APP_ROOT_API

export default {
  name: 'Home',
  data () {
    return {
      countries: []
    }
  },
  components: { SignedInUser },
  methods: {
    signUpAlerts () {
      this.$router.push('/travelalerts')
    },
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
