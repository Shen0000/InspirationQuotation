<template>
  <div>
    <h2>Daily Quote</h2>
    <br />
    <div v-if="loading">Loading Quote, please wait</div>
    <div v-else-if="categoryPreferences.length === 0">
      Go to settings and choose your preferences before viewing your daily
      quote!
    </div>
    <div v-else>
      {{ '"' + dailyQuote + '"' }}
      <br />
      {{ author }}
    </div>
  </div>
</template>
<script>
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/auth";
import "firebase/firestore";
import db from "../components/firebaseInit";
export default {
  name: "Login",
  data() {
    return {
      loading: true,
      dailyQuote: "",
      author: "",
      categoryPreferences: [],
      authorPreferences: [],
    };
  },
  methods: {
    getData() {
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
          db.collection("users")
            .doc(user.uid)
            .get()
            .then((res) => {
              this.categoryPreferences = res.data().categoryPreferences;
              this.authorPreferences = res.data().authorPreferences;
              if (
                res.data().dailyQuote.length > 0 &&
                this.checkDates(res.data().lastLogin.toDate(), new Date())
              ) {
                this.dailyQuote = res.data().dailyQuote;
                this.author = res.data().dailyQuoteAuthor;
                this.loading = false;
                console.log(
                  this.checkDates(res.data().lastLogin.toDate(), new Date())
                );
              } else {
                this.getQuote();
              }
              db.collection("users").doc(user.uid).update({
                lastLogin: firebase.firestore.FieldValue.serverTimestamp(),
              });
            })
            .catch((err) => console.error(err));
        } else {
          console.log("User must login");
        }
      });
    },
    getQuote() {
      // pick random category
      const categories = [
        ...this.categoryPreferences,
        ...this.authorPreferences,
      ];
      const randomCat =
        categories[Math.floor(Math.random() * categories.length)];
      console.log(randomCat);
      let query = "";
      if (this.categoryPreferences.includes(randomCat)) {
        query = `http://localhost:5000/get-quotes?query=${randomCat}`;
      } else if (this.authorPreferences.includes(randomCat)) {
        const formattedName = randomCat.replace(" ", "-") + "-quotes";
        query = `http://localhost:5000/get-quotes?author=/authors/${formattedName}`;
      }
      fetch(query)
        .then((response) => response.json())
        .then((data) => {
          const randomIndex = Math.floor(Math.random() * data[0].length);
          this.dailyQuote = data[0][randomIndex];
          this.author = data[1][randomIndex];
          firebase.auth().onAuthStateChanged((user) => {
            db.collection("users")
              .doc(user.uid)
              .update({
                dailyQuote: this.dailyQuote,
                dailyQuoteAuthor: this.author,
              })
              .then((this.loading = false));
          });
        })
        .catch((err) => console.error(err));
    },
    checkDates(d1, d2) {
      return (
        d1.getFullYear() === d2.getFullYear() &&
        d1.getMonth() === d2.getMonth() &&
        d1.getDate() === d2.getDate()
      );
    },
  },
  created() {
    this.getData();
  },
};
</script>