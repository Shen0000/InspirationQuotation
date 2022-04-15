<template>
    <div>
        <h1>Settings page</h1>
        <!-- {{combined}} -->
        <v-select multiple v-model="preferences" :options='combined'></v-select>
        {{preferences}}
        <!-- <p v-for="option in combined" v-bind:key="option.id">{{option}}</p> -->
    </div>
</template>

<script>

import Paths from "../../db/paths.json"
import Categories from "../../db/categories.json"
import Authors from "../../db/authors.json"
import Keywords from "../../db/keywords.json"

export default {
    name: 'settings',
    data() {
        return {
            paths: JSON.parse(Paths),
            categories: JSON.parse(Categories),
            authors: JSON.parse(Authors),
            keywords: JSON.parse(Keywords),
            combined: [],
            preferences: [],
        };
    },
    methods: {
        
    },
    created() {
        this.combined = [].concat(this.categories, this.authors);
        // console.log(this.combined);
        // console.log("hello");
    }
}
</script>

<style scoped>

</style>