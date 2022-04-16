<template>
  <div class="login">
    <h2>Login</h2>
    <router-link to="/signup" class="nav-link"><button>Register</button></router-link>
    {{}}
    <form class="login-box">
      <div class="email-address">
        <label for="email"><b> Email </b></label>
        <br>
        <input type="text" id="email" v-model="email" />
      </div>
      <div class="PW">
        <label for="password"><b> Password </b></label>
        <br>
        <input type="password" id="password" v-model="password" />
      </div>
      <button @click="login">Login</button>
    </form>
  </div>
</template>
<script>
import firebase from "firebase/app";
import "firebase/auth";
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login(e) {
      e.preventDefault();
      console.log("Hello");
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then((user) => {
          alert("You are logged in as " + user.user.email);
          console.log(user.user.email);
          this.$store.commit("setUsername", user.user.email);
          this.$store.commit("setLogin", true);
          this.$router.push("/");
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
};
</script>
<style scoped>
  body {
    margin: 0;
    padding: 0;
    background-color: #6abadeba;
    font-family: 'Arial';
  }
  .login-box {
    width: 382px;
    overflow: hidden;
    margin: auto;
    margin: 20 0 0 450px;
    padding: 80px;
    background: #23463f;
    border-radius: 15px;
  }
  h2 {
    text-align: center;
    color: #277582;
    padding: 20px;
  }
  label {
    color: #6abadeba;
    font-size: 17px;
  }
  #email {
    width: 300px;
    height: 30px;
    border: none;
    border-radius: 3px;
    padding-left: 8px;
    margin: 8px;
  }
  #password {
    width: 300px;
    height: 30px;
    border: none;
    border-radius: 3px;
    padding-left: 8px;
    margin: 8px;
  }
  input {
    border: #000;
    text-align: center;
    font-family: monospace;
    box-sizing: border-box;
    font-size: 20px;
  }
  input[type=text] {
      width: 70%;
      padding: 12px 20px;
      /*margin: 8px 0;*/
      border-radius: 10px;
  }
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  button {
      /*width: 15%;*/
      /*font-size: 2vw;*/
      padding: 12px 20px;
      margin: 8px 0;
      margin-top: 30px;
      border-radius: 10px;
      background-color: var(--button);
      color: var(--button-text);
      border: 1px solid #111;
      transition: background-color 2s, color 2s;
  }
  button:hover {
      cursor: pointer;
      background-color: var(--button-hover);
      color: var(--button-hover-text);
      border: 1px solid black;
      /* transition: color 0s, background-color 0s; */
  }
  .login {
    --color: #8e3d35;
    --color-secondary: red;
    --nav: #252525;
    --nav-link: #a10ae7;
    --nav-link-exact: #ee37cf;
    --body: #6930C3;
    --footer: #2f1544;
    --social: #80FFDB;
    --border: #eb7a39;
    --button: #80FFDB;
    --button-text: rgb(0, 0, 0);
    --button-hover: #6930C3;
    --button-hover-text: #64DFDF;
    background: #64DFDF;
    --background: #f80000;
    --text-color-primary: #64DFDF;
    --vs-controls-color: #664cc3;
    --vs-border-color: #664cc3;
    --vs-dropdown-bg: #282c34;
    --vs-dropdown-color: #cc99cd;
    --vs-dropdown-option-color: #cc99cd;
    --vs-selected-bg: #664cc3;
    --vs-selected-color: #eeeeee;
    --vs-search-input-color: #eeeeee;
    --vs-dropdown-option--active-bg: #664cc3;
    --vs-dropdown-option--active-color: #eeeeee;
  }
</style>