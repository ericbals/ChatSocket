<template>
    <h3><b>{{userName}}</b>: {{lastMessage}}</h3>
    <v-divider></v-divider>
</template>

<script>
  export default {
    name: 'MessageComponent',
    props: {
        lastMessage: String,
        messageHistory: [String],
        userName: String
    },
    data: () => ({
      messages: []
    }),
  }
</script>