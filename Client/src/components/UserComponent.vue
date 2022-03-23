 <!-- WORK IN PROGRESS TEMPLATE FOR MORE COMPLEX USER FEATURES 

<template>
  <v-container>
    <v-img v-for="user in getUsers()" :key="user.username"
            lazy-src="https://picsum.photos/id/11/10/6"
            max-height="150"
            max-width="150"
            src="https://picsum.photos/id/11/500/300"
            @click="openChat(user)"
          ></v-img>
  </v-container>
  
</template>

<script>
  export default {
    name: 'UserComponent',
    props: {
      user: {}
    },
  }
</script>

-->