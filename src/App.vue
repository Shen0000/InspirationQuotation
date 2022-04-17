<template>
  <div>
    <ul class="navbar">
      <li>
        <router-link to="/">
          <img
            src="./assets/iq_logo.png"
            alt="logo"
            width="60"
            height="60"
            class="logo"
          />
        </router-link>
      </li>
      <li v-if="!$store.state.loggedIn">
        <router-link to="/login" class="login-button">Login</router-link>
      </li>
      <li v-if="$store.state.loggedIn">
        <router-link to="/daily" class="nav-element">Daily Quote</router-link>
      </li>
      <li v-if="$store.state.loggedIn">
        <button @click="logout" class="nav-element">Logout</button>
      </li>
      <!-- <li>
        <router-link to="/quotes" class="nav-element">Quotes</router-link>
      </li> -->
      <li v-if="$store.state.loggedIn">
        <router-link to="/settings" class="nav-element">Settings</router-link>
      </li>
      <li>
        <p>{{ this.$store.state.username }}</p>
      </li>
    </ul>

    <br />

    <div class="main-container">
      <router-view />
    </div>
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
  background-color: #222;
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #988cf3;
  width: 100%;
}

li {
  color: white;
  font-size: 14px;
  height: 100%;
}

li a {
  float: left;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  height: 100%;
}
li button {
  float: right;
  background-color: #988cf3;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  border: none;
  cursor: pointer;
  color: white;
  font-size: 14px;
}
li p {
  float: right;
  vertical-align: text-top;
  margin-right: 20px;
}
/* Change the link color to #111 (black) on hover */
li a:hover {
  background-color: #111;
}
li button:hover {
  background-color: #111;
}
img {
  vertical-align: text-top;
}
.main-container {
  margin-top: 100px;
}
.login-button {
  float: right;
  margin-right: 20px;
}
</style>
