<template>
  <div>
    <div class="navbar">
      <ul>
        <li v-if="!$store.state.loggedIn">
          <router-link to="/login">Login</router-link>
        </li>
        <li v-if="$store.state.loggedIn">
          <router-link to="/daily">View Daily Quote</router-link>
        </li>
        <li>
          {{ this.$store.state.username }}
        </li>
        <li v-if="$store.state.loggedIn">
          <button @click="logout">Logout</button>
        </li>
        <li><router-link to="/quotes">Quotes</router-link></li>

        <li v-if="$store.state.loggedIn">
          <router-link to="/settings">Settings</router-link>
        </li>
      </ul>
      <router-link to="/quotes">Quotes</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";
export default {
  name: "App",
  components: {},
  data() {
    return {};
  },
  methods: {
    logout() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$store.commit("setUsername", "");
          this.$store.commit("setLogin", "");
          alert("Signed out!");
          this.$router.push("/");
        });
    },
  },
  created() {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        console.log(user.email);
        this.$store.commit("setUsername", user.email);
        this.$store.commit("setLogin", true);
        console.log("Logged in from before", user);
      }
    });
  },
};
</script>

<style>
body {
  background-color: #64DFDF;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.navbar {
  border-style: solid;
}
.nav-link {
    text-decoration: none;
}
</style>
