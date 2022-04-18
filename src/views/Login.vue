<template>
  <div class="login">
    <h2>Login</h2>
    <router-link to="/signup" class="nav-link"
      ><button>Register</button></router-link
    >
    <form class="login-box">
      <div class="email-address">
        <label for="email"><b> Email </b></label>
        <br />
        <input type="text" id="email" v-model="email" />
      </div>
      <div class="PW">
        <label for="password"><b> Password </b></label>
        <br />
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
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then((user) => {
          this.$toast.open({
            message: "You are logged in as " + user.user.email,
            type: "success",
            onDismiss: () => {
              this.$router.push("/");
            },
          });
          this.$store.commit("setUsername", user.user.email);
          this.$store.commit("setLogin", true);
        })
        .catch((error) => {
          this.$toast.open({
            message: error.message,
            type: "error",
          });
        });
    },
  },
};
</script>
<style scoped>
body {
  margin: 0;
  padding: 0;
}
.login-box {
  width: 50vw;
  max-width: 400px;
  overflow: hidden;
  margin: auto;
  margin: 20 0 0 450px;
  padding: 80px;
  background: #988cf3;
  border-radius: 15px;
}
h2 {
  text-align: center;
  color: rgb(233, 215, 215);
  padding: 20px;
}
label {
  color: #000;
  font-size: 17px;
}
#email {
  width: 80%;
  height: 30px;
  border: none;
  border-radius: 3px;
  padding-left: 8px;
  margin: 8px;
}
#password {
  width: 80%;
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
input[type="text"] {
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
  --button: #80ffdb;
  --button-text: rgb(0, 0, 0);
  --button-hover: #6930c3;
  --button-hover-text: #64dfdf;
  background: #222;
}
</style>