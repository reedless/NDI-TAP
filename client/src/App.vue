<template>
  <div id="app">
    <div
      v-if="hasAccess"
      id="nav"
      style="float: right;">
      <b-button
        href @click.prevent="eRegister"
        variant="outline-primary">eRegister</b-button>
      <b-button
        v-if="oidcIsAuthenticated"
        href @click.prevent="signOut"
        variant="outline-danger">Sign out</b-button>
      <b-button
        v-else href
        @click.prevent="login"
        variant="danger">Log in with Singpass</b-button>
    </div>
    <div id="nav">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters('oidcStore', [
      'oidcIsAuthenticated'
    ]),
    hasAccess: function () {
      return this.oidcIsAuthenticated || this.$route.meta.isPublic
    }
  },
  methods: {
    ...mapActions('oidcStore', [
      'authenticateOidcPopup',
      'removeOidcUser'
    ]),
    userLoaded: function (e) {
      console.log('I am listening to the user loaded event in vuex-oidc', e.detail)
    },
    oidcError: function (e) {
      console.log('I am listening to the oidc oidcError event in vuex-oidc', e.detail)
    },
    automaticSilentRenewError: function (e) {
      console.log('I am listening to the automaticSilentRenewError event in vuex-oidc', e.detail)
    },
    login: function () {
      this.$router.push('/protected')
    },
    signOut: function () {
      this.removeOidcUser().then(() => {
        this.$router.push('/')
      })
    },
    eRegister: function () {
      window.open('https://eregister.mfa.gov.sg/')
    }
  },
  mounted () {
    window.addEventListener('vuexoidc:userLoaded', this.userLoaded)
    window.addEventListener('vuexoidc:oidcError', this.oidcError)
    window.addEventListener('vuexoidc:automaticSilentRenewError', this.automaticSilentRenewError)
  },
  destroyed () {
    window.removeEventListener('vuexoidc:userLoaded', this.userLoaded)
    window.removeEventListener('vuexoidc:oidcError', this.oidcError)
    window.removeEventListener('vuexoidc:automaticSilentRenewError', this.automaticSilentRenewError)
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
