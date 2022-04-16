<template>
  <div>
    <h1>Settings Page</h1>
    <!-- <br /> -->
    <h2>Quote Preferences you have chosen:</h2>
    <!-- {{ [...categoryPreferences, ...authorPreferences].join(", ") }} -->
    <div class="grid-container">
      <div class="grid-item" v-for="preference in categoryPreferences" v-bind:key="preference.id">
        <p>{{preference}}</p>
      </div>
      <div class="grid-item" v-for="preference in authorPreferences" v-bind:key="preference.id">
        <p>{{preference}}</p>
      </div>
    </div>
    <br />
    <br />
    <div class="v-select-wrapper">
      <div class="categories-select">
        <h2>Categories</h2>
        <v-select
          multiple
          v-model="currentCategoryPreferences"
          :options="categories"
        ></v-select>
      </div>
      <div class="authors-select">
        <h2>People</h2>
        <v-select
          multiple
          v-model="currentAuthorPreferences"
          :options="authors"
        ></v-select>
      </div>
    </div>
    
    <!-- <p v-for="option in combined" v-bind:key="option.id">{{option}}</p> -->
    <button @click="changeSettings" class="settings-button"><span>Update settings</span></button>
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
      currentCategoryPreferences: [],
      currentAuthorPreferences: [],
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
              this.currentCategoryPreferences = this.categoryPreferences;
              this.currentAuthorPreferences = this.authorPreferences;
            });
        } else {
          console.log("User must login");
        }
      });
    },
    changeSettings() {
      console.log("Settings updated!");
      this.authorPreferences = this.currentAuthorPreferences;
      this.categoryPreferences = this.currentCategoryPreferences;
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

.v-select-wrapper {
  display: flex;
  flex-direction: row;
  margin: 10px;
}

.categories-select {
  width: 50%;
  margin: 5px;
  padding: 5px;
}

.authors-select {
  width: 50%;
  margin: 5px;
  padding: 5px;
}

.grid-container {
  display: grid;
  align-items: center;
  grid-template-columns: repeat(auto-fill, minmax(235px, 1fr));
  max-width: 1500px;
  grid-row-gap: 50px;
  grid-column-gap: 50px;
  margin: 3vh auto;
  padding-right: 3vw;
  padding-left: 3vw;
}

.grid-item {
  background-color:#988cf3;
  border-radius: 5px;
  box-sizing: border-box;
  width: 250px;
  cursor: pointer;
  transition: all 0.25s ease;
  height: 5vh;
  text-align: center;
  vertical-align: middle;
}

.grid-item:hover {
  transform: scale(1.1, 1.1);
  opacity: 0.8;
}

.settings-button {
  display: inline-block;
  border-radius: 4px;
  background-color: #988cf3;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 18px;
  padding: 20px;
  width: 200px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.settings-button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.settings-button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.settings-button:hover span {
  padding-right: 25px;
}

.settings-button:hover span:after {
  opacity: 1;
  right: 0;
}

</style>