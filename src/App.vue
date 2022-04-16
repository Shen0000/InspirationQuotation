<template>
  <div>
    <div class="navbar">
      <ul>
        <li v-if="!$store.state.loggedIn">
          <router-link to="/login">Login</router-link>
        </li>
        <router-link to="/daily"><li>View Daily Quote</li></router-link>
        <li>
          {{ this.$store.state.username }}
        </li>
        <li v-if="$store.state.loggedIn">
          <button @click="logout">Logout</button>
        </li>
        <router-link to="/quotes">Quotes</router-link>
        <br />
        <li><router-link to="/settings">Settings</router-link></li>
      </ul>
    </div>
    <router-view />
  </div>
</template>

<script>
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";
import db from "./components/firebaseInit";
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
          this.$router.push("/");
          this.$store.commit("setUsername", "");
          this.$store.commit("setLogin", "");
          alert("Signed out!");
        });
    },
  },
  created() {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        db.collection("users").doc(user.uid).update({
          lastLogin: firebase.firestore.FieldValue.serverTimestamp(),
        });
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
</style>
