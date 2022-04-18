<template>
  <div>
    <div class="navbar">
      <ul>
        <div class="floatleft">
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
          <!-- <li>
          <router-link to="/quotes" class="nav-element">Quotes</router-link>
        </li> -->
          <li v-if="$store.state.loggedIn">
            <router-link to="/daily" class="nav-element"
              >Daily Quote</router-link
            >
          </li>
          <li v-if="$store.state.loggedIn">
            <router-link to="/settings" class="nav-element"
              >Settings</router-link
            >
          </li>
        </div>
        <div class="floatright">
          <li>
            <p style="padding: 20px">{{ this.$store.state.username }}</p>
          </li>
          <li v-if="!$store.state.loggedIn">
            <router-link to="/login" class="nav-element login-button"
              >Login</router-link
            >
          </li>
          <li v-if="$store.state.loggedIn">
            <button @click="logout" class="nav-element login-button">
              Logout
            </button>
          </li>
        </div>
      </ul>
    </div>

    <br />

    <div class="main-container">
      <router-view />
    </div>
    <footer>
      <ul class="social-list">
        <li class="social-list__item">
          <a
            class="social-list__link"
            href="https://github.com/Shen0000/InspirationQuotation"
            target="_blank"
            ><i class="fab fa-github" aria-hidden="true"></i
          ></a>
        </li>
      </ul>
    </footer>
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
          this.$toast.open({
            message: "Signed out!",
            type: "success",
            onDismiss: () => {
              this.$router.push("/");
            },
          });
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
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100&family=Square+Peg&display=swap');

body {
  background-color: #222;
  margin: 0;
}
#app {
  font-family: 'Montserrat', sans-serif;
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
  background-color: transparent;
  width: 100%;
}

.navbar li {
  color: white;
  font-size: 1.2rem;
  height: 100%;
  padding: 10px;
}

.navbar li a {
  float: left;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  height: 100%;
  transition: all 1s;
}
.navbar li button {
  float: right;
  background-color: transparent;
  text-align: center;
  padding: 14px 16px;
  /* text-decoration: none; */
  border: none;
  cursor: pointer;
  color: white;
  font-size: 1.2rem;
  font-family: "Montserrat", sans-serif;
  transition: all 1s;
}
.navbar li p {
  float: right;
  vertical-align: text-top;
  margin-right: 20px;
}
/* Change the link color to #111 (black) on hover */
.navbar li a:hover {
  color: rgb(248, 168, 255);
}
.navbar li button:hover {
  color: rgb(248, 168, 255);
}
.navbar img {
  vertical-align: text-top;
  transition: all 1s;
}

.navbar img:hover {
  opacity: 0.6;
  transform: scale(1.1);
}

.main-container {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  min-height: 100vh;
  /*the above is*/
  color: rgb(255, 255, 255);
  background-color: #222;
  /* transition: background-color 2s, color 2s; */
}
.navbar {
  background-image: linear-gradient(#988cf3, #222);
  width: 100%;
  transition: all 1s;
}
.nav-element {
  vertical-align: middle;
}
.login-button {
  position: relative;
  /* float: right; */
}
footer {
  background-color: rgb(0, 0, 0);
  /* padding: 3vw; */
  padding-top: 2vh;
  padding-bottom: 2vh;
  height: 15%;
  width: 100%;
}
.social-list__link:focus,
.social-list__link:hover {
  opacity: 0.8;
  outline: none;
}
.social-list__item:hover {
  transform: scale(1.1);
}
.social-list {
  list-style: none;
  display: flex;
  justify-content: center;
  margin: 2em 0;
  padding: 0;
}
.social-list__item {
  transition: transform 250ms ease-in-out;
  margin: 0 0.5em;
}
.social-list__link {
  font-size: 40px;
  color: white;
  padding: 0.5em;
  transition: color 2s;
}
.floatleft {
  float: left;
  display: flex;
  align-items: center;
}
.floatright {
  float: right;
  display: flex;
  align-items: center;
}
</style>