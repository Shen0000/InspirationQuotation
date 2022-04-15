<template>
  <div>
    <h2>Signup</h2>
    <form>
      <div>
        <label for="email"> Email </label>
        <input type="text" id="email" v-model="email" />
      </div>
      <div>
        <label for="password"> Password </label>
        <input type="password" id="password" v-model="password" />
      </div>
      <button @click="signup" type="submit">Signup</button>
    </form>
  </div>
</template>
<script>
import firebase from "firebase"
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
      console.log("Hello");
      firebase.auth().createUserWithEmailAndPassword(
        this.email,
        this.password
      ).then((user) => {
          alert("Account created for " + user.user.email);
          this.$router.push("/")
        })
        .catch((error) => {
          alert(error)
        });
    },
  },
};
</script>