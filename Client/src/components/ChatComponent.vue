<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Chat SocketIO
        </h1>
      </v-col>
    </v-row>
    <v-row v-for="user in users" :key="user.username">
      {{user.username}}
    </v-row> 

    <v-row>
      <v-container class="chat-box text-center">
        Message History
        <MessageComponent v-for="message in messages" :key="message" :user-name="user.username" :last-message="message"/>
      </v-container>
      <v-card
    class="mx-auto my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>
    <v-card-text>
      <div>
        <v-text-field
          label="@ericbals"
          v-model="currentMessage"
          hide-details="auto"
        ></v-text-field>
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        type="text"
        @click="sendMessage"
        placeholder="Start chatting..."
      >
      </v-btn>
    </v-card-actions>
  </v-card>
    </v-row>
  </v-container>
  
</template>

<style lang="css">
  .chat-box {
    border: 1px solid black;
  }
</style>

<script>
import MessageComponent from './MessageComponent';
  export default {
    name: 'ChatComponent',
    components: {
      MessageComponent
    },
    props: {
      users: [],
      messages: [],
    },
    data: () => ({
      currentMessage: "",
      user: {}
    }),
    methods: {
      sendMessage () {
        this.$emit('message', this.currentMessage);
        this.currentMessage = "";
      }
    },
    created: {
      defineUser() {
        this.user = this.$store.getters.currentUser;
      }
    }
  }
</script>