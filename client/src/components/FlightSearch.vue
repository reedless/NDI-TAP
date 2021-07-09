<template>
  <div>
    <h2>Flight Search</h2>
    <div v-if="oidcIsAuthenticated">
      <div class="bootstrap-iso">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6 col-sm-6 col-xs-12">
              <form @submit.prevent="flightSearch">
                <div class="form-inline">
                  <label class="control-label" for="date">From: </label>
                  &ensp;
                  <select class="custom-select" v-model="from" name="from">
                    <option selected value="SIN"> Singapore </option>
                  </select>
                  &emsp;
                  <label class="control-label" for="date">To: </label>
                  &ensp;
                  <select class="custom-select" v-model="to" name="to">
                    <option selected>Select Country</option>
                    <option
                      v-for="(country, index) in countries" :key="index"
                      :value=country.airportCode>
                        {{ country.name }}
                    </option>
                  </select>
                </div>
                <br>
                <p>{{ from }}, {{ to }}</p>
                <br>
                <div class="form-row">
                  <label
                    class="control-label"
                    for="date"
                    >Depart: </label>
                  &ensp;
                  <datepicker
                    name="depart"
                    v-model="departDate"
                    :disabled-dates="disabledDates"></datepicker>
                  &emsp;
                  <label
                    class="control-label"
                    for="date">Return: </label>
                  &ensp;
                  <datepicker
                   name="return"
                    v-model="returnDate"
                   :disabled-dates="{ to: departDate }"></datepicker>
                </div>
                <br>
                <p>{{ departDate }}, {{ returnDate }}</p>
                <div class="form-group">
                  <button class="btn btn-primary" type="submit">Submit</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <a href="/login" onclick="clickAndDisable(this);">
        <img
          src="../assets/loginsingpass.png"
          class="img-fluid"
          width="230"
          border="0"
          alt="Login with Singpass"
          title="Login with Singpass">
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'
import Datepicker from 'vuejs-datepicker'
import Vue from 'vue'
import VueAxios from 'vue-axios'
// import jsonMarkup from 'json-markup'

Vue.use(VueAxios, axios)

const flightSearchPath = process.env.SIA_API_FLIGHT_SEARCH || `https://apigw.singaporeair.com/api/v1/commercial/flightavailability/get`
const headers = {
  'Content-Type': 'application/json',
  'apikey': process.env.SIA_API_FLIGHT_SEARCH || 'z7m5yus6xwub4uebucx8e24y'
}

export default {
  name: 'FlightSearch',
  props: ['countries'],
  components: {
    Datepicker
  },
  data () {
    const now = new Date()
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
    var tomorrow = new Date(today)
    tomorrow.setDate(today.getDate() + 1)

    return {
      from: 'SIN',
      to: 'Select Country',
      departDate: '',
      returnDate: '',
      disabledDates: {
        to: tomorrow
      }
    }
  },
  computed: {
    ...mapGetters('oidcStore', [
      'oidcIsAuthenticated',
      'oidcAuthenticationIsChecked',
      'oidcUser',
      'oidcIdToken',
      'oidcIdTokenExp'
    ])
    // userDisplay: function () {
    //   return jsonMarkup(this.oidcUser)
    // }
  },
  methods: {
    ...mapActions('oidcStore', ['authenticateOidcSilent', 'removeOidcUser']),
    reauthenticate () {
      this.authenticateOidcSilent()
        .catch(() => this.removeOidcUser())
    },
    formatDate (date) {
      var d = new Date(date)
      var month = '' + (d.getMonth() + 1)
      var day = '' + d.getDate()
      var year = d.getFullYear()

      if (month.length < 2) {
        month = '0' + month
      }
      if (day.length < 2) {
        day = '0' + day
      }

      return [year, month, day].join('-')
    },
    flightSearch () {
      console.log('Inside flightSearch')
      const path = flightSearchPath
      const data = {
        'clientUUID': 'SQ-API-Flight-Search',
        'request': {
          'itineraryDetails': [
            {
              'originAirportCode': this.from,
              'destinationAirportCode': this.to,
              'departureDate': this.formatDate(this.departDate),
              'returnDate': this.formatDate(this.returnDate)
            }
          ],
          'cabinClass': 'Y',
          'adultCount': 1,
          'childCount': 0,
          'infantCount': 0
        }
      }
      console.log('POST flightSearch')
      console.log(flightSearchPath)
      console.log(headers)
      console.log(data)
      axios.post(path, data, {
        headers: headers
      }).then((response) => {
        console.log(response)
      }).catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      })
    }
  }
}
</script>
