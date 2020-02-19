import messageService from '../../services/messageService';

const state = {
  messages: [],
};

const getters = {
  messages: (stateParam) => {
    return stateParam.messages;
  },
};

const actions = {
  getMessages({commit}) {
    messageService.fetchMessages()
        .then((messages) => {
          commit('setMessages', messages);
        });
  },
  addMessage({commit}, message) {
    messageService.postMessage(message)
        .then(() => {
          commit('addMessage', message);
        });
  },
  deleteMessage( {commit}, msgId) {
    messageService.deleteMessage(msgId);
    commit('deleteMessage', msgId);
  },
};

const mutations = {
  setMessages(stateParam, messages) {
    stateParam.messages = messages;
  },
  addMessage(stateParam, message) {
    stateParam.messages.push(message);
  },
  deleteMessage(stateParam, msgId) {
    stateParam.messages = stateParam.messages.filter((obj) => obj.pk !== msgId);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
