<template>
  <div>
    <h2>Login</h2>
    <router-link to="/signup"> Register</router-link>
    {{}}
    <form>
      <div>
        <label for="email"> Email </label>
        <input type="text" id="email" v-model="email" />
      </div>
      <div>
        <label for="password"> Password </label>
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