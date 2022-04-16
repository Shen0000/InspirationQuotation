<template>
    <div>
        Quotes
        <div class="quotes-wrapper">
          <div class="quotes" v-for="n in length-1" v-bind:key="n">
            <p>"{{quotes[n]}}"</p> <i>{{authors[n]}}</i>
          </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Quotes',
    data() {
      return {
        quotes: [],
        authors: [],
        length: 0,
      };
    },
    methods: {
      getData() {
        fetch(`http://localhost:5000/get-quotes?query=men&author=/authors/eminem-quotes`)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.quotes = data[0];
          this.authors = data[1];
          this.length = data[2];
        });
        
      },
    },
    created() {
      this.getData();
    }
}
</script>

<style scoped>

</style>