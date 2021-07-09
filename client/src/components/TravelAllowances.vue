<template>
  <div>
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
  </div>
</template>

<script>

export default {
  name: 'TravelAllowances',
  props: ['countries'],
  methods: {
    signUpAlerts () {
      this.$router.push('/travelalerts')
    }
  }
}

</script>
