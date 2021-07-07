<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h2>Travel Allowances</h2>
        <alert :message=message v-if="showMessage"></alert>
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
        <h2>Flight Booking</h2>
        <a href="../jsp/singpassLogin.jsp" onclick="clickAndDisable(this);">
          <img
            src="../assets/loginsingpass.png"
            class="img-fluid"
            width="230"
            border="0"
            alt="Login with Singpass"
            title="Login with Singpass">
        </a>
        <div v-if="!$auth.loading">
          <!-- show login when not authenticated -->
          <button v-if="!$auth.isAuthenticated" @click="login">Log in</button>
          <!-- show logout when authenticated -->
          <button v-if="$auth.isAuthenticated" @click="logout">Log out</button>
        </div>
        <div id="nav">
          <router-link v-if="$auth.isAuthenticated" to="/profile">Profile</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const backendPath = process.env.VUE_APP_ROOT_API;

export default {
  name: 'Home',
  data() {
    return {
      countries: [],
      message: '',
      showMessage: false,
    };
  },
  methods: {
    getCountries() {
      const path = `${backendPath}/countries`;
      axios.get(path)
        .then((res) => {
          this.countries = res.data.countries;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    login() {
      this.$auth.loginWithRedirect();
    },
    // Log the user out
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin,
      });
    },
  },
  created() {
    this.getCountries();
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
