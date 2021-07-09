<template>
  <div>
    <b-button
        href
        @click.prevent="backHome"
        variant="primary">Back to Home</b-button>
    <h1>Travel Alerts</h1>
    <form>
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          placeholder="name@example.com"
          required>
        <small id="emailHelp" class="form-text text-muted">
          We'll never share your email with anyone else.
        </small>
      </div>
      <div class="form-check" v-for="(country, index) in countrylist" :key="index">
        <input
          type="checkbox"
          class="form-check-input"
          :id=country :value="country"
          v-model="checkedCountries">
        <label :for=country> {{ country }}</label>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <span>
      Checked countries:
      {{ (checkedCountries.length === 0) ? 'None' : checkedCountries}}
    </span>
  </div>
</template>

<script>
import axios from 'axios'

const backendPath = process.env.VUE_APP_ROOT_API

export default {
  name: 'TravelAlerts',
  data () {
    return {
      checked: false,
      checkedNames: [],
      checkedCountries: [],
      countrylist: []
    }
  },
  methods: {
    getCountryList () {
      const path = `${backendPath}/countrylist`
      axios.get(path)
        .then((res) => {
          this.countrylist = res.data.country_list
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    backHome () {
      this.$router.push('/')
    }
  },
  created () {
    this.getCountryList()
  }
}
</script>
