<template>
  <div class="register">
    <h2>Signup</h2>
    <form class="login-box">
      <div>
        <label for="email"><b> Email </b></label>
        <br />
        <input type="text" id="email" v-model="email" />
      </div>
      <div>
        <label for="password"><b> Password </b></label>
        <br />
        <input type="password" id="password" v-model="password" />
      </div>
      <button @click="signup" type="submit">Signup</button>
    </form>
  </div>
</template>
<script>
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";
import db from "../components/firebaseInit";
export default {
  name: "Signup",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    signup(e) {
      e.preventDefault();
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then((user) => {
          db.collection("users").doc(user.user.uid).set({
            dailyQuote: "",
            dailyQuoteAuthor: "",
            categoryPreferences: [],
            authorPreferences: [],
            lastLogin: firebase.firestore.FieldValue.serverTimestamp(),
          });
          this.$toast.open({
            message: "Account created for " + user.user.email,
            type: "success",
            onDismiss: () => {
              this.$router.push("/");
            },
          });
        })
        .catch((error) => {
          this.$toast.open({
            message: error,
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
  background-color: #6abadeba;
  font-family: "Arial";
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
input[type="text"] {
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
}
.register {
  --button: #80ffdb;
  --button-text: rgb(0, 0, 0);
  --button-hover: #6930c3;
  --button-hover-text: #64dfdf;
  background: #222;
}
</style>