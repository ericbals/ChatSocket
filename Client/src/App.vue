<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    </v-app-bar>
    <v-main>
      <v-container>
      <h3>Online users</h3>
        <v-img v-for="user in getUsers()" :key="user.username"
            lazy-src="https://picsum.photos/id/11/10/6"
            max-height="150"
            max-width="150"
            src="https://picsum.photos/id/11/500/300"
            @click="openChat(user)"
          ></v-img>
      </v-container>
      <ChatComponent v-if="isChatOpened" :users="currentUser" :messages="messages" @message="sendMessage($event)" />
      <!-- all conversations 
      <ChatComponent :users="getUsers()" :messages="messages" @message="sendMessage($event)" />
      -->
    </v-main>
  </v-app>
</template>

<script>
import ChatComponent from './components/ChatComponent';
import SocketioService from './services/socketio.service.js';
export default {
  name: 'App',

  components: {
    ChatComponent,
  },
  data: () => ({
    messages: [],
    currentUser: {},
    isChatOpened: false
  }),
  methods: {
    getAllMessages() {
      return this.$store.getters.allMessages;
    },
    sendMessage(value) { 
      SocketioService.sendMessage(value);
      this.$store.dispatch('addToHistory_action', value);
      this.messages = this.getAllMessages();
    },
    getUsers() {
      return this.$store.getters.users;
    },
    openChat(user){
      this.isChatOpened = false;
      wait(100);
      this.currentUser = user;
      this.isChatOpened = true;
    }
  },
  created() {
    this.$store.dispatch('addUser', SocketioService.setupSocketConnection());
  },
  beforeUnmount() {
    SocketioService.disconnect();
  }
};
</script>
