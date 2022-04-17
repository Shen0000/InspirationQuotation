<template>
  <div>
    <h2>Daily Quote</h2>
    <br />
    <div v-if="loading" class="loader"></div>
    <div v-else>
      <Tilt :options="this.options" :parallax="true" class="background">
        <div class="blockquote">
          <h1 class="quote">{{ dailyQuote }}</h1>
          <h2 class="author">{{ author }}</h2>
        </div>
      </Tilt>
      <h4>Come back tomorrow for another quote!</h4>
    </div>
  </div>
</template>
<script>
import Tilt from "../components/Tilt";
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";
import Categories from "../../db/categories.json";
import Authors from "../../db/authors.json";
import db from "../components/firebaseInit";
export default {
  name: "Login",
  components: {
    Tilt,
  },
  data() {
    return {
      loading: true,
      dailyQuote: "",
      author: "",
      categoryPreferences: [],
      authorPreferences: [],
      allCategories: JSON.parse(Categories),
      allAuthors: JSON.parse(Authors),
      options: {
        max: 25,
        perspective: 1000,
        scale: 1.05,
        speed: 500,
        easing: "cubic-bezier(.03,.98,.52,.99)",
        glare: true,
      },
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
              if (
                res.data().categoryPreferences.length > 0 ||
                res.data().authorPreferences.length > 0
              ) {
                this.categoryPreferences = res.data().categoryPreferences;
                this.authorPreferences = res.data().authorPreferences;
              } else {
                this.categoryPreferences = this.allCategories;
                this.authorPreferences = this.allAuthors;
              }
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
          this.$toast.open({
            message: "Sign in before viewing your daily quote",
            type: "warning",
          });
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

<style scoped>
.background {
  height: auto;
  width: 50vw;
  background-image: linear-gradient(#000, #988cf3);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 50px;
  margin: 0 auto;
  transform-style: preserve-3d;
  transform: perspective(1000px);
}

.quote {
  font-family: "Square Peg";
  font-size: 5rem;
}

.author {
  font-size: 3rem;
  /* doesn't actually do anything */
}

.blockquote {
  position: relative;
  color: white;
  border-top: solid 1px;
  border-bottom: solid 1px;
  padding: 30px;
  margin-bottom: 40px;
  transform: translateZ(50px);
  /* font-family: "Square Peg"; */
}
.blockquote::before {
  position: absolute;
  content: "“";
  color: rgb(255, 255, 255);
  font-size: 10rem;
  transform: translateY(-33%);
  line-height: 1;
  top: 0px;
  left: 20px;
}
.blockquote::after {
  position: absolute;
  content: "”";
  color: rgb(0, 0, 0);
  font-size: 10rem;
  line-height: 1;
  transform: translateY(83%);
  right: 20px;
  bottom: 0px;
}

.blockquote h2 {
  position: relative;
  color: #ffffff;
  font-size: 1.4rem;
  font-weight: normal;
  line-height: 1;
  margin: 0;
  padding-top: 20px;
}
.loader {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #988cf3; /* Blue */
  border-radius: 50%;
  width: 100px;
  height: 100px;
  animation: spin 2s linear infinite;
  margin: 0 auto;
}
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>