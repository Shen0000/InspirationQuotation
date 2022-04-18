<template>
  <div>
    <div class="main-container">
      <img
        src="../assets/thought.png"
        alt="thought bubble image"
        class="main-image"
        draggable="false"
      />
      <h1 class="main-text">Inspiration Quotation</h1>
      <router-link :to="{ path: '/', hash: '#mission' }"
        ><img alt="Arrow Down Icon" src="../assets/arrow.png" class="arrow"
      /></router-link>
    </div>
  </div>
  <div class="mission-statement">
    <h2 id="mission">Mission Statement</h2>
    <p>
      Inspiration Quotation seeks to inspire and motivate through the words of
      those who have already had success in life. With our Daily Quote, we hope
      to push you to become a better you every day, and we strive to personalize
      our message to your interests through our preferences page. At IQ, you
      won’t find anything superficial or generalized; every quote will be
      tailored to who you are to maximize your potential and improve your
      mindset each and every day.
    </p>
    <strong v-if="!$store.state.loggedIn">
      <router-link to="/login" class="nav-element login-button"
              >Login</router-link
            > and configure your preferred quote settings to get started!
    </strong>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.main-container {
  height: 100%;
  display: flex;
  position: relative;
  justify-content: center;
  align-content: center;
  flex-direction: column;
}
.main-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50vw;
  min-width: 300px;
  user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-drag: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
.main-text {
  font-size: 4vw;
  color: #988cf3;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -185%);
}
.mission-statement {
  background-color: #988cf3;
  padding: 20px;
  color: white;
}
.mission-statement h2 {
  font-size: 3em;
}
.mission-statement p,
strong {
  margin-left: 50px;
  margin-right: 50px;
  font-size: 1.5em;
  line-height: 1.6;
}

.arrow {
  height: max(5vh, 5vw);
  user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-drag: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
</style>