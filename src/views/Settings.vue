<template>
  <div>
    <h1>Settings Page</h1>
    <!-- {{combined}} -->
    Quote Preferences you have chosen:
    {{ [...categoryPreferences, ...authorPreferences].join(", ") }}
    <br />
    <br />
    Categories
    <v-select
      multiple
      v-model="categoryPreferences"
      :options="categories"
    ></v-select>
    People
    <v-select
      multiple
      v-model="authorPreferences"
      :options="authors"
    ></v-select>
    <!-- <p v-for="option in combined" v-bind:key="option.id">{{option}}</p> -->
    <button @click="changeSettings">Update settings</button>
  </div>
</template>

<script>
import Paths from "../../db/paths.json";
import Categories from "../../db/categories.json";
import Authors from "../../db/authors.json";
import Keywords from "../../db/keywords.json";
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";
import db from "../components/firebaseInit";
export default {
  name: "settings",
  data() {
    return {
      loading: true,
      paths: JSON.parse(Paths),
      categories: JSON.parse(Categories),
      authors: JSON.parse(Authors),
      keywords: JSON.parse(Keywords),
      combined: [],
      categoryPreferences: [],
      authorPreferences: [],
    };
  },
  methods: {
    getUserCategories() {
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
          db.collection("users")
            .doc(user.uid)
            .get()
            .then((res) => {
              this.categoryPreferences = res.data().categoryPreferences;
              this.authorPreferences = res.data().authorPreferences;
            });
        } else {
          console.log("User must login");
        }
      });
    },
    changeSettings() {
      console.log("Settings updated!");
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
          db.collection("users").doc(user.uid).update({
            authorPreferences: this.authorPreferences,
            categoryPreferences: this.categoryPreferences,
          });
        } else {
          console.log("User must login");
        }
      });
    },
  },
  created() {
    this.getUserCategories();
  },
};
</script>

<style scoped>
</style>