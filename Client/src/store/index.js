import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const messageStore ={
    state: {
        historyMessages: [],
      },
    mutations: {
        addToHistory_mutation(state, payload) {
          state.historyMessages.push(payload);
        }
    },
    actions: {
        addToHistory_action (context, payload) {
          context.commit('addToHistory_mutation', payload);
        }
    },
    getters: {
        allMessages (state) {
          return state.historyMessages;
        }
    }
}

const userStore = {
  state: {
    all: [],
    currentUser: {}
  },
   mutations: {
    addUser(state, payload) {
      state.all = payload.users;
      state.all.push(payload.user);
      state.currentUser = payload.user;
    },
    setAllUsers(state, payload){
      state.all = payload;
    }
  },
  actions: {
    addUser (context, payload) {
      console.log(payload);
      context.commit('addUser', payload);
    },
    setAllUsersAction (context, payload){
      context.commit('setAllUsers', payload);
    }
  },
  getters: {
    users (state) {
      return state.all
    },
    currentUser (state) {
      return state.currentUser
    }
}
}

export const store = new Vuex.Store({
  modules: {
    messageStore: messageStore,
    userStore: userStore
  }
})