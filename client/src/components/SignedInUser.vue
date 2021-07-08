<template>
  <div>
    <h2>Flight Booking</h2>
    <div v-if="oidcIsAuthenticated">
      <div class="bootstrap-iso">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6 col-sm-6 col-xs-12">
              <form>
                <div class="form-inline">
                  <label class="control-label" for="date">From: </label>
                  &ensp;
                  <select class="custom-select" v-model="from">
                    <option selected>Select Country</option>
                    <option value="Singapore"> Singapore </option>
                    <option
                      v-for="(country, index) in countries" :key="index"
                      :value=country.name>
                        {{ country.name }}
                    </option>
                  </select>
                  &emsp;
                  <label class="control-label" for="date">To: </label>
                  &ensp;
                  <select class="custom-select" v-model="to">
                    <option selected>Select Country</option>
                    <option value="Singapore"> Singapore </option>
                    <option
                      v-for="(country, index) in countries" :key="index"
                      :value=country.name>
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
                  <button class="btn btn-primary " name="submit" type="submit">Submit</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
    <!-- <div v-else-if="oidcAuthenticationIsChecked"> -->
      <a href="/protected" onclick="clickAndDisable(this);">
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
import { mapGetters, mapActions } from 'vuex'
import Datepicker from 'vuejs-datepicker'
import jsonMarkup from 'json-markup'

export default {
  name: 'SignedInUser',
  props: ['countries'],
  components: {
    Datepicker
  },
  data () {
    const now = new Date()
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
    var yesterday = new Date(today)
    yesterday.setDate(today.getDate() - 1)

    return {
      from: 'Select Country',
      to: 'Select Country',
      min: yesterday,
      departDate: '',
      returnDate: '',
      disabledDates: {
        to: yesterday
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
    ]),
    userDisplay: function () {
      return jsonMarkup(this.oidcUser)
    }
  },
  methods: {
    ...mapActions('oidcStore', ['authenticateOidcSilent', 'removeOidcUser']),
    reauthenticate () {
      this.authenticateOidcSilent()
        .catch(() => this.removeOidcUser())
    }
  }
}
</script>
